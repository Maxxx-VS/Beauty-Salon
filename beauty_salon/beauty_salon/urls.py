from django.contrib import admin
from django.urls import path, re_path, include
from masters import views

product_patterns = [
    path("", views.products),
    path("nails", views.nails, name='nails'),
    path("hairs", views.hairs, name='hairs'),
    path("eyelashes", views.eyelashes, name='eyelashes'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('products/', include(product_patterns)),
]
