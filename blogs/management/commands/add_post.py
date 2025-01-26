from django.core.management.base import BaseCommand
from django.core.management import call_command
from blogs.models import Post

class Command(BaseCommand):
    help = 'Load test data from fixture'

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Post.objects.all().delete()


        # Добавляем записи
        call_command('loaddata', 'category_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))

        call_command('loaddata', 'product_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))