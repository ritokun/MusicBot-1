---
title: Raspbian
category: ボットのインストール
order: 4
---

<img class="doc-img" src="{{ site.baseurl }}/images/raspbian.png" alt="Raspbian" style="width: 75px; float: right;"/>

RaspbianにMusicBot JPをインストールするのには時間がかかることがあります。それでも使ってみたい！という方は、下記の手順をしてインストールしてください:

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
git clone https://github.com/kosugikun/MusicBot.git MusicBot -b master
cd MusicBot
sudo python3 -m pip install --upgrade -r requirements.txt
```

上記の手順をした後、`MusicBot`フォルダを開き、`Token`などを設定した後に、
`MusicBotフォルダ`の端末を開き`./run.sh`を実行すれば、起動できます。
