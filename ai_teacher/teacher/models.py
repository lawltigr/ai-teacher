from django.db import models

class TeachingStyle(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    avatar = models.ImageField(upload_to='avatars/')
    prompt_template = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
