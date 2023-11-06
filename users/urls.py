from django.urls import path
from users.apps import UsersConfig
from users.views import UserAuthenticationView, UserProfileView

app_name = UsersConfig.name


urlpatterns = [
    path('auth/', UserAuthenticationView.as_view(), name='user_authentication'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),


]