from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    title  = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='news/')
    created_at = models.DateField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table='news'
