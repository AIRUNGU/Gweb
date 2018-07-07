from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
import datetime


class BaseContent(models.Model):
	title = models.CharField(max_length=150)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True



class Category(BaseContent):
	name = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = 'Categorys'

	def __str__(self):
		return self.title

class Articles(BaseContent):
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	body = models.TextField()
	published = models.BooleanField(default=False)
	Draft = models.BooleanField(default=True)
	

	class Meta:
		ordering = ['-created']
		verbose_name_plural = 'Articles'

	def __str__(self):
		return self.title

class Event(BaseContent):
	activityname = models.CharField(max_length=500)
	meetingdate = models.DateField()
	meetingtime = models.TimeField()
	description = models.TextField()
	deperturevenue = models.CharField(max_length=300)
	# location = models.PointField(srid=4326)

	class Meta:
		ordering = ['-created']
		verbose_name_plural = 'Events'

	def __str__(self):
		return self.title

class Announcements(BaseContent):
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	description = models.CharField(max_length=200)

	class Meta:
		ordering = ['-created']
		verbose_name_plural = 'Announcements'

	def __str__(self):
		return self.description
	
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=1000, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	email_confirmed = models.BooleanField(default=False)
	image = models.ImageField(upload_to='Profile/%y/%m/%d', blank=True)

	class Meta:
		verbose_name_plural = 'Profiles'

	def __str__(self):
		return self.user

@receiver(post_save, sender=User)
def update_user_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)
		instance.profile.save()