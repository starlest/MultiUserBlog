from handlers.blog_handler import BlogHandler
from google.appengine.ext import db

from models.blog_post import BlogPost


class BlogPostPageHandler(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('BlogPost', int(post_id), parent=self.blog_key())
        post = db.get(key)

        if not post:
            self.render("404-not-found.html")
            return

        self.render("permalink.html", post=post)
