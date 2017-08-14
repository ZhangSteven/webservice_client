# coding=utf-8
# 
import requests
from .logging_utility import logger



def get_security(url, security_id_type, security_id):
	"""
	Get security details from url.
	"""
	logger.info('get_security(): enter')
	
	payload = {'security_id_type':security_id_type, 'security_id':security_id}
	
	logger.debug('get_security(): get url: {0}'.format(url))
	logger.debug('get_security(): security_id_type: {0}, security_id: {1}'.
					format(security_id_type, security_id))
	
	try:
		r = requests.get(url, params=payload)
		if r.status_code == 200:
			return r.json()
		else:
			logger.error('get_security(): not OK. return status code {0}'.format(r.status_code))
			return {}

	except:
		logger.exception('get_security(): ')
		return {}



def put_security(url, security_data):
	"""
	Create or update a security based on security_data.

	We expect a HTTP 200 OK if an updated is processed successfully,
	and HTTP 201 Created if a new security is added.
	"""
	logger.info('put_security(): enter')
	logger.debug('put_security(): put url: {0}'.format(url))
	logger.debug('put_security(): put data: {0}'.format(security_data))
	
	try:
		r = requests.put(url, data=security_data)
		if r.status_code == 200:
			return 'OK'
		else:
			logger.error('put_security(): not OK. return status code {0}'.format(r.status_code))
			return 'Bad'
	except:
		logger.exception('put_security(): ')
		return 'Error'