from django.conf import settings
from apps.post.models import Post
from django.db import models


User = settings.AUTH_USER_MODEL


class Report(models.Model):

	user 		= models.ForeignKey(to=User,related_name='report_by',on_delete=models.CASCADE)
	post 		= models.ForeignKey(to=Post,related_name='reports',on_delete=models.CASCADE)
	status 		= models.CharField(max_length=35,blank=False)

	created		= models.DateTimeField(auto_now_add=True)


	class Meta:
		unique_together 	= (('user','post'),)
		ordering			= ('-created',)
		verbose_name		= 'Report'
		verbose_name_plural = 'Reports'


	def __str__(self):
		return "{0} reported on {1}".format(self.user.username,self.post.title)
