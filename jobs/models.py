from django.db import models

class jobs(models.Model):
	titile=models.CharField(max_length=200)
	jdate=models.DateField()
	image=models.ImageField(upload_to='images')
	summary=models.TextField()

	def summ(self):
		return self.summary[:60]

	def __str__(self):
		return self.titile
		


