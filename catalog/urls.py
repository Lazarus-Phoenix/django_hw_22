from django.urls import path
from catalog.apps import CatalogConfig
# from . import views
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ContactTemplateView,
    ProductDeleteView, CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
)
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
    path('', ProductListView.as_view(), name="product_list"),
    path('product/<int:pk>/',cache_page(60 * 15)(ProductDetailView.as_view()), name="product_detail"),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('edit_product/<int:pk>', ProductUpdateView.as_view(), name='edit_product'),

    path('product/<int:catalog_product_id>/delete/', ProductDeleteView.as_view(), name='delete_product'),
    path('catalog/<int:owner_id>/', ProductListView.as_view(), name='user_catalog'),

    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('add_category/', CategoryCreateView.as_view(), name='add_category'),
    path('category/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

]
