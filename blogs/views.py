from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blogs.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin



class PostListView(ListView):
    model = Post
    template_name = 'blogs/post_list.html'
    context_object_name = 'posts'
    paginate_by = 3  # Количество постов на странице
    ordering = ['-created_at']  # Сортировка постов по дате создания в обратном порядке

    def get_queryset(self):  # фильтрация постов по опубликованным
        return Post.objects.filter(published=True)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogs/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):  # увеличение счетчика просмотров
        post = super().get_object()
        post.views_count += 1
        post.save()
        return post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'preview']
    template_name = 'blogs/post_form.html'
    success_url = reverse_lazy('blogs:home')

    def form_valid(self, form): # изменение флага состояния при сохранении
        post = form.save(commit=True)
        post.published = True
        post.save()
        return super().form_valid(form)



class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'preview']
    template_name = 'blogs/post_form.html'
    success_url = reverse_lazy('blogs:post_detail') # используем параметр success_url

    def get_success_url(self):
        post = self.get_object()
        return reverse_lazy('blogs:post_detail', kwargs={'pk': post.pk})

    def form_valid(self, form):
        post = form.save(commit=True)
        post.published = True
        post.save()
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blogs/post_delete_confirm.html'
    success_url = reverse_lazy('blogs:home')
    context_object_name = 'post'
