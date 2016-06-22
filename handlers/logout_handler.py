from handlers.blog_handler import BlogHandler


class LogoutHandler(BlogHandler):
    def get(self):
        self.logout()
        self.redirect('/blog')
