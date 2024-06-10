from django.urls import path
from myapp.views import *
from django.urls import path
# from ApiApplication.views import *
from myapp import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    
    path('register', views.Register.as_view(), name='register'),
    path('login/',views.LoginView.as_view(),name="login"),
    path('', views.companyapiview.as_view(), name='company_api_view'),
    path('<int:pk>', views.companyapiview.as_view(), name='company_api_view+ffsfs')
]

# urlpatterns = [
#     path('', views.companyapiview.as_view(), name='company_api_view'),
#     path('<int:pk>', views.companyapiview.as_view(), name='company_api_view+ffsfs'),
# ]