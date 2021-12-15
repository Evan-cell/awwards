from django.urls import path
from .import views


#urls
urlpatterns = [
    path('',views.loginPage, name="login"),
    path('register/',views.registerPage, name="register"),
    path('awwards/', views.awwards, name='awwards'),
]