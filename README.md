# doublet

for linux terminal.

問題に、「How does 'GOD' become 'DOG'？」（どのようにして”GOD"が”DOG"になるか？）とか言うのがありました。文字列を逆順にすればいいだけのことです。一文字置換でやると、最も単純な変換は、「GOD DOD DOG」です。DODは「Department of Defense：国防総省」の事です。簡単な数学的置換では、「321」の置換です。
でも、やっぱり、猫が好きなので、DOGをCATに置換えます。「DOG COG COT CAT」です。COGは歯車、COTは小屋の事です。GODからCATの最短経路は、「GOD COD COT CAT」です。CODは鱈の事です。

＊当たり前のことですが、CATからGODに置き換えるには順序を逆に辿れば良いです。

＊単語さえあれば、ｎ文字違っている語への一文字置換の最短ステップは、ｎ回です。

一文字置換えのパズルは、正式には、ダブレット(doublet)と言い、与えられた単語を、それぞれ、＜ダブレット＞、途中の単語を＜リンク＞、ダブレットからダブレットまでを＜チェーン＞と言います。始めの単語と最後の単語と《必要リンク数》が指定されるそうです。ルイス・キャロルが、ロンドンの女性向け週刊誌に連載したそうです。「不思議の国の論理学」という本に掲載されています。

http://purple-jwl.hatenablog.com/entry/20130123/1358931139
にダブレットの解法のC++で書かれたお手本の最適なプログラムが公開されてます。
最短の必要リンク数で解けます。
それをアレンジして、Linux Terminalで、実用的にした、
C++とCの混交したプログラムを合成しました。
Cと、C++が混じったプログラムは、「better C」と言います。

辞書ファイルから、必要な単語を自動的に読み込んで、答えを返します。

普通、辞書ファイルは、膨大な数の単語があるので、実行時に、少し時間が掛かりますが、お茶でも飲んで待ってて下さい。辞書のボキャブラリが大きかったら、答えを求めるまでの時間が飛躍的に長くなるので、なるべく、小さな辞書を使って下さい。英辞郎は大きいです。ejdic-hand-utf-8.txtは小さくて、程々なので、お薦めです。しかし、小さい辞書の場合、答えに辿り着けない場合があります。答えにたどり着けなかった場合は、"Target can not be reached!"と、メッセージが出て、止まります。

コンパイルの仕方：c++ doublet.cpp -o doublet

使い方例：console から、「doublet hate love」とします。

出力例：

$ doublet hate love

number of links : 2

hate

have

hove

love

$
