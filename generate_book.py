
import os
import yaml
import anthropic
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()  # .envファイルから環境変数を読み込む

class BookGenerator:
    def __init__(self, syllabus_file):
        self.syllabus_file = syllabus_file
        self.client = anthropic.Anthropic(
            api_key=os.environ.get("ANTHROPIC_API_KEY"),  # 環境変数からAPI keyを取得。os.getenvではなくos.environ.getを使う 🔑
        )

    def generate_book(self):
        with open(self.syllabus_file, "r", encoding="utf-8", errors="ignore") as f:
            syllabus = yaml.safe_load(f)

        if not os.path.exists("book"):
            os.makedirs("book")

        for month_data in tqdm(syllabus["curriculum"], desc="Generating book"):
            month = month_data["month"]
            topics = month_data["topics"]
            lectures = month_data["lectures"]

            month_dir = f"book/month_{month}"
            if not os.path.exists(month_dir):
                os.makedirs(month_dir)

            for lecture in tqdm(lectures, desc=f"Month {month} lectures", leave=False):
                lecture_title = lecture["title"]
                lecture_description = lecture["description"]

                lecture_file = f"{month_dir}/{lecture_title}.md"

                lecture_content = self.generate_lecture_content(lecture_title, lecture_description)
                quiz_content = self.generate_quiz_content(lecture_title, lecture_description)

                with open(lecture_file, "w", encoding="utf-8", errors="ignore") as f:
                    f.write(f"# {lecture_title}\n\n")
                    f.write(lecture_content)
                    f.write("\n\n")
                    f.write(quiz_content)

    def generate_lecture_content(self, lecture_title, lecture_description):
        with open("ais/lecture_generator.md", "r", encoding="utf-8", errors="ignore") as f:
            lecture_content_prompt = f.read().format(lecture_title=lecture_title, lecture_description=lecture_description)

        response = self.client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=2000, 
            temperature=0.7,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": lecture_content_prompt
                        }
                    ]
                }
            ]
        )

        return response.content[0].text.strip()

    def generate_quiz_content(self, lecture_title, lecture_description):
        with open("ais/quiz_generator.md", "r", encoding="utf-8", errors="ignore") as f:
            quiz_content_prompt = f.read().format(lecture_title=lecture_title, lecture_description=lecture_description)

        response = self.client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1000,
            temperature=0.5,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": quiz_content_prompt
                        }
                    ]
                }
            ]
        )

        return response.content[0].text.strip()

if __name__ == "__main__":
    if not os.path.exists("ais"):
        os.makedirs("ais")

    with open("AIdocs/書籍生成AI.md", "r", encoding="utf-8", errors="ignore") as f:
        requirements = f.read()

    lecture_generator_prompt = requirements.split("## 📝 講義資料生成AI")[1].split("## 📝 問題生成AI")[0].strip()
    with open("ais/lecture_generator.md", "w", encoding="utf-8", errors="ignore") as f:
        f.write(lecture_generator_prompt)

    quiz_generator_prompt = requirements.split("## 📝 問題生成AI")[1].strip()
    with open("ais/quiz_generator.md", "w", encoding="utf-8", errors="ignore") as f:  
        f.write(quiz_generator_prompt)

    book_generator = BookGenerator("syllabus.yaml")
    book_generator.generate_book()
