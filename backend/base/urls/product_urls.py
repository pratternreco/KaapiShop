from django.urls import path
from base.views import product_views as views

urlpatterns = [
 
    path('',views.getProducts, name="products"), 

    path('create/',views.createProduct, name="create"),     
    path('<str:pk>',views.getProduct, name="product"),
    
    path('update/<str:pk>/',views.updateProduct, name="product-update"),
    path('delete/<str:pk>/',views.deleteProduct, name="delete"),
]