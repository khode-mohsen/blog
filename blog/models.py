from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import reverse
from ckeditor.fields import RichTextField


class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	email=models.EmailField()
	phone=models.CharField(max_length=13)
	avatar=models.ImageField(blank=True)
	def __str__(self):
		return self.email
		
class BlogPost(models.Model):
	photo=models.ImageField(upload_to='ig/',blank=True)
	author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	date=models.DateField(auto_now_add=True)
	title=models.CharField(max_length=180)
	content=models.TextField()
#	def get_absolute_utl(self):
#		return reverse('blog:detail',kwargs={'id':self.id})
	def __str__(self):
		return self.title
		
class BlogComment(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)
	date=models.DateTimeField(auto_now_add=True)
	comment=RichTextField()
	def __str__(self):
		return self.comment
