from handlers.blog_handler import BlogHandler


class BlogMainHandler(BlogHandler):
    def get(self):
        self.render('main.html')
