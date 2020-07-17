from django.db import models

# Create your models here.

class Blogs(models.Model):
	subject = models.CharField(max_length=200)
	category = models.CharField(max_length=200)
	datetime = models.DateTimeField()
	
	def __str__(self):
		return self.subject

class BlogData(models.Model):
	blogs = models.ForeignKey(Blogs, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	content = models.TextField()
	image = models.ImageField(upload_to='images/', blank=True, null=True)

	def __str__(self):
		return self.title
