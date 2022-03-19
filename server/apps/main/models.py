import textwrap
from typing import Final, final

from django.db import models
from django.urls import reverse

#: That's how constants should be defined.
_POST_TITLE_MAX_LENGTH: Final = 80


@final

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    class Product(models.Model):
        product_name = models.CharField('Название товара', max_length=50)
        category = models.ForeignKey('Categories', on_delete=models.CASCADE)
        description = models.CharField('Описание ', max_length=1000)
        specification = models.CharField('Характеристики', max_length=500)
        image = models.ImageField(upload_to='images/')
        price = models.DecimalField(max_digits=7, decimal_places=2)
        in_stock = models.BooleanField(default=True)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        slug = models.SlugField(max_length=255)
        is_active = models.BooleanField(default=True)


        class Meta:
            verbose_name_plural = 'Products'
            ordering = ('-created',)



    def __str__(self):
        return self.title



