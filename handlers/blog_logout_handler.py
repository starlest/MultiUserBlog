from handlers.blog_handler import BlogHandler


class BlogLogoutHandler(BlogHandler):
    def get(self):
        self.logout()
        self.redirect('/blog')
