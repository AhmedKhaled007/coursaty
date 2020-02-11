from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.


# user - title - img - content =- created 


class Post(models.Model):
    
    user = models.ForeignKey(User , on_delete=models.CASCADE) # foreign key related with django user
    title = models.CharField(max_length=50)
    content = models.TextField(default=' ')
    img =  models.ImageField(upload_to='post_img/', blank=True)
    created = models.DateTimeField(default=datetime.datetime.now())

    # objects = models.Manager()
    


    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User , related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    reply = models.TextField(default=' ')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.reply,self.user)
    
