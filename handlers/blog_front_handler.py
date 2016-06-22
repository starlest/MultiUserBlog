from handlers.blog_handler import BlogHandler
from models.blog_post import BlogPost
from google.appengine.ext import db


class BlogFront(BlogHandler):
    def get(self):
        posts = BlogPost.all().order('-created')
        self.render('blog-front.html', posts=posts)
