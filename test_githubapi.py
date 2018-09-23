'''
@author Nicole Hilden
September 22 2018

'''

import unittest
from githubapi import get_repos, get_commits

class Test(unittest.TestCase):

    def test1_repos(self): 
        repos = get_repos("nhilden1114")
        self.assertEqual(len(repos), 5, "nhilden1114 currently has 5 repos")
        self.assertIn("SSW567", repos)
        self.assertIn("567-hw1", repos)
        self.assertIn("567-hw2a", repos)
        self.assertIn("GEDCOMProject", repos)
        self.assertIn("567githubAPI", repos)

    def test2_repos(self):
        repos = get_repos("richkempinski")
        self.assertEqual(len(repos), 4, "richkempinski currently has 4 repos")
        self.assertIn("hellogitworld", repos)
        self.assertIn("helloworld", repos)
        self.assertIn("Project1", repos)
        self.assertIn("threads-of-life", repos)

    def test3_commits(self):
        self.assertEqual(get_commits("nhilden1114", "SSW567"),1)
        self.assertEqual(get_commits("nhilden1114", "567-hw1"),4)
        self.assertEqual(get_commits("nhilden1114", "567-hw2a"),12)
        self.assertEqual(get_commits("nhilden1114", "SSW567"),1)

    def test4_commits(self):
        self.assertEqual(get_commits("richkempinski", "hellogitworld"),30)
        self.assertEqual(get_commits("richkempinski", "helloworld"),2)
        self.assertEqual(get_commits("richkempinski", "Project1"),2)
        self.assertEqual(get_commits("richkempinski", "threads-of-life"),1)

    def test5_invalid(self):
        self.assertEqual(get_repos("skjfasdjfu"),[])
        self.assertEqual(get_repos("eudjcvkjhd"),[])
        self.assertEqual(get_repos("lkeiuvhasq"),[])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
