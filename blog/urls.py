from django.urls import path
from blog.views import post_details, render_posts

app_name = 'blog'

urlpatterns = [
    path('', render_posts, name='posts'),
    path('<int:post_id>', post_details, name="post_details")
]
