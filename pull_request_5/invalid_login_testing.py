
import unittest
import sys
sys.path.append("../")
import praw
import yaml

#Invalid Login 
#-Login

class invLoginTesting(unittest.TestCase):

    def invLogin(self): 
        try:
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
            r = praw.Reddit(
                    #Try logging in without client Id or client secret
#                    client_id=self.personal_use_script,
#                         client_secret=self.client_secret,
                         user_agent=self.appName,
                         username=self.username,
                         password=self.password)
            print(r.read_only)
            print(r.auth())
            return r
        except:
            return "FAILED LOGIN: Need client secret and ID"

    def testInvLogin(self):
        exception="FAILED LOGIN: Need client secret and ID"
        assert(self.invLogin()==exception)
    
if __name__=="__main__":
    unittest.main()