from django.urls import path
from .views import stub_view
from .views import list_view
from .views import detail_view
from .views import add_model


urlpatterns = [
    path('', list_view, name="blog_index"),
    path('addpost/', add_model, name="post_add"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
]

