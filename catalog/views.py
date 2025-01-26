from operator import index

from django.http import HttpResponse
from .models import Product
from django.views.generic import ListView, DetailView, TemplateView
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


class ProductDetailView(DetailView):
    model = Product


class BaseTemplateView(TemplateView):
    template_name = "base.html"

index_view = BaseTemplateView.as_view()
