#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt
import os
import sys

class RedditScraper():

    def __init__(self):
        # set api keys and secrets from os
        reddit_client_id = os.environ.get('REDDIT_CLIENT_ID')
        reddit_client_secret = os.environ.get('REDDIT_CLIENT_SECRET')
        reddit_user = os.environ.get('REDDIT_USER')
        reddit_pw = os.environ.get('REDDIT_PW')

        # define reddit instance variable used to scrape 
        self.reddit = praw.Reddit(client_id=reddit_client_id, \
                            client_secret=reddit_client_secret, \
                            user_agent='scraper', \
                            username=reddit_user, \
                            password=reddit_pw)

    def scrape_subreddit(self, subreddit_name):

        subreddit = self.reddit.subreddit('politics')

        topics_dict = { 
            "title":[],
            "score":[],
            "id":[], "url":[],
            "comms_num": [],
            "created": [],
            "body":[]
            }

        for submission in subreddit.top('day', limit=12):
            topics_dict["id"].append(submission.id)
            topics_dict["created"].append(submission.created)
            topics_dict["score"].append(submission.score)
            topics_dict["url"].append(submission.url)
            topics_dict["comms_num"].append(submission.num_comments)
            topics_dict["title"].append(submission.title)
            topics_dict["body"].append(submission.selftext)

        topics_data = pd.DataFrame(topics_dict)

        print(topics_data)

        return topics_data

if __name__ == "__main__":
    reddit_scraper = RedditScraper()
    if len(sys.argv) > 1:
        subreddit_name = sys.argv[1]
        reddit_scraper.scrape_subreddit(subreddit_name)
    else:
        reddit_scraper.scrape_subreddit("politics")