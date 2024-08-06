from django.db import models

# Create your models here.
class Model(models.Model):
    title = models.Charfield(max_length = 200)
    description = models.TextField()
    
    def __str__(self):
        return self.title