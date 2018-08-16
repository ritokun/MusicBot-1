---
title: MacOS
category: ボットのインストール
order: 3
---

<img class="doc-img" src="{{ site.baseurl }}/images/mac.png" alt="Mac" style="width: 75px; float: right;"/>

MacにMusicBot JPをインストールするには、いくつかのライブラリとアプリケーションが必要です。最初に、あなたのシステムにPython 3.5+をインストールしてください。最良の結果を得るには、Python 3.5.4をインストールします（インストールするpkgファイルをダブルクリックしてください）。次に、ターミナルを開いて次のコマンドを実行する必要があります：

```bash
# Install Homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew update
xcode-select --install

# Install dependencies
brew install git
brew install ffmpeg
brew install opus
brew install libffi
brew install libsodium

# Clone the MusicBot
cd desktop
git clone https://github.com/Just-Some-Bots/MusicBot.git MusicBot -b master 

# Install Python dependencies
cd MusicBot
python3 -m pip install -U pip
python3 -m pip install -U -r requirements.txt
```

After this, you can find a folder called `MusicBot` on your Desktop. You can then open it, [configure]({{ site.baseurl }}/using/configuration) your bot, and then run the bot by double-clicking the `run.sh` file. If you can't run this, you may have to open Terminal, cd to the folder, and use `chmod +x run.sh` to give the file executable permissions.
