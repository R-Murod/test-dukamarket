from django.shortcuts import render

# Create your views here.
from main.models import *


def indexHandler(request):
    slider = Slider.objects.all()
    banners = BannerArea.objects.all()
    main_category = MainCategory.objects.all().order_by('-id')
    product = Product.objects.filter(section__name="Top Deals Of The Day")
    return render(request, 'index.html', {
        'slider': slider,
        'banners': banners,
        'main_category': main_category,
        'product': product,
    })
