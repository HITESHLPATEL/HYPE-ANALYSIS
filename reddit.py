#!/usr/bin/env python


import praw
from praw.models import MoreComments
import datetime as dt
import time

reddit = praw.Reddit(client_id='YOyRRjx4uICZSQ',
                     client_secret='u4CXyYGC0lc6THzWoJ9Njcgj93o',
                     user_agent='my user agent')


submission = reddit.submission(id='93e9m1')

#9li7ex
#9meaoh
#9gn3xa
#9ksse5
#9fldz6

for submission in reddit.subreddit('TheVenomSite').hot(limit=None):
    print dt.datetime.fromtimestamp(submission.created),submission.title.encode("utf-8")

submission.comments.replace_more(limit=None)
for comments in submission.comments:
    print dt.datetime.fromtimestamp(comments.created),comments.body.encode("utf-8")
    time.sleep(1)
