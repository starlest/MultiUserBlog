from handlers.blog_handler import BlogHandler
from google.appengine.ext import db


class BlogLikePostHandler(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('BlogPost', int(post_id),
                               parent=self.blog_key())
        p = db.get(key)
        if p.user.key() != self.user.key() and p.key() not in \
                self.user.liked_posts:
            p.likes += 1
            self.user.liked_posts.append(p.key())
            self.user.put()
            p.put()
        self.redirect('/blog/')
