from django.urls import path

from menu.views import CourseListView, CourseDetailView

app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='list'),
    path('detail/<int:pk>/', CourseDetailView.as_view(), name='detail'),
]
