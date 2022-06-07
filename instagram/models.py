from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete


from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    name=models.CharField(blank=True,max_length=120)
    profile_pic=models.ImageField(upload_to='pictures/',default='default.png')
    bio=models.TextField(max_length=400,blank=True)
    location=models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE,  related_name='profile')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()  

    @classmethod
    def update_bio(cls,id,bio):
        update_profile = cls.object.filter(id=id).update(bio=bio) 
        return update_profile 

    @classmethod
    def search_profile(cls,search_term) :
        profiles=cls.objects.filter(user__username__icontains=search_term) 
        return profiles 
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()         

class Post(models.Model):
    image_post=models.ImageField(upload_to='posts/')
    name= models.CharField(max_length=250,blank=True)
    caption= models.CharField(max_length=250,blank=True)
    created_at=models.DateField(auto_now_add=True, null=True)
    liked = models.ManyToManyField(User, related_name='likes', blank=True, )
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='images', null=True)
    class Meta:
        '''
        Class method to display images by date published
        '''
        ordering = ['created_at']
    
    def save_post(self):
        '''
        Method to save our post
        '''
        self.save()

    def delete_post(self):
        '''
        Method to delete our post
        '''
        self.delete()    

    def __str__(self):
        return self.name
    @property
    def num_liked(self):
        return self.liked.all().count()

    @classmethod
    def update_caption(cls, self, caption):
        update_cap = cls.objects.filter(id = id).update(caption = caption)
        return update_cap    

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null = True)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10, null = True)

    def __str__(self):
        return self.post    

class Comment(models.Model):
    comment=models.TextField()
    created=models.DateField(auto_now_add=True,null=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='comments')
    
    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(post__id=id)
        return comments

    def __str__(self):
        return self.comment

class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'
      