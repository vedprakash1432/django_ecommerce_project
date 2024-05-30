"""djangoofflineproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import include, url
# from shop.views import hello,home,about,service,hello1,hello2,hello3,hello4,hello5,hello6,hello7,hello8
# from shop.views import hello9,hello10,Name


urlpatterns = [
     path('admin/', admin.site.urls),
     path('',include('shop.urls',namespace='shop')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


    #  url('admin/',admin.site.urls),
    #  url(r'^hello$',hello),
    #  url(r'^about',about),
    #  url(r'service',service),

    # url(r'^hello/.$',hello1),
    # url(r'^hello/.+$',hello1),
    # url(r'^hello/\d$',hello1),
    # url(r'^hello/\d*$',hello1),
    # url(r'^hello/[a-z]$',hello1),
    # url(r'^hello/[A-Z]$',hello1),
    # url(r'hello/[A-Z]+$',hello1),
    # url(r'hello/[a-z]+$',hello1),
    # url(r'^hello/[A-Z]+$',hello1),
    # url(r'^hello/[a-zA-Z]+$',hello1),    # SAME WORKING
    #  url(r'^hello/[A-Za-z]+$',hello1),    # SAME WORKING
    # url(r'^hello/[A-Z][a-z]+$',hello1),  # SAME WORKING

    #BY ME 
    #url(r'^hello/.$',hello1),            #Any single charactor, disit, special symbol
    #url(r'^hello/\d$',hello2),           #Only single disit
    #url(r'^hello/[A-Z]$',hello3),        #Any upper case only 
    #url(r'^hello/[a-z]$',hello4),        #Any lover case only
    #url(r'^hello/[A-Za-z]$',hello5),     #single charactor uppper and lover
    #url(r'^hello/\d+$',hello6),          #multiple disits 
    #url(r'^hello/[^/]+$',hello7),        #until use forward slas (/)  
    #url(r'^hello/\d?$',hello8),          #zero or one only disit not multiple disits
    #url(r'^hello/\d*$',hello9),          #zero, one, and more disits 
    #url(r'^hello/\d{1,5}$',hello10),     #between one and five only disits 
    #url('Name', Name),

# ]


# def Datetime(request):
#     current_datetime = datetime.datetime.now()  
#     html = "<html><body><b>Current Date and Time Value:</b> %s</body></html>" % current_datetime
#     return HttpResponse(html)