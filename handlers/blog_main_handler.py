class BlogMainHandler(BlogHandler):
    def get(self):
        self.render('main.html')