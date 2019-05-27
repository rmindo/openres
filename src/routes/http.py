# Flask Framework
from flask import Flask, jsonify, request, make_response


# Routes
from src.routes.api import api

# Authentication
from src.models.auth import Auth


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

		if len(data) > 0:

			para['result'] = data

		return make_response(jsonify(para), code)




	# Authenticate
	def authenticate(self):

		bearer = self.http.headers.get('authorization')

		if bearer:

			return bearer
		else:

			basic = request.authorization

		return {}