from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('designers/', views.designers, name='designers'),
    path('designers/<int:designer_id>', views.designer, name='designer'),
    path('items/', views.ItemListView.as_view(), name='items'),
    path('items/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:item_id>/<int:qty>', views.add_to_cart, name='add_to_cart'),
]