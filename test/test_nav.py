"""
Test the open_bal() method to open the trustee Macau Balanced Fund.
"""

import unittest2
from webservice_client.nav import upload_nav



class TestNAV(unittest2.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestNAV, self).__init__(*args, **kwargs)



    def test_upload_nav(self):
        """
        Create a new security
        """
        self.assertTrue(upload_nav('19437', 12345.67, '2017-8-10', 1000, 12.3))

        # should fail due to invalid date
        self.assertFalse(upload_nav('19437', 12345.67, '2017-15-10', 1, 1))

        # should fail due to invalid nav
        self.assertFalse(upload_nav('19437', 0, '2017-12-10', 1, 1))

        # should fail due to invalid nav
        self.assertFalse(upload_nav('19437', '10a', '2017-12-10', 1, 1))

        # should fail due to invalid portfolio id
        self.assertFalse(upload_nav('AB123', 12345.67, '2017-12-10', 1, 1))

        # should fail due to invalid num_units
        self.assertFalse(upload_nav('19437', 12345.67, '2017-12-10', '10b', 1))

        # This is actually OK
        self.assertTrue(upload_nav('19437', 12345.67, '2017-12-10', '100.0', '1.2'))