# coding=utf-8
# 
import requests
from .utility import get_nav_url
import logging
logger = logging.getLogger(__name__)



def upload_nav(portfolio_id, nav, nav_date, num_units, unit_price):
	"""
	Upload a portfolio's NAV on date (nav_date).

	return True is successful (or should we use exceptions?)
	"""
	logger.info('upload_nav(): enter')
	logger.debug('upload_nav(): url: {0}'.format(get_nav_url()))

	data = {
		'portfolio_id':portfolio_id,
		'nav':nav,
		'date':nav_date,
		'num_units':num_units,
		'unit_price':unit_price
		}
	logger.debug('upload_nav(): data: {0}'.format(data))
	
	try:
		r = requests.post(get_nav_url(), data=data)
		if r.status_code == 200:
			return True
		else:
			logger.error('upload_nav(): not OK. return status code {0}'.format(r.status_code))
			return False

	except:
		logger.exception('upload_nav(): ')
		return False


