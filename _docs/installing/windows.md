---
title: Windows
category: ボットのインストール
order: 2
---

<img class="doc-img" src="{{ site.baseurl }}/images/windows.png" alt="Windows" style="width: 75px; float: right;"/>

Python 3.6の問題のため、[Python 3.5.4](https://www.python.org/ftp/python/3.5.4/python-3.5.4.exe)をインストールしてください。サポートは、Python 3.6を使用している場合、Python 3.5.4をインストールするように指示されることに限定されます。

MusicBot JPは、Windows 7,8、および10にもインストールできますが、コンピュータに最初にいくつかのプログラムをインストールする必要があります。

1. Python 3.5+をインストールします。最良の結果を得るには、[Python 3.5.4](https://www.python.org/ftp/python/3.5.4/python-3.5.4.exe)をインストールしてください。
2. セットアップ中に、プロンプトが表示されたら `すべてのユーザにランチャをインストールする（推奨）`と `PATHにPATHを追加する `にチェックを入れてください。
3. [Git for Windows](http://gitforwindows.org/)をインストールして下さい。
4. セットアップ中に `WindowsコマンドプロンプトからGitを使う`、 `Checkout Windows-style、Unixスタイルの終了をコミットする `、` MinTTYを使う(デフォルト端末MSYS2)`にチェックを入れてください。
5. Git Bashを開くには、フォルダ内の空のスペース(My Documentsなど)を右クリックし、「ここでBash Bash」をクリックします。
6. 開いたコマンドウィンドウで `git clone https://github.com/kosugikun/MusicBot.git MusicBot -b master`を実行してください。

> Gitを使ってボットをクローンしておらず、代わりにGitHubからZIPファイルをダウンロードして実行しようとすると、エラーが発生します。

その後、Git Bashを開いたフォルダに、 `MusicBot`というフォルダが表示されます。あなたのボットを[設定]({{site.baseurl}}/using/configuration)し、` update.bat`を実行してその後、 `run.bat`を実行してMusicBot JPを起動します。
