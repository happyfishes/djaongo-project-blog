from django.urls import path
from blog.views import *

urlpatterns = [
    path('', post_list),
    path('category/<int:category_id>', post_list),
    path('tag/<int:tag_id>', post_list),
    path('post/<int:post_id>', post_detail),

]
