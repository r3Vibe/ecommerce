from django.urls import path
from .views import register_user, login_user, logout_user, forgot_password, reset_password, activate_account, reset_password_verify

app_name = 'customAuth'


urlpatterns = [
    path('register/', register_user, name='register'),
    path('signin/', login_user, name='signin'),
    path('signout/', logout_user, name='signout'),
    path('forgot-password/', forgot_password, name='forgot-password'),
    path('reset-password/', reset_password, name='reset-password'),
    path('activate/<uidb64>/<token>/', activate_account, name='activate'),
    path('verify/<uidb64>/<token>/', reset_password_verify, name='verify'),
]
