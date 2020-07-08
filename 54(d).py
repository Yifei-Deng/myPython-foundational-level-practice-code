'''

python开发基础54-Python文件读取

'''

# 通过with关键字使用上下文管理器来直接操作文件，可以让上下文管理器帮助我们自动管理文件资源，不需要我们手动通过代码关闭文件对象
# 更为常用的方法

with open(r'/Users/Yifei/Desktop/py3/53~/file/The Zen of Python.txt') as f:
    for line in f:
        print(line,end='')


#不再需要 f.close()

'''
Outputs:

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
醜いより美しいほうがいい。
Explicit is better than implicit.
暗示するより明示するほうがいい。
Simple is better than complex.
複雑であるよりは平易であるほうがいい。
Complex is better than complicated.
それでも、込み入っているよりは複雑であるほうがまし。
Flat is better than nested.
ネストは浅いほうがいい。
Sparse is better than dense.
密集しているよりは隙間があるほうがいい。
Readability counts.
読みやすいことは善である。
Special cases aren't special enough to break the rules.
特殊であることはルールを破る理由にならない。
Although practicality beats purity.
しかし、実用性を求めると純粋さが失われることがある。
Errors should never pass silently.
エラーは隠すな、無視するな。
Unless explicitly silenced.
ただし、わざと隠されているのなら見逃せ。
In the face of ambiguity, refuse the temptation to guess.
曖昧なものに出逢ったら、その意味を適当に推測してはいけない。
There should be one-- and preferably only one --obvious way to do it.
何かいいやり方があるはずだ。誰が見ても明らかな、たったひとつのやり方が。
Although that way may not be obvious at first unless you're Dutch.
そのやり方は一目見ただけではわかりにくいかもしれない。オランダ人にだけわかりやすいなんてこともあるかもしれない。
Now is better than never.
ずっとやらないでいるよりは、今やれ。
Although never is often better than *right* now.
でも、今"すぐ"にやるよりはやらないほうがマシなことが多い。
If the implementation is hard to explain, it's a bad idea.
コードの内容を説明するのが難しいのなら、それは悪い実装である。
If the implementation is easy to explain, it may be a good idea.
コードの内容を容易に説明できるのなら、おそらくそれはよい実装である。
Namespaces are one honking great idea -- let's do more of those!
名前空間は優れたアイデアであるため、積極的に利用すべきである。




'''


