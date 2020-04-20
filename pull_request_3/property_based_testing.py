
import os
import sys
import unittest
sys.path.append("../")
import praw

class submissionUnitTest(unittest.TestCase):

    
    def testLogin(self):
        login_doc='../../credentials.yaml'
        with open(login_doc,'r') as stream:
            credentials=yaml.load(stream)
        
        
        self.reddit=None
        self.username=credentials['username']
        self.appName=credentials['user_agent']
        self.subreddit=credentials['subreddit']
        self.password=credentials['password']
        self.personal_use_script=credentials['personal_use_script']
        self.client_secret=credentials['client_secret']
        #If login works 
        r=praw.Reddit(client_id=self.personal_use_script,
                     client_secret=self.client_secret,
                     user_agent='',
                     username=self.username,
                     password='')
        return r
    
    #Intended to test whether or not praw will make this read only during log in
    def testReadOnlyProperty(self):
        r=self.login()
        title="First Unit Test"
        body=''
        subreddit=r.subreddit('comp587testing')
        subreddit.submit(title=title,selftext=body)       