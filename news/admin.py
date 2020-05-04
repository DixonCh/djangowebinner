from django.contrib import admin
from .models import Category,News
# Register your models here.
a = [Category,News]
admin.site.register(a)

