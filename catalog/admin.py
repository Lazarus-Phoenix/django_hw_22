from django.contrib import admin
from .models import Category, Product

from users.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff', 'date_joined', 'id')
    search_fields = ('email',)
    readonly_fields = ('date_joined', 'last_login')

# admin.site.register(Category)
# admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','id')
