from mongoengine import *
import datetime 

class Comment(EmbeddedDocument):
    author=StringField(required=True,default="Anonymous")
    link=URLField()
    content=StringField(required=True)
    date=DateTimeField(required=True,default=datetime.datetime.now)


# define data structure
class BlogPost(Document):
    title = StringField(required=True)
    content = StringField(required=True)
    author = StringField(required=True)
    date = DateTimeField(required=True, default=datetime.datetime.now)
    categories = ListField(StringField(max_length=30))
    comments=ListField(EmbeddedDocumentField(Comment))


connect('blog_example')
post = BlogPost()
post.title="Post"
post.content = "I think W Y Z IS AWESOME"
post.author = "Jessie Leung"
post.save()

posts= BlogPost.objects() #everything 
posts= BlogPost.objects(author='Jessie Leung') # my blog post 
post = posts.first()
print('"%s", by "%s": %s' % (post.title, post.author, post.content))

# update my blog post
post.title = "I love food"
post.save()

# verify update
print(BlogPost.objects().first().title)

# add comments 
comment=Comment()
comment.content = "I LOVE FOOD TOO"
post.comments.append(comment)
post.save()

comment = Comment()
comment.author = "Mr. I think I'm So Awesome"
comment.content= "Food is not so great sometimes...."
comment.link = "http://google.com"
post.comments.append(comment)
post.save()

print "Before comments"
# Retrieve a post
posts = BlogPost.objects()
post = posts.first()

print('"%s", by "%s": %s' % (post.title, post.author, post.content))
for comment in post.comments:
    if comment.link is not None:
        print('Comment by %s (%s): %s' % (comment.author, comment.link, comment.content))
    else:
        print('Comment by %s: %s' % (comment.author, comment.content))