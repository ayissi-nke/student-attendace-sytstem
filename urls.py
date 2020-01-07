from django.urls import path, re_path
from . import views
app_name = 'account'
urlpatterns = [
    path('attendance/', views.attendance, name="attendance"),
    path('consult/', views.consult, name="consult"),
    re_path(r'^record/(?P<course>.+)/$', views.record, name="record"),
]
