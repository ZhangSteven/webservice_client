"""
Test the open_bal() method to open the trustee Macau Balanced Fund.
"""

import unittest2
from webservice_client.id_lookup import get_security, put_security
from webservice_client.utility import get_server_url


class TestLookup(unittest2.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestLookup, self).__init__(*args, **kwargs)



    def test_get_security(self):
        data = get_security(get_server_url(), 'JPM', '0D5402S')
        self.assertEqual(len(data), 8)
        self.assertEqual(data['security_id_type'], 'JPM')
        self.assertEqual(data['security_id'], '0D5402S')
        self.assertEqual(data['currency'], 'HKD')
        self.assertEqual(data['isin'], '')
        self.assertEqual(data['bloomberg_figi'], 'BBG00D2SB834')
        self.assertEqual(data['geneva_investment_id'], '')



    def test_put_security(self):
        """
        Create a new security
        """
        data = put_security(get_server_url(), get_security_data())
        self.assertEqual(data, 'OK')



    def test_put_security2(self):
        """
        Update an existing security
        """
        pass



def get_security_data():
    return {
        'security_id_type':'CMU',
        'security_id':'WLHKFN09007',
        'name':'WING LUNG BANK LTD 5.7 28DEC2021',
        'isin':'',
        'bloomberg_figi':'BBG00000WLY9',
        'geneva_investment_id':'BBG00000WLY9 HTM',
        'currency':'',
        'comments':'This one has no ISIN, as of 2016-11-29'
    }

