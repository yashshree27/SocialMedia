from user.models import users_new
from rest_framework import serializers

class OtpserializerClass(serializers.ModelSerializer):
   # acc_created = serializers.CharField(required=False)
    #userId = serializers.CharField(required=False)

    class Meta:
        model= users_new
        fields= list(["otp"])

        #------