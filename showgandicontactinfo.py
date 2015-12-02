#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  此範例程式碼用途為透過API金鑰，取得聯絡人相關資訊

'''
API INFO: http://doc.rpc.gandi.net/
'''

import xmlrpclib


def show_contact_info(api_key):
    '''
        Receive the API_KEY and output the HANDLER and EMAIL.
    '''

    #  連接API伺服器
    api = xmlrpclib.ServerProxy('https://rpc.gandi.net/xmlrpc/')

    #  您可以呼叫API方法
    #  您必須經由API金鑰作為第一個方法的參數進行驗證
    version = api.version.info(api_key)['api_version']
    print "Gandi api version: %s" % (version)

    #  取得帳號ID
    handle_list = []
    for eachcontact in api.contact.list(api_key):
        handle_list.append(eachcontact['handle'])

    print "Gandi Site IDs: %s" % (handle_list)

    #  取得個別的Gandi帳號資料
    if len(handle_list) > 0:
        for item in api.contact.list(api_key):
            print "Handler: %s \t\t Contact: %s" % (
                item['handle'], item['email'])

if __name__ == '__main__':
    API_KEY = raw_input("Enter <YOUR API KEY>: ")
    if len(API_KEY) < 24:
        print "<YOUR API KEY> must have 24 characters"
    else:
        show_contact_info(API_KEY)
