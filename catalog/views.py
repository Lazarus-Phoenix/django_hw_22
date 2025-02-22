import logger
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
)
from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from .forms import ProductForm, ProductModeratorForm
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache


class HomeView(TemplateView):
    template_name = "home.html"


class ContactTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Контакты"
        return context

@method_decorator(cache_page(60*15), name='dispatch')
class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "product"

    # def get_queryset(self):
    #     return Product.objects.filter(published=True)

@method_decorator(cache_page(60*15), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_create.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        product = form.save(commit=False)  # Создаем продукт, но не сохраняем в БД
        product.published = True  # Устанавливаем статус опубликованного
        user = self.request.user  # Получаем текущего пользователя
        product.owner = user  # Привязываем пользователя как владельца
        product.save()  # Сохраняем продукт в БД
        return super().form_valid(form)  # Вызываем родительский метод

class ProductUpdateView(LoginRequiredMixin,UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_update.html"
    # success_url = reverse_lazy("catalog:product_detail")

    def get_success_url(self):
        try:
            return reverse('catalog:product_detail', args=[self.object.pk])
        except Exception as e:
            # Логирование ошибки
            logger.error(f"Error in get_success_url:{str(e)}")
            return reverse('catalog:products_list')

    def get_form_class(self):
        user = self.request.user
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm

        return ProductForm



class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_delete_confirm.html"
    pk_url_kwarg = 'catalog_product_id'

    def post(self, request, catalog_product_id):
        product = get_object_or_404(Product, id=catalog_product_id)
        if not request.user.has_perm('catalog.can_delete_product'):
            return HttpResponseForbidden("У вас нет прав для удаления продукта.")
        product.delete()
        return redirect('catalog:product_list')

    # permission_classes = 'catalog.can_delete_product'
    # # success_url = reverse_lazy("catalog:product_detail")
    #
    # def get_success_url(self):
    #     return reverse_lazy("catalog:product_list")



class BaseTemplateView(TemplateView):
    template_name = "base.html"


index_view = BaseTemplateView.as_view()
