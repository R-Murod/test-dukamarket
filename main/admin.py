from django.contrib import admin
from .models import *


# Register your models here.

class ProductImages(admin.TabularInline):
    model = ProductImage


class AdditionalInformations(admin.TabularInline):
    model = AdditionalInformation


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductImages, AdditionalInformations)
    list_display = ('product_name', 'categories', 'section')
    list_editable = ('categories', 'section')


admin.site.register(Section)
admin.site.register(Product, ProductAdmin)

admin.site.register(ProductImage)
admin.site.register(AdditionalInformation)
admin.site.register(Slider)
admin.site.register(BannerArea)
admin.site.register(MainCategory)
admin.site.register(Category)
admin.site.register(SubCategory)
