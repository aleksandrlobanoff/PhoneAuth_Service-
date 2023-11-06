from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from users.apps import UsersConfig

app_name = UsersConfig.name


urlpatterns = [

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]