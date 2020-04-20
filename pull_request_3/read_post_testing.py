import yaml
import sys
import urllib.request #for generating words 
import random
import unittest
 
sys.path.append("../")
import praw 



class submissionUnitTest(unittest.TestCase):
    
    def login(self):
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
                     user_agent=self.appName,
                     username=self.username,
                     password=self.password)
        return r
        
    def testReadSubmission(self):
        r=self.login()
        link_to_post='https://www.reddit.com/r/comp587testing/comments/g3vlu6/title_1/'
        
        post_1=r.submission(url=link_to_post)
        
        assert(post_1.title=='Title 1')
        assert(post_1.selftext=='Body 1')
        assert(post_1.num_comments!=None)
#        for commentForest in post_1.comments:
#            for comment in commentForest:
#                print(comment)
#                print(dir(comment))
    #            assert(comment.selftext[0:6]=='Comment')
    def testAutomatedReadSubmission(self):
        r=self.login()
        for submission in r.subreddit('comp587testing').hot():
            assert(submission.title!=None)
            assert(submission.author!=None)
    
    def testAutoamtedComment(self):
        r=self.login()
#        link_to_post='https://www.reddit.com/r/comp587testing/comments/g3vlu6/title_1/'
#        post_1=r.submission(url=link_to_post)    
        for submission in r.subreddit('comp587testing').hot():
            for i in range(0,10):
                submission.reply("comment"+str(i))
        
if __name__=='__main__' :
    unittest.main()
#    teehee=submissionUnitTest()
#    teehee.unitReadSubmission()