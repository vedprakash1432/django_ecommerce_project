# from django.http.response import HttpResponse
# from django.shortcuts import render
# from django.shortcuts import get_object_or_404, render
# from .models import Category, product
# def product_list(request, category_slug=None):
#     category = None
#     categories = category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category,slug=category_slug)
#         products = products.filter(category=category)
#     return render(request,
#                   'shop/product/list.html',
#                   {'categories': category,
#                   'categories':categories,
#                   'products': products})
# def product_detail(request, id, slug):
#     product = get_object_or_404(Product,
#                                 id=id,
#                                 slug=slug,
#                                 available=True)
#     return render(request,
#                   'shop/product/detail/html',
#                    {'product': product })
# def product_detail(request, id, slug):
#     product = get_object_or_404(Product,
#                                 id=id,
#                                 slug=slug,
#                                 available=True)
#     return render(request,
#                   'shop/product/detail.html',
#                    {'product':product})

# def homePage(request):
#     return render(request,"index.html")

# def home(request):
#     return HttpResponse('<b><h1>Hello Ramesh</h1></b>')
# def about(request):
#     return HttpResponse('<b><h1>My name is Ramesh Jaiswal. I am a student of BCA. This is my third year, and I want to become a FULL STACK DEVELOPER.</h1></b>') 