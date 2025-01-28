from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ContactTemplateView, ProductDetailView, ProductListView


app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
    path('', ProductListView.as_view(), name="product_list"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product_detail")
]
