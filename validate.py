# -*- coding=UTF-8 -*-
from urlparse import parse_qs
from hashlib  import sha1

def validate(environ, start_response):
	'''这个函数用于验证接口配置信息，或者修改 token 后用于重新验证。
	仅当向微信申请成为开发者时使用。
	本函数返回两个参数，第一个参数指示验证是否成功，第二个参数是验证
	成功后需要向微信返回的 echostr。参考微信文档'''

	token = '******' #这个是自己取的，和微信平台上一致即可
	query_string = environ['QUERY_STRING']
	qs_dic = parse_qs(query_string)

	signature = qs_dic['signature'][0] if 'signature' in qs_dic else ''
	timestamp = qs_dic['timestamp'][0] if 'timestamp' in qs_dic else ''
	nonce = qs_dic['nonce'][0] if 'nonce' in qs_dic else ''
	echostr = qs_dic['echostr'][0] if 'echostr' in qs_dic else ''

	s = ''.join(sorted([token, timestamp, nonce]))
	encryptor = sha1()
	encryptor.update(s)

	#如果验证成功，就向微信服务器回传 echostr	
	if signature == encryptor.hexdigest():
		status = '200 OK'
		response_headers = [('Content-type', 'text/plain'),
							('Content-Length', str(len(echostr)))]

		start_response(status, response_headers)
		return [echostr]

def application(environ, start_response):
	'''application 是 mod_wsgi 规定的入口点'''
	return validate(environ, start_response)
