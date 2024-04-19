# Webアプリ開発

## 目次

1. [はじめに](#introduction)
2. [Webアプリの概要](#web-app-overview)
3. [Webアプリ開発の流れ](#web-app-development)
4. [フロントエンド開発](#frontend-development)
5. [バックエンド開発](#backend-development)
6. [例題と演習](#examples-and-exercises)
7. [用語集](#glossary)
8. [4択問題](#multiple-choice)

<a id="introduction"></a>
## はじめに

この講義では、簡単なWebアプリの開発方法について学習します。  
Webアプリとは、インターネットを通じてブラウザ上で動作するプログラムのことです。  
ここでは、Webアプリの基本的な構造や、開発に使うツール、プログラミング言語の基本的な使い方などを理解します。  
実際にWebアプリを作成することで、Webアプリ開発の実践的なスキルを身につけることが目的です。

<a id="web-app-overview"></a>
## Webアプリの概要

Webアプリとは、Webブラウザ上で動作するアプリケーションのことです。  
従来のデスクトップアプリとは異なり、Webアプリはインターネットを通じて提供されるため、ユーザーはインターネットに接続さえすれば、どこからでもアクセスできるという特徴があります。  
Webアプリの主な特徴としては、

- ブラウザ上で動作するため、インストールや設定が不要
- デバイスやOSに依存せず、どの環境からでもアクセス可能
- サーバー側で処理を行うため、クライアント側の負荷が軽い
- 更新がすぐに反映されるため、常に最新の状態を利用できる

などが挙げられます。  
これらの特徴により、Webアプリは非常に便利で、多くの人々に利用されています。

<a id="web-app-development"></a>
## Webアプリ開発の流れ

Webアプリを開発する際の主な流れは以下のようになります。

| ステップ | 説明 |
|----------|------|
| 要件定義 | まず、作りたいWebアプリがどんな目的を持ち、どんな機能が必要か、誰が使うのか、どんな見た目にするのかを考えます。<br/>これは、プロジェクトの「設計図」を作るようなもので、何を作るかを決める大切な最初のステップです。<br/> |
| フロントエンド開発 | 次に、HTML（ウェブページの骨組みを作る言語）、CSS（ウェブページの見た目を整える言語）、JavaScript（ウェブページに動きをつけるプログラミング言語）を使って、ウェブページを作ります。<br/>これは、ユーザーが直接見て触れる部分、つまりWebアプリの「顔」を作る作業です。<br/> |
| バックエンド開発 | ここでは、ユーザーから見えない部分であるサーバーサイドの処理を行います。<br/>データベースとの連携やAPI（アプリケーションプログラミングインターフェース）の開発など、Webアプリの機能を支える「裏側」の仕事をします。<br/> |
| 統合 | フロントエンドとバックエンドをつなぎ合わせて、Webアプリ全体を完成させます。<br/>これにより、見た目だけでなく機能も備えた、実際に使えるアプリができあがります。<br/> |
| テスト | 作ったWebアプリが正しく動くか、バグ（エラー）がないかをチェックします。<br/>これは、ユーザーにとって快適に使えるかどうかを確認する重要な作業です。<br/> |
| デプロイ | 最後に、Webアプリをサーバーにアップロードして、インターネット上で公開します。<br/>これにより、世界中の人がアプリを使えるようになります。<br/> |

これらの工程を踏まえながら、効果的にWebアプリを開発していきます。

<a id="frontend-development"></a>
## フロントエンド開発

Webアプリのフロントエンド（クライアントサイド）の開発では、主にHTML、CSS、JavaScriptを使用します。

| 技術 | 説明 |
|------|------|
| HTML | Webページの構造を定義する。<br/>これは、Webページの骨組みを作るための言語です。<br/>簡単に言うと、Webページの基本的な形やセクションを決めるために使います。<br/>例えば、見出しや段落、リストなど、ページ上でどこに何を表示するかを決めることができます。<br/> |
| CSS | Webページの見た目（レイアウト、色、フォントなど）を設定する。<br/>これは、Webページをきれいに見せるための言語です。<br/>HTMLで作った骨組みに、色や大きさ、位置などのスタイルを加えて、見た目を整える役割を持っています。<br/>例えば、文字の色を変えたり、画像を並べたりすることができます。<br/> |
| JavaScript | ユーザーとの対話性や動的な機能を実現する。<br/>これは、Webページに動きをつけるためのプログラミング言語です。<br/>例えば、ボタンをクリックしたときに何かが起こるようにしたり、データをリアルタイムで更新したりすることができます。<br/>Webページをただ表示するだけでなく、ユーザーが操作できるようにするために重要な言語です。<br/> |

これらの技術を組み合わせることで、ユーザーにとって使いやすく、魅力的なWebアプリを構築できます。

<a id="backend-development"></a>
## バックエンド開発

Webアプリのバックエンド（サーバーサイド）の開発では、主にサーバーサイドのプログラミング言語を使用します。代表的な言語には以下のようなものがあります。

| 言語 | 説明 |
|------|------|
| PHP | ウェブサイトを作るのに適した、初心者にも扱いやすいオープンソースのプログラミング言語です。<br/>オープンソースとは、誰でも自由に使える、改良できるという意味です。<br/>PHPは、簡単なウェブサイトから複雑なウェブアプリケーションまで、幅広く使われています。<br/> |
| Python | 初心者にも理解しやすいシンプルな文法を持つプログラミング言語で、ウェブ開発だけでなく、データ分析や機械学習など、多岐にわたる分野で使われています。<br/>Pythonには、開発を助けてくれる様々なフレームワーク（あらかじめ用意された便利な機能の集まり）があり、これが多くのプログラマーに愛される理由の一つです。<br/> |
| Ruby | ウェブアプリケーションの開発に適した、シンプルで直感的に理解しやすい文法を持つプログラミング言語です。<br/>Rubyは特に「Ruby on Rails」というフレームワークと組み合わせて使われることが多く、迅速な開発が可能です。<br/>書きやすさと理解しやすさから、初心者にもおすすめの言語です。<br/> |

<a id="examples-and-exercises"></a>
## 例題と演習

### 例題1: 簡単なToDoリストアプリの作成

ToDoリストアプリを作成する際のフロントエンド開発の例として、以下のようなHTML/CSS/JavaScriptのコードを使用できます。

```html
<!-- HTML -->
<div id="todo-app">
  <h1>ToDoリスト</h1>
  <input type="text" id="todo-input" placeholder="ToDoを入力">
  <button id="add-button">追加</button>
  <ul id="todo-list"></ul>
</div>
```

```css
/* CSS */
#todo-app {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f4f4f4;
  border-radius: 5px;
}

#todo-list {
  list-style-type: none;
  padding: 0;
}

#todo-list li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  border-bottom: 1px solid #ddd;
}
```

```javascript
// JavaScript
document.addEventListener('DOMContentLoaded', function() {
  const todoInput = document.getElementById('todo-input');
  const addButton = document.getElementById('add-button');
  const todoList = document.getElementById('todo-list');

  addButton.addEventListener('click', function() {
    const todoText = todoInput.value.trim();
    if (todoText !== '') {
      const todoItem = document.createElement('li');
      const todoLabel = document.createElement('span');
      todoLabel.textContent = todoText;
      const deleteButton = document.createElement('button');
      deleteButton.textContent = '削除';
      deleteButton.addEventListener('click', function() {
        todoItem.remove();
      });
      todoItem.appendChild(todoLabel);
      todoItem.appendChild(deleteButton);
      todoList.appendChild(todoItem);
      todoInput.value = '';
    }
  });
});
```

この例では、HTMLでToDoリストのUI要素を定義し、CSSでスタイリングを行っています。  
JavaScriptでは、ToDoの追加と削除の機能を実装しています。

### 演習1: ToDoリストアプリにカテゴリ機能を追加する

ToDoリストアプリにカテゴリ機能を追加してみましょう。  
カテゴリを選択できるドロップダウンメニューを追加し、  
ToDoアイテムにカテゴリを紐付けられるようにします。

<a id="glossary"></a>
## 用語集

| 用語 | 説明 |
| --- | --- |
| Webアプリ | インターネットを使ってアクセスすることができるアプリケーションのことです。<br/>例えば、オンラインショッピングサイトやSNSなどがこれにあたります。 |
| フロントエンド | ユーザーが直接触れる部分、つまりウェブサイトの見た目や操作する部分を作ることを担当します。<br/> |
| バックエンド | ユーザーから見えない部分で、データの保存やサーバーの管理など、ウェブサイトを動かすための裏側の処理を担当します。<br/> |
| HTML | Webページの骨組みを作るための言語です。<br/>文章や画像をどこにどう表示するかを定義します。<br/> |
| CSS | HTMLで作られたWebページのデザインを決める言語です。<br/>色やフォント、レイアウトなど、見た目に関する設定を行います。<br/> |
| JavaScript | Webページに動きをつけるためのプログラミング言語です。<br/>例えば、ボタンをクリックしたときに何かが起こるような機能を作ることができます。<br/> |
| PHP | サーバーで動くプログラムを作るための言語です。<br/>Webサイトのデータを管理したり、ユーザーからの入力を処理するのに使われます。<br/> |
| Python | 初心者にも読みやすいとされるプログラミング言語で、Webアプリ開発だけでなく、データ分析や機械学習など幅広い分野で使われています。<br/> |

<a id="multiple-choice"></a>
## 4択問題

<details>
<summary>問題1: Webページの骨組みを作るために使用される言語はどれですか？</summary>

- a. CSS
- b. JavaScript
- c. HTML
- d. PHP

<details>
<summary>回答と解説</summary>

回答: c. HTML

HTMLは、Webページの基本的な構造やセクションを定義するために使用されます。これにより、見出し、段落、リストなど、ページ上でのコンテンツの配置を決定します。
</details>
</details>

<details>
<summary>問題2: Webアプリの見た目（レイアウト、色、フォントなど）を設定するために使用される言語はどれですか？</summary>

- a. CSS
- b. HTML
- c. JavaScript
- d. Ruby

<details>
<summary>回答と解説</summary>

回答: a. CSS

CSSは、Webページを視覚的に装飾するために使用される言語です。HTMLで作成された骨組みにスタイルを適用し、色、フォント、レイアウトなどの見た目を整えます。
</details>
</details>

<details>
<summary>問題3: Webページに動きをつけるためのプログラミング言語はどれですか？</summary>

- a. CSS
- b. HTML
- c. PHP
- d. JavaScript

<details>
<summary>回答と解説</summary>

回答: d. JavaScript

JavaScriptは、Webページに対話性や動的な機能を追加するために使用されるプログラミング言語です。例えば、ボタンのクリックに応じて何かが起こるような機能を実装することができます。
</details>
</details>

<details>
<summary>問題4: サーバーで動くプログラムを作るために使用される言語はどれですか？</summary>

- a. CSS
- b. JavaScript
- c. PHP
- d. HTML

<details>
<summary>回答と解説</summary>

回答: c. PHP

PHPは、サーバーサイドで動作するプログラムを作成するために使用される言語です。Webサイトのデータを管理したり、ユーザーからの入力を処理するのに適しています。
</details>
</details>