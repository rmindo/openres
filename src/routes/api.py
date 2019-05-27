def api(http, api):


	# Result
	def result(version, name):

		if version in api:

			return getattr(api[version], name)(http.request)
		else:
			return http.response({'error': 'Invalid API Version'}, 400)



	# Create Invoice
	@http.flask.route('/api/<string:version>/invoices', methods=['POST'])
	def createinvoice(version):

		return result(version, 'createinvoice')