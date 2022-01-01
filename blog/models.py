from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    STATUS_CHOICES=(
        ('draft','Draft'),
        ('published','Published')
    )
    title=models.CharField(max_length=300)
    slug=models.SlugField(max_length=250,unique_for_date='publish')