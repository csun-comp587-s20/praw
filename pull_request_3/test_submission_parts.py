
import yaml
import sys
import urllib.request #for generating words 
import random 
import unittest
sys.path.append("../")
import praw 


class automatedTesting(): 

    def readOnlylogin(self):
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
        r = praw.Reddit(client_id=self.personal_use_script,
                     client_secret=self.client_secret,
                     user_agent=self.appName)
        return r

    #Test the no read for praw    
    def readOnly(self):
        try:  
            r = self.readOnlylogin()
            title = 'Teehee'
            body = 'Teehee'
            subreddit = r.subreddit('comp587testing')
            subreddit.submit(title=title, selftext=body)        
            return "Success"
        except Exception as e:
            return str(e)
    def testReadOnly(self):
        assert(self.readOnly()=="USER_REQUIRED: 'Please log in to do that.'")
        
if __name__=='__main__' :
    auto=automatedTesting()
    auto.testReadOnly()