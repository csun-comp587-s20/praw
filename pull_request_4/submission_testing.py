import unittest
import praw
import yaml
import sys
import random 
import pprint
import warnings
# Submissions 
#   - Delete 
#   - Upvote
#   - DownVote 
class submissionTest(unittest.TestCase):

    # Tests deleteing top submission in 'hot' category 
    def testDeleteOneSubmission(self): 
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        r = self.login() 
        subreddit = r.subreddit('comp587testing') 

        self.postToSubreddit(1)

        # submission id for deleting 
        submission_id = None 
        for submission in subreddit.hot(limit=1):
            submission_id = submission 
        
        submission = r.submission(id = submission_id) 
        submission.delete()

        self.assertEqual(submission.selftext, '[deleted]')

    def testDeleteTwoSubmission(self): 
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        r = self.login() 
        subreddit = r.subreddit('comp587testing') 

        self.postToSubreddit(2)

        # submission id for deleting 
        submission_id = None 
        for submission in subreddit.hot(limit=2):
            submission_id = submission 
            submission = r.submission(id = submission_id) 
            submission.delete()

            self.assertEqual(submission.selftext, '[deleted]')

    # # Tests upvote one submission in 'hot' category
    # # Because the bot automatically upvotes a submission when it is created 
    # # The N amount of submissions to be upvoted is FIRST downvoted  
    def testUpvoteOneSubmission(self): 
        r = self.login() 
        subreddit = r.subreddit('comp587testing') 
        
        self.downVoteSubmission(1) 

        upvote_score = 0

        for submission in subreddit.hot(limit=1): 
            upvote_score += submission.score 
            submission.upvote() 

        # print (upvote_score)
        self.assertEqual(upvote_score, 1)

    def testUpvoteAtMostThreeSubmission(self): 
        r = self.login() 
        subreddit = r.subreddit('comp587testing') 

        amount_to_downvote = self.randomInts(1, 3) 
        # print(amount_to_downvote) 
        self.downVoteSubmission(amount_to_downvote)

        N_score = 0 
        for submission in subreddit.hot(limit = amount_to_downvote):
            N_score += submission.score
            submission.upvote() 
        
        self.assertEqual(N_score, amount_to_downvote)

    # # Because the bot automatically upvotes a submission when it is created 
    # # The N amount of submissions to be downvoted is FIRST upvoted 
    def testOneSubmissionDownVote(self): 
        r = self.login() 
        subreddit = r.subreddit('comp587testing')

        self.upVoteSubmission(1) 

        downvote_score = 0 
        for submission in subreddit.hot(limit = 1): 
            submission.downvote() 
            downvote_score += submission.score
        
        self.assertEqual(1, downvote_score)

    def testAtMostThreeSubmissionDownVote(self):
        r = self.login() 
        subreddit = r.subreddit('comp587testing')

        amount_to_upvote = self.randomInts(1, 3) 
        self.upVoteSubmission(amount_to_upvote)

        N_score = 0 
        for submission in subreddit.hot(limit = amount_to_upvote): 
            submission.downvote() 
            N_score += submission.score
        self.assertEqual(N_score, amount_to_upvote)


    # METHODS BELOW ARE NOT PART OF TESTS 
    def upVoteSubmission(self, amount): 
        r = self.login() 
        subreddit = r.subreddit('comp587testing')

        for submission in subreddit.hot(limit = amount): 
            submission.upvote() 

    def downVoteSubmission(self, amount): 
        r = self.login() 
        subreddit = r.subreddit('comp587testing')

        for submission in subreddit.hot(limit = amount): 
            submission.downvote() 

    def randomInts(self, minlength, maxlength):
        rand = random.randint(minlength, maxlength)
        return rand
    
    def postForTesting(self):
        post = 0
        randompost = 25
        while (post < randompost): 
            r = self.login()
            title = 'Post # ' + str(post) + ' for submission testing'
            body = 'body for post'
            subreddit = r.subreddit('comp587testing')
            subreddit.submit(title=title, selftext=body)
            post += 1
    
    def postToSubreddit(self, amountToPost): 
        posted = 0 
        while (posted < amountToPost): 
            r = self.login() 
            title = 'Post # ' + str(posted)
            body = 'body for post' 
            subreddit = r.subreddit('comp587testing') 
            subreddit.submit(title=title, selftext=body) 
            posted += 1 
        
    def login(self): 
        login_doc='../credentials.yaml'
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

if __name__=='__main__' :
    # warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
    unittest.main()


    # submissionTest = submissionTest() 
    # submissionTest.testDeleteOneSubmission()
    # submissionTest.is_removed()
    # submissionTest.postForTesting()