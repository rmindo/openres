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

		if a == True:
			return self.http.response(output, code)
		else:
			return self.http.response(a)




	def createinvoice(self, req):

		data = req.json

		return self.result(data, 201)