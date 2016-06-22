from handlers.blog_handler import BlogHandler
from google.appengine.ext import db


class BlogPostDeleteCommentHandler(BlogHandler):
    def get(self, ids):
        post_id = ids.split('-')[0]
        comment_id = ids.split('-')[1]

        post_key = db.Key.from_path('BlogPost', int(post_id),
                                    parent=self.blog_key())
        post = db.get(post_key)

        if not self.user or not post or post.user.key() != self.user.key():
            return self.redirect('/login')

        comment_key = db.Key.from_path('BlogPostComment', int(comment_id),
                                       parent=post_key)
        comment = db.get(comment_key)

        if comment:
            db.delete(comment)

        self.redirect('/blog/%s' % str(post.key().id()))
