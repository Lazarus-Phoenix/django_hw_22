from operator import index

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import ProductForm

from .forms import ProductForm
from .models import Product
from django.views.generic import ListView, DetailView, TemplateView,CreateView,UpdateView,DeleteView
from django.core.mail import send_mail


class HomeView(TemplateView):
    template_name = "home.html"


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    # def post(self, request, *args, **kwargs):
    #     name = request.POST.get('name')
    #     phone = request.POST.get('phone')
    #     message = request.POST.get('message')
    #
    #     subject = f'Обратная связь с сайта: {name}'
    #     body = f'Имя: {name}\nТелефон: {phone}\nСообщение:\n{message}'
    #
    #     sender = 'dmitrij-bezgubov@yandex.ru'  # Замените на реальный email
    #     recipients = ['master1kungfu@gmail.com']  # Замените на реальный email
    #
    #     try:
    #         send_mail(
    #             subject,
    #             body,
    #             sender,
    #             recipients,
    #             fail_silently=False,
    #         )
    #         return HttpResponse('Сообщение отправлено!')
    #     except Exception as e:
    #         return HttpResponse(f'Ошибка при отправке сообщения: {str(e)}')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'product'

    # def get_queryset(self):
    #     return Product.objects.filter(published=True)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm

    # fields = ['name', 'image', 'category', 'purchase_price' ]

    template_name = 'catalog/product_create.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form): # изменение флага состояния при сохранении
        product = form.save(commit=True)
        product.published = True
        product.save()
        return super().form_valid(form)

    def create_product(request):
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('product_list.html')
        else:
            form = ProductForm()
        return render(request, 'product_create.html', {'form': form})


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    # fields = ['name', 'image', 'category', 'purchase_price' ]

    template_name = 'catalog/product_update.html'
    success_url = reverse_lazy('catalog:product_detail')

    def get_success_url(self):
        product = self.get_object()
        return reverse_lazy('catalog:product_detail', kwargs={'pk': product.pk})

    def form_valid(self, form):
        product = form.save(commit=True)
        product.published = True
        product.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_delete_confirm.html'

class BaseTemplateView(TemplateView):
    template_name = "base.html"

index_view = BaseTemplateView.as_view()
