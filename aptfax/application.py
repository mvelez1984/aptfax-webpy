import web

Urls = ('/posts/', 'app.controllers.posts.List',
		'/posts/create/', 'app.controllers.posts.Create',
		'/posts/(.*)', 'app.controllers.posts.Details'
		)

app = web.application(Urls, globals())

if __name__ == "__main__":
	app.run()