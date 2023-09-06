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

|A列|B列|C列|D列|E列|
|:---|:---|:---|:---|:---|
| (番号) | (一緒にグループになりたい番号1) | (一緒にグループになりたい番号2) | (一緒にグループになりたい番号3) | (性別) |

のように入力します。

**例:**
|A列|B列|C列|D列|E列|
|:---|:---|:---|:---|:---|
| 1 | 4 | 3 | 2 | 女 |
| 2 | 8 | 7 | 6 | 男 |
| ︙ | ︙ | ︙ | ︙ | ︙ |

そして、保存します。「**2. プログラムのダウンロード**」でデスクトップに作成した「group_assigner」フォルダに保存すると、後々楽かもしれません。

### 3. グループの自動割り当て
では、コマンドプロンプト上で以下のコマンドを実行しましょう。
```
cd desktop
cd group_assigner
python3 main.py -f (Excelファイルのパス) -r (改善回数) -g (作成するグループ数) -rng (使用するExcel上の範囲)
```
`-f`オプションにおいては、Excelファイルとmain.pyが同じフォルダに保存してある場合、フルパスではなくファイル名だけで指定することもできます（その他相対パスも使用可）

`-r`の目安は50,100あたりです。300程度を指定し、他の作業をしながら気長に待つ(最長２時間ぐらいで変化がなくなります）こともできます。

`-rng`は`A1:E35`のように指定してください。

完了すると`### FINISHED ###`と表示され、完成したグループが表示されます。しかし実行途中にもその段階のグループも表示されるため、満足なグループが完成したらその時点で止めてしまっても構いません。

なお、作業途中に表示されているグループの見方は
```
[[[ (名簿), (一緒になりたい人1), (一緒になりたい人1), (一緒になりたい人1), (性別) ],
  [ (名簿), (一緒になりたい人1), (一緒になりたい人1), (一緒になりたい人1), (性別) ],
  [ (名簿), (一緒になりたい人1), (一緒になりたい人1), (一緒になりたい人1), (性別) ],
  [ (名簿), (一緒になりたい人1), (一緒になりたい人1), (一緒になりたい人1), (性別) ]],
 [[ (名簿), (一緒になりたい人1), (一緒になりたい人1), (一緒になりたい人1), (性別) ],
  [ (名簿), (一緒になりたい人1), (一緒になりたい人1), (一緒になりたい人1), (性別) ],
  [ (名簿), (一緒になりたい人1), (一緒になりたい人1), (一緒になりたい人1), (性別) ],
  [ (名簿), (一緒になりたい人1), (一緒になりたい人1), (一緒になりたい人1), (性別) ]],
 [[...
```
のようになっており、外から2番目のカッコで囲まれた部分が1グループになります。

また、グループの上には数字が２つ表示されています。２つ目の数字が直下のグループにおいて叶えられた希望数になります。
