from django.db import models


class Category(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="cat_imgs/")

    def __str__(self):
        return self.title


class Size(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="product_imgs/")
    slug=models.CharField(max_length=400)
    detail=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ProductAttribute(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    price=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product.title
