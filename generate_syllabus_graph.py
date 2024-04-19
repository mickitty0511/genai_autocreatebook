# 必要なモジュールをインポート
import yaml
from graphviz import Digraph

# YAMLファイルを読み込み、シラバスデータを取得
with open('syllabus.yaml', 'r', encoding='utf-8') as file:
    syllabus = yaml.safe_load(file)

# Graphvizを使用してシラバスのグラフを作成
graph = Digraph(comment='Syllabus Graph', format='png')
graph.attr('graph', rankdir='TB', splines='ortho', newrank='true')

# 最大幅を計算するための変数を初期化
max_node_width = 0
max_subgraph_width = 0

# シラバスデータを元にノードを作成し、最大幅を計算
for month_data in syllabus['curriculum']:
    topics = ', '.join(month_data['topics'])
    if len(topics) > max_node_width:
        max_node_width = len(topics)
    lecture_titles = [lecture['title'] for lecture in month_data['lectures']]
    lecture_list = '\n'.join([f"・{title}" for title in lecture_titles])  # 講義タイトルの前に「・」を追加
    if len(lecture_list) > max_subgraph_width:
        max_subgraph_width = len(lecture_list)

# ノードの幅を最大幅に設定
node_width = str(max_node_width / 8)  # 幅の単位は適宜調整
subgraph_width = str(max_subgraph_width / 17)  # 幅の単位は適宜調整

# シラバスデータを元にノードとサブグラフを作成
for i, month_data in enumerate(syllabus['curriculum'], start=1):
    month = month_data['month']
    topics = ', '.join(month_data['topics'])
    month_node = f"Month {month}\n{topics}"
    graph.node(month_node, shape='box', style='filled', fillcolor='lightblue', fontname="MS UI Gothic", width=node_width)

    with graph.subgraph(name=f'cluster_month_{month}') as subgraph:
        subgraph.attr(style='filled', color='lightgrey', labeljust='l', height='0', width=subgraph_width)
        subgraph.node_attr.update(style='filled', color='white', height='2', width=subgraph_width)

        lecture_titles = [lecture['title'] for lecture in month_data['lectures']]
        # 左寄せ改行
        lecture_list = '\l'.join([f"・{title}" for title in lecture_titles])  # 講義タイトルの前に「・」を追加
        lecture_list = lecture_list + '\l'
        subgraph.node(f'Lectures_Month_{month}', shape='box', label=lecture_list, fontname="MS UI Gothic", width=subgraph_width)

    graph.edge(month_node, f'Lectures_Month_{month}', style='dashed', headport='n', tailport='s')

# 月ごとのノードを順に接続
with graph.subgraph() as s:
    s.attr(rank='same')
    for i in range(len(syllabus['curriculum']) - 1):
        current_month = syllabus['curriculum'][i]
        next_month = syllabus['curriculum'][i + 1]
        current_month_node = f"Month {current_month['month']}\n{', '.join(current_month['topics'])}"
        next_month_node = f"Month {next_month['month']}\n{', '.join(next_month['topics'])}"
        graph.edge(current_month_node, next_month_node)
        s.node(current_month_node)
        s.node(next_month_node)

# グラフをファイルに保存し、表示
graph.render('syllabus_graph', view=True)