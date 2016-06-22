import webapp2
from google.appengine.ext import db

from handlers.blog_delete_post_handler import BlogDeletePostHandler
from handlers.blog_edit_post_handler import BlogEditPostHandler
from handlers.blog_front_handler import BlogFront
from handlers.blog_handler import BlogHandler
from handlers.blog_like_post_handler import BlogLikePostHandler
from handlers.blog_new_post_handler import BlogNewPostHandler
from handlers.blog_signup_handler import BlogSignupHandler
from handlers.blog_login_handler import BlogLoginHandler
from handlers.blog_logout_handler import BlogLogoutHandler


class BlogPostPage(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('BlogPost', int(post_id), parent=self.blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return

        self.render("permalink.html", post=post)


app = webapp2.WSGIApplication([('/', BlogFront),
                               ('/blog/?', BlogFront),
                               ('/blog/([0-9]+)', BlogPostPage),
                               ('/edit/([0-9]+)', BlogEditPostHandler),
                               ('/like/([0-9]+)', BlogLikePostHandler),
                               ('/delete/([0-9]+)', BlogDeletePostHandler),
                               ('/blog/newpost', BlogNewPostHandler),
                               ('/signup', BlogSignupHandler),
                               ('/login', BlogLoginHandler),
                               ('/logout', BlogLogoutHandler)
                               ],
                              debug=True)
