from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls', namespace='contact')),
    path('portfolio/', include('portfolio.urls', namespace='portfolio')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('service/', include('services.urls', namespace='service')),
    path('about/', include('about.urls', namespace='about')),
    path('courses/', include('menu.urls', namespace='courses')),
    path('', include('home.urls', namespace='home')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
