from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('getproducts',views.getproducts),
    # path('getproductbycategory',views.GetProductsInCategorie),
    path('getcategories',views.getcategories),
    path('postproduct',views.getcategories),
    path('products',views.products),
    path('products/<int:id>',views.product_detail),
    path('Commandes/<int:id>',views.command_detail),
    path('users',views.users),
    path('LignesCommandes',views.LignesCommandes),
    path('Commandes',views.Commandes),
    path('Payments',views.Payments),
    path('users/<int:id>',views.command_by_user),
    # path('commande_detail/<int:id_command,int:id_book>',views.commande_detail),
    
    
    # path('images/<int:id>',views.images)
    
]

