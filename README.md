# doublet

for linux terminal.

ダブレット(doublet)は、単語から単語までを一文字ずつ置き換えて、繋げるパズルです。
与えられた２つの単語を、それぞれ、＜ダブレット＞、途中の単語を＜リンク＞、ダブレットからダブレットまでを＜チェーン＞と言います。
単語さえあれば、ｎ文字違っている語への一文字置換の最短ステップは、ｎ回です。

始めの単語と最後の単語と《必要リンク数》が指定されるそうです。ルイス・キャロルが、ロンドンの女性向け週刊誌に連載したそうです。
「不思議の国の論理学」という本に掲載されています。

http://purple-jwl.hatenablog.com/entry/20130123/1358931139
にダブレットの解法のC++で書かれたお手本の最適なプログラムが公開されてます。
最短の必要リンク数で解けます。
それをアレンジして、Linux Terminalで、実用的にした、
C++とCの混交したプログラムを合成しました。
Cと、C++が混じったプログラムは、「better C」と言います。

辞書ファイルから、必要な単語を自動的に読み込んで、答えを返します。

普通、辞書ファイルは、膨大な数の単語があるので、実行時に、少し時間が掛かりますが、お茶でも飲んで待ってて下さい。
辞書のボキャブラリが大きかったら、答えを求めるまでの時間が飛躍的に長くなるので、なるべく、小さな辞書を使って下さい。
英辞郎は大きいです。ejdic-hand-utf-8.txtは小さくて、程々なので、お薦めです。
しかし、小さい辞書の場合、答えに辿り着けない場合があります。
答えにたどり着けなかった場合は、"Target can not be reached!"と、メッセージが出て、止まります。

debパッケージは、doubletバイナリからなり、deb系linux(amd64)で、実行できます。

僕の、GitHubリポジトリextwords中の、ewordsパッケージに依存します。


コンパイルの仕方：c++ doublet.cpp -o doublet

使い方例

$ doublet hate love

number of links : 2

hate

have

hove

love

$
