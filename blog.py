import webapp2

from handlers.blog_delete_post_handler import BlogDeletePostHandler
from handlers.blog_edit_post_handler import BlogEditPostHandler
from handlers.blog_front_handler import BlogFront
from handlers.blog_like_post_handler import BlogLikePostHandler
from handlers.blog_login_handler import BlogLoginHandler
from handlers.blog_logout_handler import BlogLogoutHandler
from handlers.blog_new_post_handler import BlogNewPostHandler
from handlers.blog_post_delete_comment_handler import \
    BlogPostDeleteCommentHandler
from handlers.blog_post_edit_comment_handler import BlogPostEditCommentHandler
from handlers.blog_post_new_comment_handler import BlogPostNewCommentHandler
from handlers.blog_post_page_handler import BlogPostPageHandler
from handlers.blog_signup_handler import BlogSignupHandler

app = webapp2.WSGIApplication([('/', BlogFront),
                               ('/blog/?', BlogFront),
                               ('/blog/([0-9]+)', BlogPostPageHandler),
                               ('/edit/([0-9]+)', BlogEditPostHandler),
                               ('/like/([0-9]+)', BlogLikePostHandler),
                               ('/deletecomment/([0-9]+[-][0-9]+)',
                                BlogPostDeleteCommentHandler),
                               ('/editcomment/([0-9]+[-][0-9]+)',
                                BlogPostEditCommentHandler),
                               ('/comment/([0-9]+)', BlogPostNewCommentHandler),
                               ('/delete/([0-9]+)', BlogDeletePostHandler),
                               ('/blog/newpost', BlogNewPostHandler),
                               ('/signup', BlogSignupHandler),
                               ('/login', BlogLoginHandler),
                               ('/logout', BlogLogoutHandler)
                               ],
                              debug=True)
