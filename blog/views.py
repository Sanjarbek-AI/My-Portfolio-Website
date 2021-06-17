from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from blog.forms import CommentModelForm
from blog.models import BlogModel


class BlogListView(ListView):
    template_name = 'blog.html'
    paginate_by = 1

    def get_queryset(self):
        qs = BlogModel.objects.order_by('-pk')
        q = self.request.GET.get('q')
        tag = self.request.GET.get('tag')
        if q:
            qs = qs.filter(title__icontains=q)
        if tag:
            qs = qs.filter(tags__name__icontains=tag)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_blogs'] = BlogModel.objects.order_by('-pk')[:3]

        return context


class BlogDetailView(DetailView):
    template_name = 'blog-details.html'
    model = BlogModel


class CommentCreateView(CreateView):
    form_class = CommentModelForm

    def form_valid(self, form):
        form.instance.blog = get_object_or_404(BlogModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'pk': self.kwargs.get('pk')})
