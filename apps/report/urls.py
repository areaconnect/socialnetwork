from django.urls import path
from .import views




app_name = 'report'

urlpatterns = [
    path('create/<str:slug>/',views.report_post,name='report-post'),
]

