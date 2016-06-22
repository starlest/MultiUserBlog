from handlers.blog_handler import BlogHandler
from models.blog_post import BlogPost
from google.appengine.ext import db


class BlogFront(BlogHandler):
    def get(self):
        posts = BlogPost.all().order('-created')
        for post in posts:
            print post.key().id
        self.render('blog-front.html', posts=posts)
