import jwt




# Authentication
class Auth:


	def basic(self, email, password):

		return



	# Decode Token
	def decodetoken(self, token, key):
		
		return jwt.decode(token, key, algorithm='HS256')



	# Create Token
	def createtoken(self, payload, key):
		
		return jwt.encode(payload, key, algorithm='HS256')