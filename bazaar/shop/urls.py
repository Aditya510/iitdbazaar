from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    UserProductListView
)
from . import views

urlpatterns = [

    path('', ProductListView.as_view(), name='shop-home'),
    path('user/<str:username>', UserProductListView.as_view(), name='user-Products'),
    path('Product/<int:pk>/', ProductDetailView.as_view(), name='Product-detail'),
    path('Product/new/', ProductCreateView.as_view(), name='Product-create'),
    path('Product/<int:pk>/update/', ProductUpdateView.as_view(), name='Product-update'),
    path('Product/<int:pk>/delete/', ProductDeleteView.as_view(), name='Product-delete'),
    path('about/', views.about, name='shop-about'),
    path('thanks/', views.thanks, name='thanks'),
    path('sendquery/<int:pk>', views.get_query, name='send-query'),

]