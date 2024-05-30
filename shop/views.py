from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, product 
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request,
                  'shop/product/list.html',
                  {'category' : category,
                  'categories' : categories,
                  'products' : products})

def product_detail(request, id, slug):
    p = get_object_or_404(product,
                                id=id,
                                slug=slug,
                                available=True)

    return render(request,
                  'shop/product/detail.html',
                  {'product' : p})




# from django.shortcuts import render, get_object_or_404
# from .models import Category, product 
# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)

#     return render(request,
#                   'shop/product/list.html',
#                   {'category' : category,
#                   'categories' : categories,
#                   'products' : products})

# def product_detail(request, id, slug):
#     product = get_object_or_404(product,
#                                  id=id,
#                                  slug=slug,
#                                  available=True)

#     return render(request,
#                   'shop/product/details.html',
#                   {'product' : product})



# def home(request):
    #  return HttpResponse("<html><head><title>home</title><body>This is a home page</body></head></html>") 

#  def contact(request):
#      return HttpResponse("<html><head><title>contact</title><body>This is a contact</body></head></html>")


#  def about(request):
#      return HttpResponse("<html><head><title>about</title><body>This is a about</body></head></html>")

# def hello(request):
#     return HttpResponse("Hello World")

# def home(request):
#     return HttpResponse("This is a home")

# def about(request):
#     return HttpResponse("This is a about")

# def service(request):
#     return HttpResponse("This is a service")

# def hello1(request):
#     return HttpResponse("< url(r'^hello.$',hello1) Any single CHARACTOR or DISIT and special symbbol")

# def hello2(request):
#     return HttpResponse("url(r'^hello/\d$',hello2).")

# def hello3(request):
#     return HttpResponse("r'^hello/[A-Z]$',hello3.")

# def hello4(request):
#     return HttpResponse("r'^hello/[a-z]$',hello4.")

# def hello5(request):
#     return HttpResponse("r'^hello/[A-Za-z]$',hello5.")

# def hello6(request):
#     return HttpResponse("^hello/\d+$',hello6.")

# def hello7(request):
#     return HttpResponse("<H1>r'^hello/[^/]+$',hello7.</H1>")

# def hello8(request):
#     return HttpResponse("<H1>r'^hello/\d?$',hello8.</H1>")

# def hello9(request):
#     return HttpResponse("<H1>r'^hello/\d*$',hello9.</H1>")

# def hello10(request):
#     return HttpResponse("<H1>r'^hello/\d{1,3}$',hello10.</H1>")

# # DYNAMIC VIEWS 

# def Name(request):
#     fn = 'Ramesh'
#     mn = 'Jaiswal'
#     ln = 'GKP'
#     return HttpResponse("<html><body>My full name is : %s %s %s </body></html>" %(fn,mn,ln))






