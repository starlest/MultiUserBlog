from google.appengine.ext import db
from handlers import blog_handler
from models.blog_post_comment import BlogPostComment
from models.user import User


# noinspection PyAttributeOutsideInit
class BlogPost(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    likes = db.IntegerProperty(required=True)
    user = db.ReferenceProperty(User, collection_name="BlogPosts")

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        comments = BlogPostComment.all().ancestor(self.key())
        print comments.count()
        return blog_handler.render_str("post.html", p=self,
                                       comments=comments, user=self.user)
