# coding: utf8

import urllib2
import json

user_agent = 'sublime plugin'

def send_req(url):
    try:
        headers = {'User-Agent': user_agent}
        request = urllib2.Request(url, headers=headers)
        opener = urllib2.build_opener()
        resp = opener.open(request)
        data = resp.read()
        opener.close()
        return data
    except:
        return 0

def qqdict(word, user_agent=user_agent):
    url = 'http://dict.qq.com/dict?q=%s' % word

    data = send_req(url)
    if data == 0:
        return ['network error']

    res   = json.loads(data)
    local = res.get('local', [])
    baike = res.get('baike', [])

    result = []

    if local:
        des = local[0]['des']
        for item in des:
            if item.get('p', None):
                result.append('%s %s' % (item['p'], item['d']))
            else:
                result.append(item['d'])
    elif baike:
        # bkstr = baike[0]['abs']
        result = [u'百科']
    else:
        result = ['not found']

    return result

def youdao(word, user_agent=user_agent):
    url = 'http://fanyi.youdao.com/openapi.do?keyfrom=SublimePlugIn&key=1604792744&type=data&doctype=json&version=1.1&q=%s' % word

    data = send_req(url)
    if data == 0:
        return ['network error']

    res   = json.loads(data)
    basic = res.get('basic', [])
    web   = res.get('web', [])
    
    result = []

    if basic:
        result = basic['explains']
    elif web:
        result = [u'网络释义']
    else:
        result = ['not found']

    return result

if __name__ == '__main__':
    import sys
    res = youdao(sys.argv[1], 'plugin for sublime text 2')
    for r in res:
        print r
