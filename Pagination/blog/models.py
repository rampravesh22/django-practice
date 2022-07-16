from django.db import models
from django.urls import reverse

# Create your models here.



class Blog(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    publish_date = models.DateField(auto_now_add=True)
    
    def get_absolute_url(self):
        print(self.title)
        return reverse("create",kwargs={"name":"Rampravesh"})
    
    