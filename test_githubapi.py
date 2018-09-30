'''
@author Nicole Hilden
September 30 2018

'''

import unittest
from unittest import mock
from mock import mock, Mock
from githubapi import get_repos

class Test(unittest.TestCase):

    @mock.patch('requests.get')
    def test1_mock_repos(self, mockedReq):
        mock_response = [Mock(), Mock(), Mock(), Mock(), Mock(), Mock()]
        mock_response[0].json.return_value = [{"name": '567-hw1'}, {"name": '567-hw2a'},\
            {"name": '567githubAPI'}, {"name": 'GEDCOMProject'}, {"name": 'SSW567'}]
        mock_response[1].json.return_value = [{'sha': 1}, {'sha': 2}, {'sha': 3}]
        mock_response[2].json.return_value = [{'sha': 1}, {'sha': 2}]
        mock_response[3].json.return_value = [{'sha': 1}, {'sha': 2}, {'sha': 3}, {'sha': 4}]
        mock_response[4].json.return_value = [{'sha': 1}, {'sha': 2}, {'sha': 3}]
        mock_response[5].json.return_value = [{'sha': 1}, {'sha': 2}, {'sha': 3}, {'sha': 4}, {'sha': 5}]

        mockedReq.side_effect = mock_response
        self.assertEqual(get_repos("nhilden1114"), [('567-hw1', 3), ('567-hw2a', 2), ('567githubAPI', 4),\
                                                    ('GEDCOMProject', 3), ('SSW567', 5), ])

    @mock.patch('requests.get')
    def test2_mock_repos(self, mockedReq):
        mock_response = [Mock(), Mock(), Mock(), Mock(), Mock()]
        mock_response[0].json.return_value = [{'name': 'hellogitworld'}, {'name': 'helloworld'},\
                                              {'name': 'Project1'}, {'name': 'threads-of-life'}]
        mock_response[1].json.return_value = [{'sha': 1}, {'sha': 2}, {'sha': 3}]
        mock_response[2].json.return_value = [{'sha': 1}, {'sha': 2}]
        mock_response[3].json.return_value = [{'sha': 1}, {'sha': 2}, {'sha': 3}, {'sha': 4}]
        mock_response[4].json.return_value = [{'sha': 1}, {'sha': 2}, {'sha': 3}]

        mockedReq.side_effect = mock_response
        self.assertEqual(get_repos("richkempinski"),[('hellogitworld', 3), ('helloworld', 2), ('Project1', 4),\
                                                   ('threads-of-life', 3)])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
