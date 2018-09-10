import urllib.request
import json

content = input('请输入翻译内容:')

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {}
data['i']= content
data['from'] =  'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] =  '1536579531515'
data['sign'] =  'd91d39137b109dd7ef8ff8f4e25efb44'
data['doctype'] = 'json'
data['version'] =  '2.1'
data['keyfrom'] =  'fanyi.web'
data['action'] ='FY_BY_CLICKBUTTION'
data['typoResult'] =  'false'
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')

target = json.loads(html)


print('翻译结果：%s' %(target['translateResult'][0][0]['tgt']))
