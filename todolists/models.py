from django.db import models

# Create your models here.
	owner = models.CharField(max_length=50)
	title = models.CharField(max_length=200)
	summary = models.TextField()
	date = models.DateField('date published')
	status = models.IntegerField()