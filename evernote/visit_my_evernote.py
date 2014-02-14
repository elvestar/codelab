# -*- coding: utf-8 -*-
#
# Copyright 2013, Not All Rights Reserved.
# Author:   Windriver
# Email:    windriver1986@gmail.com
# Created:  2013-09-26 01:13
#
# Description: 

from evernote.edam.userstore import UserStore
from evernote.edam.notestore import NoteStore
from evernote.edam.type import ttypes

import thrift.protocol.TBinaryProtocol as TBinaryProtocol
import thrift.transport.THttpClient as THttpClient


print "代码演示了如何调用中文Evernote（印象笔记）的API来访问开发者自己的笔记。"\
    "主要难点是理解Thrift RPC的使用，以及UserStore和NoteStore这两个核心概念"
print "获得了UserStore和NoteStore之后，事情就变得好办了。"\
    "可参考：http://dev.yinxiang.com/documentation/reference/"

# 开发者Token和note_store_url使用你从官方获得的
# 链接：http://dev.yinxiang.com/documentation/cloud/chapters/Authentication.php#devtoken
# user_store_url是通用的
dev_token = "S=s26:U=58bf4e:E=14b34e43adc:C=143dd330edf:P=1cd:A=en-devtoken:V=2:H=d6b3eccf27e88dc219018b0fe2ce1cab"
user_store_url = "https://app.yinxiang.com/edam/user"
note_store_url = "https://app.yinxiang.com/shard/s26/notestore"

# 建立 UserStore 的 Client
user_store_client = THttpClient.THttpClient(user_store_url)
user_store_proto = TBinaryProtocol.TBinaryProtocol(user_store_client)
user_store = UserStore.Client(user_store_proto, user_store_proto)

print "\n输出用户的信息:"
user = user_store.getUser(dev_token)
print user.username, user.id

# 建立 NoteStore 的 Client 
note_store_client = THttpClient.THttpClient(note_store_url)
note_store_proto = TBinaryProtocol.TBinaryProtocol(note_store_client)
note_store = NoteStore.Client(note_store_proto, note_store_proto)

print "\n输出各个笔记本的信息:"
notebooks = note_store.listNotebooks(dev_token)
notebook_tool = ""
for notebook in notebooks:
  if notebook.name == "工具":
    print "Find notebook (工具)"
    notebook_tool = notebook


note_filter = NoteStore.NoteFilter(order = ttypes.NoteSortOrder.UPDATED, ascending = False, 
    notebookGuid = notebook_tool.guid)

note_count_in_tool = note_store.findNoteCounts(dev_token, note_filter, False)
print notebook_tool.name, notebook_tool.serviceCreated, note_count_in_tool.notebookCounts

# Get meta data list
metadata_spc = NoteStore.NotesMetadataResultSpec(includeTitle = True, includeContentLength = True)
note_metadata_list = note_store.findNotesMetadata(dev_token, note_filter, 0, 200, metadata_spc)
print note_metadata_list.totalNotes

# Traversal note
for note_metadata in note_metadata_list.notes:
  print "Title: ", note_metadata.title, ", length: ", note_metadata.contentLength
  note = note_store.getNote(dev_token, note_metadata.guid, withContent = True,
      withResourcesData = False, withResourcesRecognition = False, 
      withResourcesAlternateData = False)
  print note.content
  break

