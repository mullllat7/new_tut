from django.db import models

# from app.category.utils import slug_generator


class Category(models.Model):
    title = models.CharField(max_length=100, primary_key=True,unique=True,blank=True,)
    def __str__(self):
        return self.title


class CategoryImage(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_image')
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.category.title

