from django.db import models
from django.utils import timezone
from django.urls import reverse


tz = timezone.get_default_timezone()



class News(models.Model):
    title = models.CharField(max_length=150)
    most_important = models.TextField(max_length=255)
    content = models.TextField(blank=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    slug = models.SlugField(null=True, unique=True, max_length=70)

    def get_absolute_url(self):
        return '/news/' + str(self.slug)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-time_create', 'title']


class Accidents(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=False)
    time_create = models.DateField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

