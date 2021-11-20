from django.urls import path,include
from . import views

urlpatterns = [
    # all paths are extending /shop/...
    path('', views.index, name='index'),
    path('support/', views.support, name='support'),
    path('about/',views.about, name='about'),
    path('search/',views.search, name='search'),
    # including request with some data{id} in the path
    path('product/<int:myid>', views.product, name='product'),
    path('tracker/',views.tracker, name='tracker'),
    path('checkout/', views.checkout, name='checkout'),
]
