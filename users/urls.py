from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from users.apps import UsersConfig
from users.views import UserAuthenticationView, UserProfileView

app_name = UsersConfig.name


urlpatterns = [
    path('auth/', UserAuthenticationView.as_view(), name='user_authentication'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]