=================
VIM插件的编程语言
=================

let：用来定义变量，每次赋值等操作都会用到let

| 

.：用来连接字符串

| 

line(".")用来取得当前的行数，col(".")用来取得当前的列数

line("$")用来

getline(line\_no)用来取得第line\_no行的内容

| 

startinsert用来把vim切换到insert模式

| 

**exec** "normal! a\\t\\t   /\*\*<         \*/"           该语句的要点：

#. exec -
   后面跟着字符串，能执行一定的功能。而相对的说，call是直接调用后面的函数（\ **但是exec也可以呀**\ ）；
#. normal! - ？
#. a - 表示插入后面的字符（在回车之前插入）。

<SID>：这个这个标签常用在**函数调用或定义**\ 之前，它干吗用的？

| 

apend(line\_no, str) -
该函数用来在line\_no行加入str字符串。append每次执行就会自动添加一个换行符，而通过在str中加入"\\n"来换行的方式则不可行（\ **也可能是我的方法不对**\ ）。\ |image0|

| 

if后面要对应着endif

function后面要对应着endfunction

| 

经常出现a:leading\_blank这样的形式，我发现  \ **a:后面跟的遍历经常是函数的形参**\ ！

我又发现了以 l:
开头的参数形式，难道它是\ [STRIKEOUT:全局变量或是环境变量]\ ？如synopsisCol和synopsisLine

| 

**我的学习成果包括一个函数，此外还有一些对comgd.vim文件作出的针对我的需求的修改
- 2012-4-29 23:49:31**

--------------

       |image1|

| 

**关于map - 2012-5-4 16:42:32**

--------------

map <F2> : call xxxx的意思是按F2时调用该函数，

而imap<F8> EXPECT\_EQ 则表示按下F8就会插入EXPECT\_EQ。

`http://hi.baidu.com/%BB%EC%BF%DA%B7%B9%B5%C4%BE%DB%B1%A6%C5%E8/blog/item/98867808d4ed78d563d98678.html <http://hi.baidu.com/%BB%EC%BF%DA%B7%B9%B5%C4%BE%DB%B1%A6%C5%E8/blog/item/98867808d4ed78d563d98678.html>`__

| 

| 

.. |image0| image:: VIM%E6%8F%92%E4%BB%B6%E7%9A%84%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80.resources/ef90eea547d24f8a39f885277aca8d23.png
.. |image1| image:: VIM%E6%8F%92%E4%BB%B6%E7%9A%84%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80.resources/bda75720af107cda5143604aab7c65d5.png
