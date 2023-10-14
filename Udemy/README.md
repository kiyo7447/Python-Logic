# 何処の情報をまとめたのか？

UdemyのPython講座を受講した時のメモをまとめたものです。
現役シリコンバレーエンジニアが教えるPython 3 入門 + 応用 +アメリカのシリコンバレー流コードスタイル
https://tmnets.udemy.com/course/python-beginner/learn/lecture/8509966?learning_path_id=4835268#overview

https://tmnets.udemy.com/course/python-beginner/learn/lecture/8393044?learning_path_id=4835268#overview

GitHub



# Pythonの文字化け調査
Visual Studio Code (VSCode)では、一部の設定を調整することで文字化け問題を解消できる場合があります。以下のステップを試してみてください。

1. **VSCodeの設定を開く**: "File" メニューから "Preferences" を選択し、その後 "Settings" をクリックします。または、`Ctrl + ,` を押すことで直接設定画面を開くことも可能です。

2. **検索バーに"terminal.integrated.env.windows"を入力する**: この設定項目は、VSCodeのターミナルで使用される環境変数を管理します。

3. **環境変数に新しい設定を追加する**: "Edit in settings.json" をクリックします。そうすると設定ファイルが開かれます。ここに次の行を追加します（すでに何かしらの設定がある場合は、その中に追加してください）:

    ```json
    "terminal.integrated.env.windows": {
        "PYTHONIOENCODING": "utf-8:surrogateescape"
    }
    ```

4. **VSCodeを再起動する**: 上記の設定を適用するために、VSCodeを再起動します。

上記の設定により、VSCodeの統合ターミナルでPythonが出力する文字列のエンコーディングがUTF-8に設定されます。これにより、日本語の文字化けが解消される可能性があります。

なお、VSCodeの統合ターミナルを使用していない場合、または上記の手順が問題を解決しない場合は、使用しているPythonの実行環境やコード、エラーメッセージなどの詳細情報が必要となります。


# VSCodeでの調査
Visual Studio Code（VSCode）でPythonのデバッグ実行を行うときに日本語が文字化けする問題は、VSCodeのPython拡張機能の設定を変更することで解消できる場合があります。

以下のステップを試してみてください：

1. **VSCodeの設定を開く**: "File" メニューから "Preferences" を選択し、その後 "Settings" をクリックします。または、`Ctrl + ,` を押すことで直接設定画面を開くことも可能です。

2. **検索バーに"Python"を入力し、Pythonの設定項目を見つける**: "Python"と入力すると、VSCodeのPython拡張機能に関連する設定項目が表示されます。

3. **"Python > Terminal: Execute In File Dir" の設定を有効にする**: この設定を有効にすると、VSCodeはPythonファイルがあるディレクトリでコードを実行します。これにより、VSCodeのPython拡張機能はUTF-8エンコーディングを正しく認識するようになる可能性があります。

4. **"Python > Terminal: Env"の設定を変更する**: ここで新しい環境変数を追加します。具体的には、「Edit in settings.json」をクリックして設定ファイルを開き、次の行を追加します:

    ```json
    "python.terminal.executeInFileDir": true,
    "python.env": {
        "PYTHONIOENCODING": "utf-8:surrogateescape"
    }
    ```

5. **VSCodeを再起動する**: 上記の設定を適用するために、VSCodeを再起動します。

以上の設定で、デバッグ時の日本語文字化け問題が解消されることを願っています。

なお、これでも解決しない場合は、具体的なエラーメッセージや使用しているPythonのコードなどの詳細情報が必要となります。それに基づいて、より具体的な解決策を提案することが可能です。


# コードスタイrのチェック
## ３つのコードスタイルチェッカー
1. pep8  
チェックはライト  
pip install pep8
1. flake8  
pip install flake8
1. pylint
チェックは厳しい  
pip install  
pylint

