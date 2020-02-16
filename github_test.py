"""
    @author Jenish Kevadia

    Script imports methods from 'github.py' script and implements test cases for the github repositories
"""


import unittest
from github import get_repositories

class TestGithub(unittest.TestCase):
    """ Test cases """

    def test_get_repositories(self):
        """ Test case to check the user's repositories and commits"""

        self.assertEqual(get_repositories('dev22'), ["Repo: dev, Number of commits: 2"])
        self.assertEqual(get_repositories('smartdev008'), ["Repo: dev, Number of commits: 2"])


if __name__ == "__main__":
    """ Run test cases on startup """
    unittest.main(exit=False, verbosity=2)