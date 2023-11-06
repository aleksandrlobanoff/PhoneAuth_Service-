import random

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


class UserAuthenticationView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        user = User.objects.filter(phone_number=phone_number).first()

        if user is not None:
            otp_code = random.randint(1000, 9999)
            user.otp_code = str(otp_code)
            user.save()

            return Response({'otp_code': otp_code})
        else:
            # invite_code = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))
            otp_code = random.randint(1000, 9999)

            user = User.objects.create(phone_number=phone_number, otp_code=str(otp_code))

            return Response({'otp_code': otp_code})

    def put(self, request):
        phone_number = request.data.get('phone_number')
        otp_code = request.data.get('otp_code')

        user = User.objects.filter(phone_number=phone_number).first()
        if not user or not user.check_otp_code(otp_code):
            return Response({'message': 'Invalid credentials'}, status=400)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({'access_token': access_token})
