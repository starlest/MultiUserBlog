from handlers.blog_handler import BlogHandler
from models.blog_post_comment import BlogPostComment
from google.appengine.ext import db


class BlogPostNewCommentHandler(BlogHandler):
    def get(self, post_id):
        if self.user:
            self.render("post-new-comment.html")
        else:
            self.redirect("/login")

    def post(self, post_id):
        if not self.user:
            self.redirect('/blog')
            return

        content = self.request.get('content')
        key = db.Key.from_path('BlogPost', int(post_id),
                               parent=self.blog_key())
        p = db.get(key)
        if p and content:
            c = BlogPostComment(parent=key, content=content,
                                user=self.user)
            c.put()
            self.redirect('/blog/%s' % str(p.key().id()))
        else:
            error = "content, please!"
            self.render("post-new-comment.html", error=error)

