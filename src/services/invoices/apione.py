# Version
v = 'v1'



# Version 1
class apione():


	# Init
	def __init__(self, http):

		# HTTP
		self.http = http




	def result(self, output, code):

		a = self.http.authenticate()

		if 'error' in a:
			return self.http.response(a['error'], 401)
		else:
			o = output()

			if 'error' in o:
				return self.http.response(o['error'], 400)

			return self.http.response(o, code)




	def createinvoice(self, http):

		data = http.json

		return data