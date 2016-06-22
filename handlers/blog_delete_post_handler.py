from handlers.blog_handler import BlogHandler
from google.appengine.ext import db


class BlogDeletePostHandler(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('BlogPost', int(post_id),
                               parent=self.blog_key())
        p = db.get(key)
        if self.user and p and p.user.key() == self.user.key():
            db.delete(p)
        self.redirect('/blog/')
