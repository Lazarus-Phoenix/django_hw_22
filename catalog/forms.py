from django import forms
from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError
from django.conf import settings

from catalog.models import Product


def validate_forbidden_words(value):
    forbidden_words = getattr(settings, "FORBIDDEN_WORDS", [])
    value_lower = value.lower()
    for word in forbidden_words:
        if word in value_lower:
            raise ValidationError(f'Использование слова "{word}" запрещено.')


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class ProductModeratorForm(FormStyleMixin, ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['created_at', 'updated_at', "owner"]

    def clean_purchase_price(self):
        price = self.cleaned_data.get("purchase_price")
        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной")
        return price

    def clean_name(self):
        name = self.cleaned_data.get("name")
        validate_forbidden_words(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        validate_forbidden_words(description)
        return description



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "purchase_price"]

    def clean_purchase_price(self):
        price = self.cleaned_data.get("purchase_price")
        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной")
        return price

    def clean_name(self):
        name = self.cleaned_data.get("name")
        validate_forbidden_words(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        validate_forbidden_words(description)
        return description

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs.update({"class": "form-check-input"})
            else:
                field.widget.attrs.update({"class": "form-control"})
