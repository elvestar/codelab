=============================================================
Github + Markdown/reStructedText + Jekyll/Pelican打造个人博客
=============================================================

**参考文章**

| 

Pelican路线：

`http://www.lizherui.com/pages/2013/08/17/build\_blog.html <http://www.lizherui.com/pages/2013/08/17/build_blog.html>`__

| 

Jekyll路线：

`http://www.ruanyifeng.com/blog/2012/08/blogging\_with\_jekyll.html <http://www.ruanyifeng.com/blog/2012/08/blogging_with_jekyll.html>`__

`http://www.yangzhiping.com/tech/writing-space.html <http://www.yangzhiping.com/tech/writing-space.html>`__

`http://www.yangzhiping.com/tech/r-markdown-knitr.html <http://www.yangzhiping.com/tech/r-markdown-knitr.html>`__

`http://www.yangzhiping.com/tech/wordpress-to-jekyll.html <http://www.yangzhiping.com/tech/wordpress-to-jekyll.html>`__

| 

**Pelican之旅**

--------------

**Pelican介绍**

`http://docs.getpelican.com/en/3.2/ <http://docs.getpelican.com/en/3.1.1/>`__

| 

（发现ping不通papi.python.org，github也上不去，所以先暂停搞）

| 

**安装**\ ：

sudo pip install pelican

sudo pip install markdown（apt-get安装的markdown不管用貌似）

| 

**使用**\ ：

+--------------------------------------------------------------------------+
| mkdir blog && cd blog                                                    |
| pelican-quickstart（复杂的配置过程...）                                  |
| vi  content/my-first-blog.md                                             |
| make publish                                                             |
| make server（自检）                                                      |
| git clone git@github.com:Windriver/windriver.github.io.git               |
| cd  windriver.github.io.git                                              |
| cp ../output/\* . -r                                                     |
| git commit -a -m "xxx"                                                   |
| git push                                                                 |
+--------------------------------------------------------------------------+

| 

| 

**安装pelican-themes**\ ：

cd ..

git clone
`https://github.com/getpelican/pelican-themes.git <https://github.com/getpelican/pelican-themes.git>`__

cd  pelican-themes/

sudo pelican-themes -i bootstrap2（试一下boostraps2主题）

修改pelicanconf.py，加入THEME = 'bootstrap2'

发布到github；

| 

**加入GoogleAnalytics**\ ：

登录\ `GoogleAnalytics <http://www.google.com/analytics>`__\ ，注册获得一个“跟踪
ID”；

修改pelicanconf.py，加入GOOGLE\_ANALYTICS = 'UA-44200537-1'；

发布到github；

| 

| 

**Jekyll之旅** - 2013-9-21 0:24:27

--------------

发现用起来并不如想象中那样方便，于是停止尝试，先专心搞pelican。

| 

| 

**使用第三方评论系统：友言** - 2013-9-22 23:55:53

--------------

`http://www.uyan.cc/ <http://www.uyan.cc/>`__  

| 

| 在某篇文章的<article>后面加上这块代码，就可以使用友言的服务了

+----------------------------------------------------------------------------------------------+
| <!-- UY BEGIN -->                                                                            |
|  <div id="uyan\_frame"></div>                                                                |
|  <script type="text/javascript" src="http://v2.uyan.cc/code/uyan.js?uid=1843826"></script>   |
|  <!-- UY END -->                                                                             |
+----------------------------------------------------------------------------------------------+

| 

效果如下：

|image0|

| 

下一步，我会修改pelican的源码，使其能在网页后面自动缀上这段代码。

| 

尝试了N久，终于搞定了。原来是在theme里面做的。

| 

我先修改了bootstrap2的bootstrap2/templates/article.html，加上：

+--------------------------------------------------------------------------+
|   22                  {% if **UYAN\_UID** and SITEURL and article.status |
| != "draft" %}                                                            |
|   23                                                                     |
|                                                                          |
|   24                                                                     |
|                                                                          |
|   25                                                                     |
|   26                                                                     |
|                                                                          |
|   27                  {% endif %}                                        |
| |image2|                                                                 |
+--------------------------------------------------------------------------+

| 

然后重装bootstrap2主题：

          sudo pelican-themes **-r** bootstrap2

          sudo  pelican-themes **-i** bootstrap2

然后make publish，就OK了。

| 

从这里，可以看出，如果我自己需要定制一个theme的话，也要修改templates下面的各种.html。

| 

| 

**博客的图片管理** - 2013-9-23 1:32:24

--------------

https://lh5.googleusercontent.com/vBF-iWApPvDU7FMEr-eKzZHE8pnOfaNskczdPzYtxic=w640-h426-no

| 

| 

**与Evernote互通**  - 2013-9-25 1:02:11

--------------

先注册Evernote的API key：

+--------------------------------------------------------------------------+
|   Your Evernote API Key                                                  |
| | *API access details for your records:*                                 |
| | Consumer Key:            ``windriver``                                 |
| | Consumer Secret:  ``4660f40068a33444``                                 |
| | Note:  This info will also be emailed to you shortly                   |
+--------------------------------------------------------------------------+

| 

貌似上面的key不是正式的，只能访问sandbox，要想访问线上的服务器，要经过\ `**Key
Activation** <http://dev.evernote.com/support/glossary.php#k>`__\ 的过程。

| 

不管了，搞先。先安装python sdk：

sudo pip install evernote

| 

研究了下\ `Evernote的API <http://dev.yinxiang.com/documentation/>`__\ ，发现分为两组：本地API和云API。本地API只能访问Evernode在本地的文件，显然，这不是我想要的，而且很不方便。至于云API，我发现它有两种认证方式：

#. OAuth认证；
#. 开发者Token；

开发者Token就是我想要的东西！于是我申请了一下：

+-------------------------------------------------------------------------------------------------------+
| Developer Token:                                                                                      |
| S=s9:U=f38d5:E=148a8cf4838:C=141511e1c3a:P=1cd:A=en-devtoken:V=2:H=06d5f3f2d0f723c0160290955387d55a   |
| NoteStore URL:                                                                                        |
| https://app.yinxiang.com/shard/s9/notestore                                                           |
| Expires:                                                                                              |
| 24 September 2014, 17:57                                                                              |
+-------------------------------------------------------------------------------------------------------+

| 

昨晚搞了N小时，没搞定。今晚仔细研究了出错的原因，参考了\ `论坛的帖子 <http://discussion.evernote.com/topic/39624-getnotestoreurl-is-not-work/>`__\ ，终于解决了问题。顺带了解了Thrift的用法和UserSotre/NoteStore的概念。

| 

| 

| 

| 

**Markdown VS. reStructedText** -   2013-9-21 2:24:55

--------------

感觉用Markdown写出的东西，虽然很简洁，但是层次不分明，当内容多了以后，会感觉版面很乱。

| 

研究pelican时，觉得它的\ `官方文档 <http://docs.getpelican.com/en/3.2/>`__\ 的板式就很好，我猜测是用RST生成的。结果一番调查，终于确定它就是用RST写的。于是我也决定改变方向，暂停使用Markdown，换用RST！

| 

使用RST写完并上传以后，感觉不错，这是我近期的大突破。我相信，\ **Github**
+ **reStructedText** + **Pelican**\ 这套工具就是我想要的东西！

| 

**RST参考文章**\ ：

`Sphinx与reStructedText的学习 <evernote:///view/997589/s9/511829c3-8044-4446-b2b6-2e42a75718fa/511829c3-8044-4446-b2b6-2e42a75718fa/>`__

`***re***\ **Structured\ :sup:`Text`  **\ **简明教程** <http://blog.csdn.net/jiyucn/article/details/2157189>`__

`reStructuredText简明教程 <http://jwch.sdut.edu.cn/book/rst.html#id2>`__

`Python官方文档 <http://docs.python.org/2/>`__\ （RST使用的典范）

| 

**在线编辑器**\ ：

`http://rst.ninjs.org/ <http://rst.ninjs.org/>`__

| 

| 

**RST语法总结**  - 2013-9-22 1:36:12

--------------

**划分段落**\ （文章的提纲）

| 

.. toctree::

    :maxdepth: 2

| 

**段落修饰**\ （如列表和引用）

.. tip::

.. seealso::  

.. warning::

| 

**文本修饰**\ （也可以叫行内标记）：加粗，斜体，超链接

| 

**复杂元素**\ ：表格，图片，代码，公式

插入代码：

::   （简单代码）

.. code-block:: c++

| 

插入图片

.. image:: ../../../image/kechengbiao.png
                                                            

    :width: 320
                                                                                      

    :height: 480   

| 

**锚定**\ ：包括段落间锚定，文档间锚定。

| 

| 

http://192.168.1.112:8000/posts/2010/image/kechengbiao.png

| 

  

| 

| 

.. |image0| image:: Github%20+%20Markdown_reStructedText%20+%20Jekyll_Pelican%E6%89%93%E9%80%A0%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2.resources/f6d6f35ca1e0c9c3646286aa994c3fc3.png
.. |image1| image:: Github%20+%20Markdown_reStructedText%20+%20Jekyll_Pelican%E6%89%93%E9%80%A0%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2.resources/3ee7f8d30175e351429d9fd9c967a5d4.png
.. |image2| image:: Github%20+%20Markdown_reStructedText%20+%20Jekyll_Pelican%E6%89%93%E9%80%A0%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2.resources/3ee7f8d30175e351429d9fd9c967a5d4.png
