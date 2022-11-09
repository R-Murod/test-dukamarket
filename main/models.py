from django.db import models


# Create your models here.
class Slider(models.Model):
    DISCOUNT_DEAL = (
        ('Hot Deals', 'Hot Deals'),
        ('New Arraivels', 'New Arraivels'),
    )
    image = models.ImageField(upload_to='upload')
    discount_deal = models.CharField(choices=DISCOUNT_DEAL, max_length=100)
    sale = models.IntegerField(default=0)
    brand_name = models.CharField(max_length=200)
    discount = models.IntegerField(default=0)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.brand_name


class BannerArea(models.Model):
    image = models.ImageField(upload_to='upload')
    discount_deal = models.CharField(max_length=200)
    quote = models.CharField(max_length=200)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.quote


class MainCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.main_category.name + '---' + self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.category.main_category.name + ' ---> ' + self.category.name + ' ---> ' + self.name


class Section(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    total_quantity = models.IntegerField()
    availability = models.IntegerField()
    featured_image = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    price = models.IntegerField()
    discount = models.IntegerField()
    product_information = models.TextField()
    model_name = models.CharField(max_length=200)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.CharField(max_length=200)
    description = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200)


class AdditionalInformation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.CharField(max_length=200)
    detail = models.CharField(max_length=200)
