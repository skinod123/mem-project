from django.urls import path

from . import views 

urlpatterns = [
    path('', views.page_indeks, name="blocc"),
    path('<int:index>/', views.index, name='urls-html')
    
]