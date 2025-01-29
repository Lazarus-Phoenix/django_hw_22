from django.urls import path
from catalog.apps import CatalogConfig
from . import views


app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', views.ContactTemplateView.as_view(), name='contacts'),
    path('', views.ProductListView.as_view(), name="product_list"),
    path('product/<int:pk>/',views.ProductDetailView.as_view(), name="product_detail"),
    path('add_post/', views.ProductCreateView.as_view(), name='add_post'),
    path('edit_post/<int:pk>', views.ProductUpdateView.as_view(), name='edit_post'),
    path('delete_post/<int:pk>', views.ProductDeleteView.as_view(), name='delete_post'),
]
