from django.urls import path
from .import views




app_name = 'comment'

urlpatterns = [
    path('add/',views.comment_add,name='comment-add'),
    path('remove/',views.comment_remove,name='comment-remove'),
]

