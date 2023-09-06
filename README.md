# group.assigner.beta
## About
人のグループへの割り当てを自動化するPythonプログラムです。

このプログラムでは、以下のことができます。

- Excelファイルに並べられた「番号」「一緒にグループになりたい３人の番号」「男女」の情報から、男女バランスを維持しつつ、可能な限り「一緒にグループになりたい」人を同じグループに割り当てます。

なお、このプログラムは制作途中のベータ版であり、今後機能を一般化・拡張していく可能性があります（というかそうしたいです）。

## 使い方
Windows10,11での使用を想定していますが、他の環境でもほぼ同様に機能するはずです。
### 1. Pythonのインストール
[こちら](https://www.python.jp/install/windows/install.html)の記事を参考にPythonをインストールしてください。
### 2. プログラムのダウンロード
コマンドプロンプト上で、以下のコマンドを実行してください。
```
cd desktop
mkdir group_assigner
cd group_assigner
curl -O https://raw.githubusercontent.com/kombumori/group.assigner.beta/main/main.py
curl -O https://raw.githubusercontent.com/kombumori/group.assigner.beta/main/requirements.txt
pip install -r requirements.txt
```
### 2. Excelファイルの準備
Excelの一番前にあるシートに

| (番号) | (一緒にグループになりたい番号1) | (一緒にグループになりたい番号2) | (一緒にグループになりたい番号3) | (性別) |
のように入力します。

**例:**

| 1 | 4 | 3 | 2 | 女 |
| 2 | 8 | 7 | 6 | 男 |
