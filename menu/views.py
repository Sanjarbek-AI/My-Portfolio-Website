from django.views.generic import ListView, TemplateView, DetailView

from menu.models import CourseModel


class CourseListView(ListView):
    template_name = 'layouts/courses.html'

    def get_queryset(self):
        return CourseModel.objects.all()


class CourseDetailView(DetailView):
    model = CourseModel
    template_name = 'layouts/course-detail.html'
