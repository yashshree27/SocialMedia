from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import hashlib
from .passwdserialisation import *

class Signup_Post(APIView):
    def post(self,request):
        usrData = JSONParser().parse(request)
        print("user  pass data type ", type(usrData))
        print("user data: ", usrData)
        serializer = PasswdserializerClass(data=usrData)
        password = usrData['password']
        hash_password = hashlib.md5(password.encode()).hexdigest()

        print(hash_password)
        usrData['password'] = hash_password
        print("hassh passs rpint ", usrData)

        print("type of usr data after hash: ", type(usrData))
        print("req data hashed: ", usrData)

        if serializer.is_valid():
            print("inside valid s hash")
            serializer.save()
            print("type ", type(serializer.data))
            return Response("Signup SuccessFull", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)