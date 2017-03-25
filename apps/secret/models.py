from __future__ import unicode_literals

from django.db import models
from ..login_reg.models import User
class UserManager(models.Manager):
	def get_info(self,info,id):
		self.create(comment=info['description'], user_id=id)

	def like(self,var,id):
		users_id=User.objects.get(id=var)
		comments_id=Comment.objects.get(id=id)
		comments_id.users_comment.add(users_id)

class Comment(models.Model):
	comment=models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	user_id=models.ForeignKey(User, related_name="comm")
	users_comment=models.ManyToManyField(User, related_name="something")	
	objects=UserManager()
