from django.urls import path
from accounts import views


urlpatterns = [

    path('login/', views.LoginScreen.as_view(), name = 'LoginScreen'),
    path('register/', views.RegisterScreen.as_view(), name = 'RegisterScreen'),
    path('AdminLogoutView/', views.AdminLogoutView.as_view(), name = 'AdminLogoutView'),

]