# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.9.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import client
from client.rest import ApiException
from client.apis.apps_api import AppsApi


class TestAppsApi(unittest.TestCase):
    """ AppsApi unit test stubs """

    def setUp(self):
        self.api = client.apis.apps_api.AppsApi()

    def tearDown(self):
        pass

    def test_get_api_group(self):
        """
        Test case for get_api_group

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
