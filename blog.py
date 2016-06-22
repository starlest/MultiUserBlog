import webapp2
from google.appengine.ext import db
from handlers.blog_handler import BlogHandler
from handlers.signup_handler import SignupHandler
from handlers.login_handler import LoginHandler
from handlers.logout_handler import LogoutHandler
from models.blog_post import BlogPost


class MainHandler(BlogHandler):
    def get(self):
        self.render('main.html')


class BlogFront(BlogHandler):
    def get(self):
        posts = BlogPost.all().order('-created')
        self.render('blog-front.html', posts=posts)


class PostPage(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id),
                               parent=BlogHandler.blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return

        self.render("permalink.html", post=post)


class NewPost(BlogHandler):
    def get(self):
        if self.user:
            self.render("newpost.html")
        else:
            self.redirect("/login")

    def post(self):
        if not self.user:
            self.redirect('/blog')

        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            p = BlogPost(parent=BlogHandler.blog_key(), subject=subject,
                         content=content)
            p.put()
            self.redirect('/blog/%s' % str(p.key().id()))
        else:
            error = "subject and content, please!"
            self.render("newpost.html", subject=subject, content=content,
                        error=error)


app = webapp2.WSGIApplication([('/', MainHandler),
                               ('/blog/?', BlogFront),
                               ('/blog/([0-9]+)', PostPage),
                               ('/blog/newpost', NewPost),
                               ('/signup', SignupHandler),
                               ('/login', LoginHandler),
                               ('/logout', LogoutHandler)
                               ],
                              debug=True)
