# Pythonの基本文法

## 目次
1. [はじめに](#introduction)
2. [Pythonの基本構文](#basic-syntax)
3. [変数定義](#variable-declaration)
4. [条件分岐とループ](#control-flow)
5. [関数定義](#functions)
6. [クラスの定義](#classes)
7. [コーディングのベストプラクティス](#best-practices)
8. [練習問題](#exercises)
9. [用語集](#glossary)


<a id="introduction"></a>
## 1. はじめに

Pythonは、プログラミングを学ぶ人にとって非常に扱いやすい言語です。  
シンプルでわかりやすい文法を持っており、多くの便利な機能を提供するライブラリが豊富にあります。  
この講義では、Pythonの基本的な文法や、プログラムを書く際の基本的なルール、きれいなコードを書くためのコツなどを学んでいきます。  
Pythonの基本をしっかりと理解することで、プログラミングの基礎力をしっかりと身につけることができます。

<a id="basic-syntax"></a>
## 2. Pythonの基本構文

Pythonでプログラミングを始めるにあたって、まず知っておくべき基本的な構文がいくつかあります。

| 概念 | 説明 |
| --- | --- |
| **変数定義** | データを保存するための箱のようなものです。 |
| **基本演算子** | 数学の計算（足し算、引き算など）やデータの比較を行うための記号です。 |
| **条件分岐（if-elif-else）** | 「もし〜ならば、そうでなければ」という条件によって、プログラムの動きを変えることができます。 |
| **繰り返し処理（for, while）** | 同じ処理を繰り返し行うための構文です。 |
| **関数定義** | 特定の処理をまとめて名前をつけ、何度も使えるようにしたものです。 |
| **クラス定義** | データと処理をひとまとめにして扱うための構文です。 |

これらの基本構文を理解することで、Pythonでのプログラミングがスムーズになります。

<a id="variable-declaration"></a>
## 3. 変数定義

Pythonで変数を定義するときは、変数に名前を付けて値を代入します。  

```python
x = 10
name = "Alice"
is_student = True
```

変数名には以下のルールがあります。

- 英小文字、数字、アンダースコアを使用可
- 日本語は使用できますが、複数人でコードを管理する場合は日本語は使用しないこと
- 数字から始めることはできない
- 予約語（例えば`if`、`for`、`class`など、Pythonがすでに特定の目的で使っている単語）は変数名として使えません

<a id="control-flow"></a>
## 4. 条件分岐とループ

Pythonの制御構文には、if-elif-else文とfor文、while文があります。

```python
# if-elif-else
if x > 0:
    print("正の値")
elif x < 0:
    print("負の値")
else:
    print("ゼロ")

# for
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# while
count = 0
while count < 3:
    print(count)
    count += 1
```

条件式の評価結果によって処理を分岐させたり、繰り返し処理を行うことができます。

<a id="functions"></a>
## 5. 関数定義

Pythonでは以下のように関数を定義します。

```python
def greet(name):
    """
    名前を受け取って挨拶する関数
    """
    print(f"Hello, {name}!")

greet("Alice")  # 出力: Hello, Alice!
```

関数には以下のような特徴があります。

- `def`キーワードで定義
- 引数と返り値を持つことができる
- docstringで関数の説明を記述可能

関数を使うことで、コードの再利用性が高まります。

<a id="classes"></a>
## 6. クラスの定義

Pythonはオブジェクト指向プログラミングをサポートしており、クラスを定義することができます。

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

person = Person("Alice", 25)
person.introduce()  # 出力: Hello, my name is Alice and I'm 25 years old.
```

クラスには以下のような特徴があります。

- `class`キーワードで定義
- `__init__`メソッドでインスタンス変数の初期化
- メソッドでインスタンスの機能を定義

クラスを使うことで、オブジェクト指向のプログラミングが可能になります。

<a id="best-practices"></a>
## 7. コーディングのベストプラクティス

Pythonのコーディングにおいて、以下のようなベストプラクティスがあります。

- 変数名や関数名は意味のある名称を使う
- 4スペースのインデントを使う
- 短い関数を作る
- docstringを書く
- PEP 8のスタイルガイドラインに沿う

これらのルールを意識することで、可読性の高いきれいなコードを書くことができます。

<a id="exercises"></a>
## 8. 練習問題

### 問題1: 
2つの整数を受け取り、その和を返す関数を定義してください。

```python
def add_numbers(a, b):
    """
    2つの整数を受け取り、その和を返す関数
    """
    return a + b

result = add_numbers(3, 5)
print(result)  # 出力: 8
```

### 問題2:
人物クラスを定義し、名前と年齢を持つインスタンスを作成し、自己紹介をするメソッドを呼び出してください。

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

person = Person("Alice", 25)
person.introduce()  # 出力: Hello, my name is Alice and I'm 25 years old.
```

<a id="glossary"></a>
## 9. 用語集

| 用語 | 説明 |
| --- | --- |
| 変数 | これは、あなたがプログラムで使うデータを保存するための箱のようなものです。名前をつけて、後でその名前でデータを呼び出せます。 |
| 条件分岐 | 「もし〜だったら、これをする。そうでなければ、あれをする」というように、ある条件によってプログラムの動きを変えるための方法です。 |
| 繰り返し処理 | 同じ作業を何度も繰り返すときに使います。例えば、リストの中の各項目に対して同じ操作を行いたい場合などです。 |
| 関数 | ある特定の作業を行うためのコードのまとまりです。必要な情報を渡すと、それを使って何か作業をして、結果を返してくれます。 |
| クラス | プログラムの中で、データとそれを操作する機能を一緒にまとめたものです。これを使うと、現実世界の物事をプログラムの中で表現しやすくなります。 |
| コメント | コード内で実行されないテキストのことで、プログラムの説明やメモとして使用されます。Pythonでは `#` の後に続く行がコメントとして扱われます。 |
| docstring | 関数やクラスの最初に書く説明文です。これを書くことで、他の人がそのコードを読んだときに、何をするものなのかがすぐにわかります。 |
| PEP 8 | Pythonでプログラムを書くときのルールブックのようなものです。これに従うことで、他の人が読んでも理解しやすい、きれいなコードを書くことができます。 |

<a id="introduction"></a>
# Pythonの基本文法

## 目次
- [はじめに](#introduction)
- [4択問題](#multiple-choice-questions)
- [実践問題](#practice-problems)

## 4択問題 <a id="multiple-choice-questions"></a>

<details>
<summary>問題1: Pythonの変数命名規則で正しいものはどれですか?</summary>

- a. 変数名に空白を含める
- b. 変数名に数字から始める
- c. 変数名に予約語を使う
- d. 変数名は小文字のみ使う

<details>
<summary>回答と解説</summary>

回答: d. 変数名は小文字のみ使う

Pythonの変数命名規則では、変数名は小文字で始め、単語間はアンダースコア(_)で区切るのが一般的です。変数名に空白や数字から始める、予約語を使うのは避けるべきです。
</details>
</details>

<details>
<summary>問題2: Pythonのコメントアウトの方法はどれですか?</summary>

- a. // 
- b. #
- c. /*  */
- d. <!--  -->

<details>
<summary>回答と解説</summary>

回答: b. #

Pythonでコメントアウトする際は、行頭に `#` を付けます。C言語のように `//` や `/* */` は使用できません。HTMLのようなタグ `<!--  -->` も使えません。
</details>
</details>

<details>
<summary>問題3: 以下のコードの出力はどうなりますか?</summary>

```python
x = 5
y = 10
print(x + y * 2)
```

- a. 15
- b. 25 
- c. 35
- d. 45

<details>
<summary>回答と解説</summary>

回答: c. 35

このコードでは、まず `x = 5`, `y = 10` と変数に値が代入されます。
次に `print(x + y * 2)` が実行されますが、この際の計算順序は乗算が先に行われるため、`y * 2` が20となり、`x + 20` の結果35が出力されます。
</details>
</details>

<details>
<summary>問題4: Pythonの組み込み関数`print()`の使い方で正しいものはどれですか?</summary>

- a. `print(x, y, z, sep=',', end='\n')`
- b. `print(x y z, sep=',', end='\n')`
- c. `print(x, y, z, sep=' ', end='')`
- d. `print(x y z, sep=' ', end='')`

<details>
<summary>回答と解説</summary>

回答: a. `print(x, y, z, sep=',', end='\n')`

Pythonの`print()`関数では、引数として変数名を並べ、`sep`オプションで区切り文字を指定し、`end`オプションで改行文字を指定できます。
aの形式が正しい使い方で、bのように変数名の間に空白を入れるのは誤りです。
</details>
</details>

<details>
<summary>問題5: 以下のコードの出力はどうなりますか?</summary>

```python
def greet(name):