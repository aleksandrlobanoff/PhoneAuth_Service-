import random

from rest_framework.response import Response
from rest_framework.views import APIView

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
            invite_code = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))
            otp_code = random.randint(1000, 9999)

            user = User.objects.create(phone_number=phone_number, invite_code=invite_code, otp_code=str(otp_code))

            return Response({'otp_code': otp_code, 'invite_code': invite_code})
