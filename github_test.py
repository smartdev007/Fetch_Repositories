"""
    @author Jenish Kevadia
    Script imports methods from 'github.py' script and implements test cases for the github repositories
"""


import unittest
import json
from github import get_repositories
from unittest import mock

def get_link(url):
    """ Fetch URL """
    if url == 'https://api.github.com/users/dev22/repos':
        return fetch('repos.json')

def fetch(path):
    """ Open path file """
    data = text()
    with open(path, 'r') as f:
        data.text = json.loads(f)
    return data.text

class text:
    """ Declare text class for path file """
    text = ""


class TestGithub(unittest.TestCase):
    """ Test cases """

    @mock.patch('requests.get')
    def test_get_repositories(self, mockedReq):
        """ Test case to check the user's repositories and commits"""
        mockedReq.side_effect = get_link

        repos = get_repositories('dev22')
        self.assertEqual(repos, "Failed to fetch the repos")


if __name__ == "__main__":
    """ Run test cases on startup """
    unittest.main(exit=False, verbosity=2)
