For two young women who had "nothing to do," Lewis Carroll invented a game called "doublets" and published it in a London women's magazine in 1879.

This game involves giving two words and replacing the letters of the given words one by one to arrive at another given word. The given words are called "doublets," the intermediate words are called "links," and the chain from one doublet to the other is called "chains." For example,

head,heal,teal,tell,tall,tail

The shorter the chain, the better. In the above example, the length of the chain is 4.

For more details, see the book "The Logic of Wonderland" (written by Lewis Carroll, edited and translated by Naoki Yanase).

There are detailed rules, but here we will assume that words can be freely selected from the dictionary file.

I slightly modified the code output by ChatGPT.

The dictionary file is specified by the variable "dictionary."

If you replace the dictionary file with a Japanese hiragana file, it will become compatible with Japanese. However, because Japanese has consonants, even if the number of characters matches, the beats may not match.

doublet.py is for English, doubletj.py is for Japanese.
