from django.urls import path
from my_app import views

#template tagging
app_name = 'my_ap'

urlpatterns = [
    path('relative/', views.relative, name = 'relative'),
    path('other/',views.other, name = 'other'),
]
