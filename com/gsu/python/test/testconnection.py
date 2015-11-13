'''
Created on Oct 1, 2015

@author: Ashwin
'''
from pymongo import MongoClient
import datetime


c= MongoClient()
db = c['test']
print(db['mycol'])
post = {"author": "Mike","text": "My first blog post!","tags": ["mongodb", "python", "pymongo"],"date": datetime.datetime.utcnow()}
posts = db.posts
post_id = posts.insert_one(post).inserted_id
post_id