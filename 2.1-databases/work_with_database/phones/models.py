from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True)
    price = models.IntegerField(null=True)
    image = models.CharField(max_length=300, null=True)
    release_date = models.CharField(max_length=50, null=True)
    lte_exists = models.BooleanField(null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)
