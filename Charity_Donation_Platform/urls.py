
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('faq/', include('FAQ.urls')),
    path('', include('blog.urls')),
    path('', include('events.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('', include('about.urls')),


    path('', include('user_app.urls')),

    path('', include('user_app.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
