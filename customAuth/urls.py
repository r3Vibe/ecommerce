from django.urls import path
from .views import register_user, login_user, logout_user

app_name = 'customAuth'


urlpatterns = [
    path('register/', register_user, name='register'),
    path('signin/', login_user, name='signin'),
    path('signout/', logout_user, name='signout'),
]
