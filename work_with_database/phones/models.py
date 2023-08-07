from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify 

class Phone(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=150)
    price = models.CharField(max_length=7)
    release_date = models.CharField(max_length=10)
    lte_exists = models.CharField(max_length=5)
    slug = models.SlugField()

    
    
    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)