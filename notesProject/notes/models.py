from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True)
	title = models.CharField(max_length = 100, blank = True, default = "")
	description = models.CharField(max_length = 1000, blank = True, default = "")
	time = models.DateTimeField(default = datetime.now())
	tag = models.CharField(max_length = 100, blank = True, default = "")

	def __str__(self):
		return self.title

	# def get_absolute_url(self):
	# 	return reverse(notes:, kwargs = {"pk": self.id})

