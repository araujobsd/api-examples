#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  The sample code is to show info of your Gandi SSL certificates with api key.
#  此範例程式碼用途為透過api金鑰，取得Gandi SSL憑證相關資訊
#

'''
API INFO: http://doc.rpc.gandi.net/
'''

import xmlrpclib


def show_cert_info(api_key):
    '''
        Receive the API_KEY and output the SSL status per domain.
    '''

    #  Connect to the api server
    #  連接api伺服器
    api = xmlrpclib.ServerProxy('https://rpc.gandi.net/xmlrpc/')

    #  Now you can call api methods.
    #  You must authenticate yourself by passing
    #  the api key as the first method's argument
    #  您可以呼叫api方法
    #  您必須經由api金鑰作為第一個方法的參數進行驗證
    version = api.version.info(api_key)['api_version']
    print "Gandi api version: %s" % (version)

    #  Count your Gandi certs
    #  計算Gandi憑證的數量
    gandi_cert_nums = api.cert.count(api_key)

    gandi_cert_count_msg = "You have %s certificate" % (gandi_cert_nums)
    if gandi_cert_nums > 1:
        gandi_cert_count_msg += "s"
    print gandi_cert_count_msg

    #  Get all certs
    #  取得所有憑證
    cert_list = []
    for eachsite in api.cert.list(api_key):
        cert_list.append(eachsite['id'])
    if len(cert_list) > 0:
        print "Gandi CERT IDs: %s" % (cert_list)

    #  Get info on each Gandi certs
    #  取得各個Gandi憑證的相關資訊
    if len(cert_list) > 0:
        for item in api.cert.list(api_key):
            print "Domain: %s with SSL status: %s" % (
                item['cn'], item['status'])


if __name__ == '__main__':
    API_KEY = raw_input("Enter <YOUR API KEY>: ")
    if len(API_KEY) < 24:
        print "<YOUR API KEY> must have 24 characters"
    else:
        show_cert_info(API_KEY)
