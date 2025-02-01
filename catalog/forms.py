from django import forms

from catalog.models import Product

from django.core.exceptions import ValidationError

"""
 Валидатор для проверки запрещенных слов
"""
# from django.conf import settings
#
# def validate_forbidden_words(value):
#     forbidden_words = getattr(settings, 'FORBIDDEN_WORDS', [])
#     value_lower = value.lower()
#     for word in forbidden_words:
#         if word in value_lower:
#             raise ValidationError(f' Использование слова "{word}" запрещено.')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'purchase_price']

    # def clean_price(self):
    #     price = self.cleaned_data.get('purchase_price')
    #     if price < 0:
    #         raise forms.ValidationError("Цена не может быть отрицательной.")
    #     return price

    # def save(self, *args, **kwargs):
    #     self.full_clean()  # Вызывает все валидаторы, включая custom clean methods
    #     super().save(*args, **kwargs)