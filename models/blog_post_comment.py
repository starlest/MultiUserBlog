from google.appengine.ext import db

from handlers import blog_handler
from models.user import User


# noinspection PyAttributeOutsideInit
class BlogPostComment(db.Model):
    content = db.TextProperty(required=True)
    user = db.ReferenceProperty(User, collection_name="BlogPostComments")

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return blog_handler.render_str("post-comment.html", c=self)
