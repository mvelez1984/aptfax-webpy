import web
import re
from web import form
from ..models import posts

view = web.template.render('app/views')

class Container(object):
    pass

class List:
	def GET(self):
		result = Container()
		result.query_text = 'all posts'
		result.search_results = posts.find()
		return view.list(result)
	def POST(self):
		input = web.input()
		result = Container()
		query = None
		result.query_text = 'all posts'
		if input.desc_query:
			result.query_text = 'posts with "%s" in description' % input.desc_query
			query = { 'description' : re.compile(input.desc_query, re.IGNORECASE) }
		result.search_results = posts.find(query)
		return view.list(result)

class Details:
	def GET(self, id):
		post = posts.find_by_id(id)
		return view.details(post)

class Create:
	def GET(self):
		return view.create()
	def POST(self):
		posts.insert(web.input())
		raise web.seeother('/posts/')