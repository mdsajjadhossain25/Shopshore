from django.shortcuts import render
from store.models import Product, ReviewRating, Promotion_banner

# Create your views here.
def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('-created_date')
    
    banner_products = Product.objects.all().filter(is_banner=True).order_by('-created_date')
    promotion_banner = Promotion_banner.objects.all().filter(is_active=True).order_by('-created_date')
    
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
        
    context = {'products':products, 'reviews':reviews, 'banner_products':banner_products,'promotion_banner':promotion_banner,}
    
    return render(request, 'home.html', context)