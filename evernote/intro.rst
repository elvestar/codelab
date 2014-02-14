

+ `Home`_
+ `Get it`_
+ `Docs`_
+ `Extend/Develop`_

` `_


Navigation
~~~~~~~~~~


+ `index`_
+ `modules`_ |
+ `next`_ |
+ `previous`_ |
+ `Sphinx home`_|
+ `Documentation`_




`Table Of Contents`_
~~~~~~~~~~~~~~~~~~~~


+ Introduction

    + Conversion from other systems
    + Use with other systems
    + Prerequisites
    + Usage





Previous topic
``````````````

`Sphinx documentation contents`_



Next topic
``````````

`First Steps with Sphinx`_



This Page
~~~~~~~~~


+ `Show Source`_




Quick search
~~~~~~~~~~~~

Enter search terms or a module, class or function name.



Introduction¶
=============

This is the documentation for the Sphinx documentation builder. Sphinx
is a tool that translates a set of `reStructuredText`_ source files
into various output formats, automatically producing cross-references,
indices etc. That is, if you have a directory containing a bunch of
reST-formatted documents (and possibly subdirectories of docs in there
as well), Sphinx can generate a nicely-organized arrangement of HTML
files (in some other directory) for easy browsing and navigation. But
from the same source, it can also generate a LaTeX file that you can
compile into a PDF version of the documents, or a PDF file directly
using `rst2pdf`_.

The focus is on hand-written documentation, rather than auto-generated
API docs. Though there is support for that kind of docs as well (which
is intended to be freely mixed with hand-written content), if you need
pure API docs have a look at `Epydoc`_, which also understands reST.

For a great introduction to writing docs in general the whys and hows,
see also `Write the docs`_, written by Eric Holscher.



Conversion from other systems¶
------------------------------

This section is intended to collect helpful hints for those wanting to
migrate to reStructuredText/Sphinx from other documentation systems.


+ Gerard Flanagan has written a script to convert pure HTML to reST;
  it can be found at the `Python Package Index`_.
+ For converting the old Python docs to Sphinx, a converter was
  written which can be found at `the Python SVN repository`_. It
  contains generic code to convert Python-doc-style LaTeX markup to
  Sphinx reST.
+ Marcin Wojdyr has written a script to convert Docbook to reST with
  Sphinx markup; it is at `Google Code`_.
+ Christophe de Vienne wrote a tool to convert from Open/LibreOffice
  documents to Sphinx: `odt2sphinx`_.
+ To convert different markups, `Pandoc`_ is a very helpful tool.




Use with other systems¶
-----------------------

See the ` *pertinent section in the FAQ list*`_.



Prerequisites¶
--------------

Sphinx needs at least Python 2.5 or Python 3.1 to run, as well as
the`docutils`_ and `Jinja2`_ libraries. Sphinx should work with
docutils version 0.7 or some (not broken) SVN trunk snapshot. If you
like to have source code highlighting support, you must also install
the `Pygments`_ library.



Usage¶
------

See ` *First Steps with Sphinx*`_ for an introduction. It also
contains links to more advanced sections in this manual for the topics
it discusses.



Navigation
~~~~~~~~~~


+ `index`_
+ `modules`_ |
+ `next`_ |
+ `previous`_ |
+ `Sphinx home`_|
+ `Documentation`_

Copyright 2007-2013, Georg Brandl. Created using `Sphinx`_ 1.2.1.
.. _Sphinx: http://sphinx-doc.org/
.. _docutils: http://docutils.sf.net/
.. _Pandoc: http://johnmacfarlane.net/pandoc/
.. _rst2pdf: http://rst2pdf.googlecode.com
.. _reStructuredText: http://docutils.sf.net/rst.html
.. _next: http://sphinx-doc.org/tutorial.html
.. _Google Code: http://code.google.com/p/db2rst/
.. _the Python SVN repository: http://svn.python.org/projects/doctools/converter
.. _Python Package Index: https://pypi.python.org/pypi/html2rest
.. _Documentation: http://sphinx-doc.org/contents.html
.. _Get it: http://sphinx-doc.org/install.html
.. _Write the docs: http://write-the-docs.readthedocs.org/
.. _Epydoc: http://epydoc.sf.net/
.. _Extend/Develop: http://sphinx-doc.org/develop.html
.. _index: http://sphinx-doc.org/genindex.html
.. _odt2sphinx: https://pypi.python.org/pypi/odt2sphinx/
.. _Pygments: http://pygments.org/
.. _modules: http://sphinx-doc.org/py-modindex.html
.. _Show Source: http://sphinx-doc.org/_sources/intro.txt
.. _pertinent section in the FAQ list: http://sphinx-doc.org/faq.html#usingwith
.. _Sphinx home: http://sphinx-doc.org/index.html
.. _Jinja2: http://jinja.pocoo.org/


