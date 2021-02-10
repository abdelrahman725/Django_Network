from django.contrib import admin
from .models import *

# Register your models here.


class User_info(admin.ModelAdmin):
  list_display=("id","username","email")

class Post_info(admin.ModelAdmin): 
  list_display=("id","user","likes","content","time")

admin.site.register(User,User_info)
admin.site.register(Post,Post_info)




