from django.contrib.auth.models import AbstractUser
from django.db import models
import re
def validate_post(post):
    pattern = re.search(r'\w+',post)
    if pattern:return True
    return False


class User(AbstractUser):
    # creat a post for every user.
    pass


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="post_owner")
    content = models.TextField(blank=False,null=True)
    time = models.CharField (max_length=255,null=True)
    #time = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.content[:13]}... by: ({self.user})"
   
    def Valid_Post(self):
        return validate_post(self.content) and self.likes>=0

    

