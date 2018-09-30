'''
@author Nicole Hilden
September 30 2018

'''

import unittest
from unittest import mock
import githubapi

class Test(unittest.TestCase):
    
    @mock.patch("githubapi.get_repos")
    def test1_repos(self, mock_repos):
        mock_repos.return_value = ["SSW567", "GEDCOMProject", "567-hw1", "567-hw2a", "567githubAPI"]
        repos = githubapi.get_repos("nhilden1114")
        self.assertEqual(len(repos), 5, "nhilden1114 currently has 5 repos")
        self.assertIn("SSW567", repos)
        self.assertIn("567-hw1", repos)
        self.assertIn("567-hw2a", repos)
        self.assertIn("GEDCOMProject", repos)
        self.assertIn("567githubAPI", repos)

    @mock.patch("githubapi.get_repos")
    def test2_repos(self, mock_repos):
        mock_repos.return_value = ["hellogitworld", "helloworld", "Project1", "threads-of-life"]
        repos = githubapi.get_repos("richkempinski")
        self.assertEqual(len(repos), 4, "richkempinski currently has 4 repos")
        self.assertIn("hellogitworld", repos)
        self.assertIn("helloworld", repos)
        self.assertIn("Project1", repos)
        self.assertIn("threads-of-life", repos)

    @mock.patch("githubapi.get_commits")
    def test3_commits(self, mock_commits):
        mock_commits.return_value = 1
        self.assertEqual(githubapi.get_commits("nhilden1114", "SSW567"),1)
        mock_commits.return_value = 4
        self.assertEqual(githubapi.get_commits("nhilden1114", "567-hw1"),4)
        mock_commits.return_value = 12
        self.assertEqual(githubapi.get_commits("nhilden1114", "567-hw2a"),12)

    @mock.patch("githubapi.get_commits")
    def test4_commits(self, mock_commits):
        mock_commits.return_value = 30
        self.assertEqual(githubapi.get_commits("richkempinski", "hellogitworld"),30)
        mock_commits.return_value = 2
        self.assertEqual(githubapi.get_commits("richkempinski", "helloworld"),2)
        mock_commits.return_value = 1
        self.assertEqual(githubapi.get_commits("richkempinski", "threads-of-life"),1)

    @mock.patch("githubapi.get_repos")
    def test5_invalid(self, mock_repos):
        mock_repos.return_value = []
        repos = githubapi.get_repos("jsdhfasdfj")
        self.assertEqual(len(repos), 0, "jsdhfasdfj is invalid")
        

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
