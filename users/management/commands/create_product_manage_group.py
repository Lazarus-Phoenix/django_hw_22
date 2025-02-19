from django.core.management import BaseCommand


from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        products_moderators = Group.objects.create(name='Модератор продуктов')
        add_permission = Permission.objects.get(codename='add_product')
        change_permission = Permission.objects.get(codename='change_product')
        view_permission = Permission.objects.get(codename='view_product')
        delete_permission = Permission.objects.get(codename='delete_product')
        products_moderators.permissions.add(add_permission, change_permission, view_permission, delete_permission)
        self.stdout.write(self.style.SUCCESS('Создана группа "Модератор продуктов".'))
        self.stdout.write(self.style.SUCCESS('Добавлены разрешения к группе.'))
        products_moderators.save()