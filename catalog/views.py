from django.views.generic import ListView, DetailView, TemplateView,CreateView,UpdateView,DeleteView


from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ProductForm
from .models import Product


def product_form_view(request, template_name, form_class, success_url):
    if request.method == "POST":
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class()

    return render(request, template_name, {'form': form})


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
    template_name = 'catalog/product_create.html'
    success_url = reverse_lazy('catalog:product_list')



    # def create_product(request):
    #     if request.method == 'POST':
    #         form = ProductForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('catalog/product_list.html')
    #     else:
    #         form = ProductForm()
    #     return render(request, 'product_create.html', {'form': form})


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_update.html'
    success_url = reverse_lazy('catalog:product_detail')

    # def form_valid(self, form):
    #     product = form.save(commit=False)
    #     product.published = True
    #     product.save()
    #     return super().form_valid(form)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_delete_confirm.html'
    success_url = reverse_lazy('catalog:product_detail')

    def get_success_url(self):
        return reverse_lazy('catalog:product_list')

class BaseTemplateView(TemplateView):
    template_name = "base.html"

index_view = BaseTemplateView.as_view()
