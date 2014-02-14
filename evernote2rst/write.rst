=============
写一些Vim插件
=============

起源：\ `海波和王欣请我为PMO做Vim分享（培训） <evernote:///view/997589/s9/663ee65e-7d2a-4dd1-bbe7-9fe294aa947d/663ee65e-7d2a-4dd1-bbe7-9fe294aa947d/>`__

| 

需求：

#. 头文件，源码文件和单测文件之间的互相跳转 - Done
#. 百度（Google）风格的C++缩进，尤其是private的处理（是难点）- Done
#. 更多的代码补全（如blade）-
#. include的排序（参考：help sort）- Done
#. Blade与Vim的集成（参考：help write-compiler-plugin）- Done
#. FF的自动修正 - 延后
#. 自动生成单测Case框架
#. 自动在.cpp中生成函数框架
#. 快速打开帮助（Vim与man的集成）
#. 一键折叠所有代码

   -  延后。考虑到tagbar可以实现类似的功能，所以暂时不搞。

#. ctag/cscope/omini的代码补全的范围扩大到BLADE\_ROOT
#. 快速打开文件
#. 一键注释函数 - Done
#. BUILD文件的缩进（终于搞定了，原来是没加上"filetype plugin indent
   on”，伤不起啊！）

| 

**1. 三类文件间的跳转插件**

--------------

决定在a.vim基础上修改

| 

xxx.h xxx.cpp -> xxx\_test.cpp大体流程：

#. 获取base name；
#. 拼出xxx\_test.cpp；
#. 打开它；

目前已经能通过AUT指令在.h/.cpp和\_test.cpp之间跳转。

git@github.com:Windriver/a.vim.git 

| 

**2. 百度风格的C++缩进 - 2013-12-28 22:43:36**

--------------

换用QQ的indent/cpp.vim后，发现namespace的问题解决了，但是还有几个小问题：

#. for循环折行后的缩进。由于Baidu规范的规定是4空格缩进，for循环折行后，循环体与for语句搞到一起了。而google的是2空格缩进，所以google的for循环缩进很好看。
#. private加上:后可以自动与上一行保持缩进。但是我希望是像google一样半缩进

   -  配置setl cinoptions=g2，并在indent/cpp.vim的49行加上elseif l:pline
      =~# '^\\s\*\\(public\\:\\\|private\\:\\\|protected\\:\\).\*’      
      let l:retv -=
      2能部分解决，但是还有小bug（我决定先这样子了，等以后再完善）

#. 

总结：

indent/cpp.vim的主要功能是搞定namespace，template的缩进，以及跳过注释。cindent和cinoptions才是解决缩进问题的主力。

| 

**3. include的排序 - 2013-12-28 23:25:10**

--------------

 Done

| 

看起来很成功！

| 

**4. 去空行的插件 - 2013-12-29 15:12:19**

--------------

Done

| 

我写的函数的功能包括：

#. 删除多余空行；（无法去除文件尾部的双行，所以为了实现功能2，必须执行两次：silent!
   :.g/^$/d）
#. 删除文件末尾的空行；
#. 删除行尾空格；

| 

**5. Blade与vim的集成**

--------------

主要是blade对quickfix功能的支持情况。问了韩超，他说知道有，但是不知道具体那条指令。后来在Github上\ `blade的中文说明书上 <https://github.com/chen3feng/typhoon-blade/blob/master/doc/user_manual_zh_CN.md>`__\ 确认了blade确实支持quickfix，然后又在QQ的.vimrc中找到了set
local makeprg=blade的指令，然后好help makeprg，help
quickfix，终于搞定了这块。

| 

使用流程：

#. :set makeprg=blade
#. :make build
#. :cw "打开quickfix窗口
#. :cn :cp “下一个/上一个错误

| 

**6. Vim与man的集成**

--------------

| `looking up c++ documentation inside of
vim <http://stackoverflow.com/questions/2272759/looking-up-c-documentation-inside-of-vim/2337620#2337620>`__ 

| 

查找了N多安装C++ manpage的方法，都未果。决定先放弃。

| 

不甘心，再搜了下，终于在\ `这篇博客 <http://bzhao.xicp.net:9009/?p=243>`__\ 上找到了\ `C++
manpage的下载地址 <http://ftp.tsukuba.wide.ad.jp/software/gcc/libstdc++/doxygen/libstdc++-api.20131202.man.tar.bz2>`__\ 。在mac上解压，并把文件拷贝到/usr/share/man/man3/下面，终于可以用man
C++的。但是用法特别蛋疼，例如：

man 3 std::vector

man出来的页面也很不易读，感觉有还不如没有好。我想我以后可能会搞一个man系统。

| 

**7. 一键注释函数或者代码块**

--------------

随手写了一个：

| nmap <leader>cf viw$%,c<space><cr><c-o>  

第一次运行是注释，再次运行是解注释。

| 

这个函数还不完美，但是先这样，以后再改进（仍然是20%-80%策略）

| 

**8. 快速打开文件**

--------------

再次尝试了BufExplorer和lookupfile，两个都不错。后者的话，感觉反应慢，但是我按c-p，就会立刻弹出结果，应该是可以设置反应时间的。

| 

**9. 自动生成单测Case框架**

--------------

先写出正则：

| \\(class \\)\\@=.\*\\( : public\\)\\@<= 

| 

search参数：

'b'     search backward instead of forward 

'W'     don't wrap around the end of the file

'n'     do Not move the cursor 

| 

完成了GetUnittestClassName()函数，用到了search和matchlist。用起来很赞！

| 

|
