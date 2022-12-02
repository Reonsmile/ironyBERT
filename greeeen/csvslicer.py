# coding: UTF-8
# テキストファイルを、10行ずつ区切るだけのプログラム
# Created 2011.9.12 @amay077

import codecs

# 入力ファイルを開く
fin = codecs.open('greeeen.csv', 'r', 'utf-8')

# 一応初期化
count = 0
prevPage = -1

# １行ずつループ
for line in fin:
    # 整数÷整数だと切り捨てられるよ
    page = count / 10
    
    # 10行処理したら page が変わるから、そこで出力ファイルを変えるよ
    if page != prevPage:
        fout = codecs.open('page' + str(page + 1) + ".csv", 'w', 'utf-8')
    
    prevPage = page
    # ファイルに出力する
    fout.write(line)
    count = count + 1

# ファイルは python のガベージコレクタによって勝手に閉じられる（らしい）