import os
import sys
import unittest
import yaml
sys.path.append("../")
import praw
import time

class authPartsTest(unittest.TestCase):

    
    def Login(self):
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
                     user_agent=self.username,
                     username=self.username,
                     password=self.password)
        return r
    #Testing the property that you can't submit more than two times per second
    def testAutoRate(self):
        r=self.Login()
        title="Time Testing"
        body="time testing body"
        for i in range(0,100):
            start=time.time()
            for i in range(0,3):
                subreddit=r.subreddit('comp587testing')
                subreddit.submit(title=title,selftext=body)       
            end=time.time()-start
            print(end)
            assert((end>1)==True)
    
if __name__=="__main__":
    unittest.main()

            