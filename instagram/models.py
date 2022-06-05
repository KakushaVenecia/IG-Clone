from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete


# Creating and uploading details of a user to their own directory 
def user_directory_path(instance,filename):
    return 'user_{0},{1}'.format(instance.user.id, filename)



# Create your models here.
class Image(models.Model):
    image=models.ImageField(upload_to=user_directory_path , verbose_name="image", null=False)
    image_name=models.CharField(max_length =30)
    image_caption=models.CharField(max_length =250000)
    posted=models.DateTimeField(auto_now_add=True)
    profile=models.ForeignKey(User, on_delete=models.CASCADE)
    likes=models.IntegerField(default=0)
    comments=models.CharField(max_length =250000)

    def __str__(self):
        return self.image_name

class Follow(models.Model):
    follower=models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    following=models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")

class Myprofile(models.Model):
    image=models.ImageField(upload_to=user_directory_path , verbose_name="image", null=False)
    bio=models.CharField(max_length =160)
    


class Stream(models.Model):
    following=models.ForeignKey(User, on_delete=models.CASCADE, related_name="stream_following")
    profile=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ForeignKey(Image, on_delete=models.CASCADE , null=False)
    date=models.DateTimeField()

    def add_stream(sender, instance):
        image = instance
        profile = image.profile
        followers=Follow.objects.all().filter(following=profile)
        for follower in followers:
            stream=Stream(image=image, user=follower.follower, date=image.posted, following=profile)
            stream.save()

# post_save.connect(Stream.add_stream, sender=Image)


