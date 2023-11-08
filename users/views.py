import random
import string
import time

from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User
from users.serializers import UserSerializer


class UserAuthenticationView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        user = User.objects.filter(phone_number=phone_number).first()

        if user is not None:
            otp_code = random.randint(1000, 9999)
            user.otp_code = str(otp_code)
            user.save()

            # Имитация отправки кода авторизации
            time.sleep(2)

            print('otp_code:', otp_code)

            return Response({'message': 'Code sent successfully'})
        else:
            invite_code = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))
            otp_code = random.randint(1000, 9999)

            user = User.objects.create(phone_number=phone_number, invite_code=invite_code,
                                       otp_code=str(otp_code))  # Сохранение профиля в БД

            print('otp_code:', otp_code)

            return Response({'message': 'Code created successfully'})

    def get(self, request):
        phone_number = request.data.get('phone_number')
        otp_code = request.data.get('otp_code')

        user = User.objects.filter(phone_number=phone_number).first()
        if not user or not user.check_otp_code(otp_code):
            return Response({'message': 'Invalid credentials'}, status=400)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({'access_token': access_token})


class UserProfileView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        invite_code = user.invite_code

        activated_user_phone_numbers = []

        if invite_code:
            activated_users = User.objects.filter(other_profile_invite_code=invite_code)
            activated_user_phone_numbers = activated_users.values_list('phone_number', flat=True)

        if not activated_user_phone_numbers:
            activated_user_phone_numbers = ['No inviters']

        serialized_data = {
            'phone_number': user.phone_number,
            'invite_code': invite_code,
            'other_profile_invite_code': user.other_profile_invite_code,
            'activated_user_phone_numbers': activated_user_phone_numbers,
        }

        return serialized_data

    def post(self, request):
        user = self.request.user
        other_profile_invite_code = request.data.get('other_profile_invite_code')

        user.other_profile_invite_code = other_profile_invite_code
        user.save()

        return Response({'message': 'Чужой инвайт-код был успешно активирован в профиле пользователя.'})
