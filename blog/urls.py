
from django.urls import path, include
# from . import views
from.views import BlogView, BlogDetailed
urlpatterns = [
    # path('blog/', views.blog, name = "Blog"),
    path('blog/', BlogView.as_view(), name = "Blog"),
    path('blog_details/<int:pk>', BlogDetailed.as_view(), name = "Blog-Detail")
]