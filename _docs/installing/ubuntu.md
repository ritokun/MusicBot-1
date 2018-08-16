---
title: Ubuntu
category: ボットのインストール
order: 1
---

<img class="doc-img" src="{{ site.baseurl }}/images/ubuntu.png" alt="Ubuntu" style="width: 75px; float: right;"/>

Installing MusicBot on Ubuntu via the command line is the **recommended way to install the bot**, though the system dependencies differ depending on what version of Ubuntu you are using. Firstly, lets install the dependencies required for your system:

## Ubuntu 14.04
~~~ bash
# ビルドツールをインストール
sudo apt-get install build-essential unzip -y
sudo apt-get install software-properties-common -y

# 外部ポジトリを追加する
sudo add-apt-repository ppa:deadsnakes -y
sudo add-apt-repository ppa:mc3man/trusty-media -y
sudo add-apt-repository ppa:chris-lea/libsodium -y

# システムの依存関係をインストール
sudo apt-get update -y
sudo apt-get install git python python3.5-dev libav-tools libopus-dev libffi-dev libsodium-dev python3-pip -y
sudo apt-get upgrade -y

# MusicBotを入れたいディテクトリの中に、MusicBotをクローン
git clone https://github.com/kosugikun/MusicBot.git ~/MusicBot -b master
cd ~/MusicBot

# Pythonの依存関係をインストール
sudo python3.5 -m pip install -U pip
sudo python3.5 -m pip install -U -r requirements.txt 
~~~

## Ubuntu 16.04
~~~ bash
# ビルドツールをインストール
sudo apt-get install build-essential unzip -y
sudo apt-get install software-properties-common -y

# 外部リポジトリを追加
sudo add-apt-repository ppa:mc3man/xerus-media -y

# システムの依存関係をインストールする
sudo apt-get update -y
sudo apt-get install git ffmpeg libopus-dev libffi-dev libsodium-dev python3-pip python3-dev -y
sudo apt-get upgrade -y

# MusicBotを入れたいディテクトリの中に、MusicBotをクローン
git clone https://github.com/Just-Some-Bots/MusicBot.git ~/MusicBot -b master
cd ~/MusicBot

# Pythonの依存関係をインストール
sudo python3 -m pip install -U pip
sudo python3 -m pip install -U -r requirements.txt 
~~~

上記の手順をした後、MusicBotのフォルを開き、Tokenなどを設定した後に、
MusicBotのフォルダの端末を開き./run.shを実行すれば、起動できます
