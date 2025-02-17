from django.urls import path
from catalog.apps import CatalogConfig
from . import views
from .views import ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', views.ContactTemplateView.as_view(), name='contacts'),
    path('', views.ProductListView.as_view(), name="product_list"),
    path('product/<int:pk>/',views.ProductDetailView.as_view(), name="product_detail"),
    path('add_product/', views.ProductCreateView.as_view(), name='add_product'),
    path('edit_product/<int:pk>', views.ProductUpdateView.as_view(), name='edit_product'),

    path('product/<int:catalog_product_id>/delete/', views.ProductDeleteView.as_view(), name='delete_product'),
    path('catalog/<int:owner_id>/', ProductListView.as_view(), name='user_catalog')

]
