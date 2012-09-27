from config import db
from bson import ObjectId

def find(q=None):
	return db.posts.find(q)

def find_by_id(_id):
	return db.posts.find_one({ '_id' : ObjectId(_id) })

def insert(post):
	db.posts.insert(post)