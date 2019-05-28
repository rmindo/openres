# Flask Framework
from flask import Flask, jsonify, request, make_response, Response


# Routes
from src.routes.api import api

# Authentication
from src.models.auth import Auth


# Dummy Credentials
users = {
	'email': 'ruel@mindo.com',
	'auth': {
		'key': 'secretkey',
		'password': 'test',
		'token': 'F6Xik2zCXdAEBdIKkOmeZuR6BasPQ4QeuxTZEo5kn44wjT9wVl3YZU6uHhMwGW276GfMEt38AQlRxxEAwSkuD8eydleHAnOiAxNTYxNjI2MjM2LjAsICdpZCc6IDF9YTBjZmM2OWFmZDk2NWMyYzNmNDg3ZTk5OGUyOTFiMzc5MWI3Yzk5YzFkMTE0MzRmNjg3MDk1NjU3NWI3MmM3Ng'
	}
}


# HTTP
class HTTP:

	status = {
		'200': 'Ok',
		'201': 'Created',
		'400': 'Bad Request',
		'401': 'Unauthorized',
		'403': 'Forbidden',
		'404': 'Not Found',
		'405': 'Method Not Allowed',
		'406': 'Not Acceptable',
		'409': 'Conflict',
	}

	# Request
	request = request



	def __init__(self):

		# Authentication
		self.auth = Auth()

		# Flask Framework
		self.flask = Flask(__name__)



	# API Services
	def api(self, service):
		api(self, service)




	# Response
	def response(self, data = [], code = 401):

		para = {
			'status': code,
			'message': self.status[str(code)],
		}

		if 'error' in data:
			para['status'] = data['code']
			para['result'] = {'error': data['error']}

			response = make_response(jsonify(para), data['code'])

			if 'headers' in data:
				for i,v in data['headers'].items():
					response.headers.set(i,v)
			return response
		else:
			if len(data) > 0:

				para['result'] = data


		return make_response(jsonify(para), code)




	# Authenticate
	def authenticate(self):

		auth = request.headers.get('authorization')

		if auth.find('Basic') >= 0:
			basic = self.auth.decode(auth.replace('Basic ', '')).split(':')

			if basic[0] == users['email'] and basic[1] == users['auth']['password']:
				return True
			else:
				r = {
					'code': 401,
					'error': 'Username/Password is Required',
					'headers': {
						'WWW-Authenticate': 'Basic realm="Required"'
					}
				}

				return r
		else:
			if auth.find('Bearer') >= 0:
				parse = self.auth.parse(auth.replace('Bearer ', ''))

				if parse and 'payload' in parse:
					# Payload
					payload = parse['payload']

					if 'token' in parse:
						if users['auth']['token'] == parse['token']:
							# Verify token
							return self.auth.verify(users['auth']['key'], payload, parse['signature'])

				return {'code': 401, 'error': 'Invalid Token'}