from django.test import Client, TestCase
from django.urls import reverse, resolve
from .models import Post, User
from .views import index,login_view,logout_view,register
import unittest


##Tesing Models
class PostTestCase(TestCase):
  def setUp(self):
   #Creating users
    user1=User.objects.create(username="ahmed",email="ahmed@gmail.com",password="k22")
    user2=User.objects.create(username="ali",email="ali@gmail.com",password="linux")
    user3=User.objects.create(username="mohamed",email="mohamed@gmail.com",password="windows")
    user4=User.objects.create(username="hosam",email="hosam@gmail.com",password="mac")
   #Creating post

    self.post_1 = Post.objects.create(user=user1,content=" ",likes=3)
    self.post_2 = Post.objects.create(user=user2,content="watch attack on titans guys",likes=0)
    self.post_3 = Post.objects.create(user=user3,content="use signal",likes=-1)
    self.post_4 = Post.objects.create(user=user4,content="nothing to tweet right now",likes=0)
    self.post_5 = Post.objects.create(user=user3,content="ooh i like that ",likes=7)
    self.post_6 = Post.objects.create(user=user2,content="Elon musk is great !",likes=1)
    self.post_7 = Post.objects.create(user=user1,content="Watch death note guys",likes=10)
    self.post_8 = Post.objects.create(user=user4,content="",likes=-5)
    self.post_9 = Post.objects.create(user=user4,content="&*",likes=5)
    self.post_10 = Post.objects.create(user=user4,content="make me cry ! ",likes=-3)
    

#1
  def test_posts_count(self):
    c= Client()
    Posts = c.get("/")
    self.assertEqual(Posts.context["posts"].count(),10)
#2
  def test_PostValidation_False(self):
    self.assertFalse(self.post_1.Valid_Post())
    self.assertFalse(self.post_3.Valid_Post())
    self.assertFalse(self.post_8.Valid_Post())
    self.assertFalse(self.post_9.Valid_Post())
    self.assertFalse(self.post_10.Valid_Post())
   
#3
  def test_PostValidation_True(self):
    self.assertTrue(self.post_2.Valid_Post())
    self.assertTrue(self.post_4.Valid_Post())
    self.assertTrue(self.post_5.Valid_Post())
    self.assertTrue(self.post_6.Valid_Post())
    self.assertTrue(self.post_7.Valid_Post())
#4
  def test_Post_content_and_likes(self):
    first_post = Post.objects.get(id=1)
    first_post_content = first_post.content
    first_post_likes = first_post.likes

    self.assertEqual(first_post_content," ")
    self.assertEqual(first_post_likes,3)
    
    


#----------------------------------------------------------------------------------------------------------


##testing all the urls paths
class Test_Url(TestCase):
  def setUp(self):
    self.client = Client()
#5
  def test_Url(self):
    c= Client()
    home = c.get('/')
    error = c.get("/error")
    login = c.get("/login")
    logout= c.get("/logout")
    register= c.get("/register")
  #Asserting the urls are  :  
    self.assertEqual(error.status_code,404)
    self.assertEqual(login.status_code,200)
    self.assertEqual(logout.status_code,302)
    self.assertEqual(register.status_code,200)
    self.assertEqual(home.status_code,200)
  #Assertin the templates are indeed used 
    self.assertTemplateUsed(home,'network/index.html')
    self.assertTemplateUsed(login,'network/login.html')
    self.assertTemplateUsed(register,'network/register.html')
    

#Tesing resolving of the views :   
#6
  def test_resolving(self):
    index_viewed = resolve(reverse('index'))
    logout_viewed = resolve(reverse('logout'))
    login_viewed = resolve(reverse('login'))
    register_viewed = resolve(reverse('register'))

    self.assertEqual(index_viewed.func,index)
    self.assertEqual(logout_viewed.func,logout_view)
    self.assertEqual(login_viewed.func,login_view)
    self.assertEqual(register_viewed.func,register)


#Test Posting data   

  

    
   




  