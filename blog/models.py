from django.db import models
class blog(models.Model):
	image=models.ImageField(upload_to='images')
	titile=models.CharField(max_length=40)
	summary=models.TextField()

	def __str__(self):
		return self.titile

	def sun(self):
		return self.summary[:200]

