from django.test import TestCase
from .models import *
from django.contrib.auth.models import *
# Create your tests here.

class TestProfileCase(TestCase):
  def setUp(self):
    self.user = User(name='Twiga')
    self.user.save()
    
    self.profile = Profile(id=1, profile_pic='sunrise.jpg',bio='I am Woman',location= 'Nairobi', user=self.user.username)
    
    
  def test_instance(self):
    self.assertTrue(self.profile,Profile)
    
  def test_save_method(self):
    self.profile.save_profile()
    new_object = Profile.objects.all()
    self.assertTrue(len(new_object)>0)
    

    
class TestPostCase(TestCase):
  def setUp(self):
    self.profile = Profile(id=1, photo='sunrise.jpg',bio='I am woman')
    self.profile.save()
    self.user = User(username='Twiga')
    self.user.save()    
    self.post = post_delete(post_image_id=1, name='Island', caption='I am always here', user=self.profile)
  
  def test_instance(self):
    self.assertTrue(isinstance(self.post, Post))
    
  def test_save_method(self):
    self.post.save_post()
    posts = Post.objects.all()
    self.assertTrue(len(posts)>0)
    
  def test_delete_method(self):
    self.post.delete_post()
    new_post = Profile.objects.filter(name=self.name)
    self.assertTrue(len(new_post)<0)
    
  def test_update_caption(self):
    self.post.update_caption()
    new_caption = Post.objects.get(caption='new caption')
    self.post.update_caption(new_caption)

# Create your tests here.
