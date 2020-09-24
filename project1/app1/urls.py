from django.urls import path

from . import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('foods', views.foods, name='foods'),
    path('index', views.index, name='index'),
    path('single.html', views.single, name='single.html'),   #임시로 넣어둠
    path('lifestyle', views.lifestyle, name='lifestyle'),
    path('single', views.single, name='single'),
    
    path('test', views.test, name='test'), #테스트용 url
    
    #path('<int:app1_id>/', views.detail, name='detail'),
]