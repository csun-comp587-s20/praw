import unittest
import praw
import yaml
import sys
import random 
import pprint
import warnings
# Comments
#   - Delete 
#   - Upvote
#   - DownVote 
class commentTesting(unittest.TestCase):
    # Delete comments made in postComment() 
    def testDeleteMadeComments(self): 
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        r = self.login() 
        subreddit = r.subreddit('comp587testing') 
        # Posts a certain amount of comments 
        # count = the number of comments in the post before deleting
        count = self.postComment()
        post = r.submission(id = 'g9vrj1')
    
        for top_level_comment in post.comments: 
            comment = r.comment(top_level_comment)
            comment.delete() 
        
        # need updated submission id to find updated amount of comments in post 
        updatedPostID = r.submission(id = 'g9vrj1')
        self.assertLess(updatedPostID.num_comments, count)

    # Test for upvoting comments
    def testOneUpvote(self): 
        r = self.login() 
        subreddit = r.subreddit('comp587testing')

        submission = r.submission(id = 'g9zcj8')
        # number of downvotes of all comments 
        amount_of_upvotes = 0
        # loop through all comments in submission and upvote once 
        for comments in submission.comments: 
            current_comment = r.comment(comments)
            # append # of downvotes on comments 
            amount_of_upvotes += current_comment.ups
            current_comment.upvote()

        self.assertGreater(amount_of_upvotes, 0)     

    # The bot account used to post comments 
    # automatically upvotes when it posts a comment 
    # Therefore the downvote should be 0 
    def testOneDownVote(self): 
        r = self.login() 
        subreddit = r.subreddit('comp587testing')
        submission = r.submission(id = 'g9zcj8')
        # number of downvotes of all comments 
        amount_of_downvotes = 0
        # loop through all comments in submission and downvote once 
        for comments in submission.comments: 
            current_comment = r.comment(comments)
            # append # of downvotes on comments 
            amount_of_downvotes += current_comment.downs
            current_comment.downvote()

        self.assertLessEqual(amount_of_downvotes, 0)

    # METHODS BELOW ARE NOT PART OF TESTS 
    # unittest library only runs test on methods that start with 'test' 
    def postComment(self): 
        r = self.login() 
        subreddit = r.subreddit('comp587testing') 

        submission = r.submission(id='g9vrj1')
        # amount of commnets to add to post
        number_of_comments = self.randomInts(1, 5) 
        # print(number_of_comments)
        while (number_of_comments > 0):
            submission.reply('This is a comment')
            number_of_comments -= 1

        # return updated amount of comments after adding 
        updated_submission = r.submission(id='g9vrj1')
        # print(updated_submission.num_comments)
        return updated_submission.num_comments
        
    # generates random integers 
    def randomInts(self, minlength, maxlength):
        rand = random.randint(minlength, maxlength)
        return rand
    
    def postForTesting(self):
        r = self.login()
        subreddit = r.subreddit('comp587testing')
        title = 'Post For upvote / downvote'
        body = 'This is a generated post to test upvoting / downvoting comments'
        subreddit.submit(title=title, selftext=body)
        
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
    unittest.main()

    # commenttest = commentTesting() 
    # commenttest.testOneDownVote()
    # commenttest.DeleteComment()
    # commenttest.postComment()
