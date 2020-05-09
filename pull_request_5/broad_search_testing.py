import unittest
import sys
sys.path.append("../")
import praw
import yaml
import random 
import pprint
import warnings
#Broad search testing
#Run a search with praw with new/top and see if it matches what the user sees
class searchTesting(unittest.TestCase):
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
        r = praw.Reddit(client_id=self.personal_use_script,
                     client_secret=self.client_secret,
                     user_agent=self.appName,
                     username=self.username,
                     password=self.password)
        return r
    
    def BroadSearch(self):
        r=self.login()
        
        #We're going to pick some popular subreddits to do our wide search 
        #and ask for the first 100 of the top posts of each of the subeddits.
        #If this is consistent with what we saw and produces the same results in 
        #a search, this will pass our parameteres
        subs=['politics','AskMen','AskReddit','gaming','Comp587Testing',
              'rarepuppers']
        
        
        #If submission works it should be consistent no matter how many
        #times we do the same search
        for sub in subs:
            titles=[]
            for i in range(0,10):
                print("Starting Pass: ",i)
                
                if(i==0):
                    for submission in r.subreddit(sub).hot(limit=100):
                        titles.append(submission.title)
                        print(titles)
                else:
                    #We'll define successful if at least 90% of titles overlap
                    pass_limit=0
                    for submission in r.subreddit(sub).hot(limit=100):
                        print(submission.title)
                        if(pass_limit>3):
                            return "FAILURE"
                        if submission.title in titles:
                            pass
                        else:
                            pass_limit+=1
                    
        return "SUCCESS"
    
    def testBroadSearch(self):
        assert(self.BroadSearch()=="SUCCESS")
        
        
if __name__=="__main__":
    unittest.main()