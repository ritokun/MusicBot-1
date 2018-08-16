---
title: Raspbian
category: ボットのインストール
order: 4
---

<img class="doc-img" src="{{ site.baseurl }}/images/raspbian.png" alt="Raspbian" style="width: 75px; float: right;"/>

RaspbianにMusicBotをインストールするのには時間がかかることがあります。それでも使ってみたい！という方は、下記の手順をしてインストールしてください:

```bash
# システムパッケージを更新する
sudo apt-get update -y
sudo apt-get upgrade -y

# 依存関係のインストール
sudo apt install python3-pip
sudo apt install git
sudo apt install libopus-dev
sudo apt install ffmpeg

# MusicBot JPをクローン(ディテクトリは変えてもいいです)
cd ~
git clone https://github.com/Just-Some-Bots/MusicBot.git MusicBot -b master
cd MusicBot
sudo python3 -m pip install --upgrade -r requirements.txt
```

上記の手順をした後、MusicBotのフォルを開き、Tokenなどを設定した後に、
MusicBotのフォルダの端末を開き./run.shを実行すれば、起動できます。
