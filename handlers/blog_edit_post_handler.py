from handlers.blog_handler import BlogHandler
from google.appengine.ext import db

from models.blog_post import BlogPost


class BlogEditPostHandler(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('BlogPost', int(post_id), parent=self.blog_key())
        p = db.get(key)

        if self.user.key() == p.user.key():
            self.render("edit-post.html", subject=p.subject,
                        content=p.content)
        else:
            self.redirect("/login")

    def post(self, post_id):
        self.redirect('/blog')
        if not self.user:
            self.redirect('/blog')

        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            key = db.Key.from_path('BlogPost', int(post_id),
                                   parent=self.blog_key())
            p = db.get(key)
            p.subject = subject
            p.content = content
            p.put()
            self.redirect('/blog/%s' % str(p.key().id()))
        else:
            error = "subject and content, please!"
            self.render("edit-post.html", subject=subject, content=content,
                        error=error)
