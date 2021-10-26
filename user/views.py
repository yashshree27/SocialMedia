
#----api.py code----
from django.views.decorators.http import require_http_methods
from requests import post
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import hashlib
import hashlib
from django.http import QueryDict
from .passwdserialisation import *
import json
from socialmedia import *
from .loginSerialization import *
from .serialization import *
from .user_serialization import *
from .OtpSerialization import *

import random,smtplib

'''
class UserD(RetrieveAPIView):
    sc= serializerLoginClass
    lookup_field = "mobilenumber"
    print("test")

    @csrf_exempt
    def get_queryset(self,request):
        if request.method == "POST":
            getQueryString = {'mobilenumber': '9976543435'}
            print("\n\n query set: ", users_new.objects.filter(**getQueryString))
            return users_new.objects.filter(**getQueryString)
        else:
            return "not a post method"


'''

'''
class try1(APIView):
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
'''








#-------------login code-------------------------------

class UserD(APIView):
    print("\n\ninside userD\n\n")
    def post(self,request):
            print("received value",self.request.data)
            getQueryString = self.request.data
            getQueryString['password'] = hashlib.md5(getQueryString['password'].encode()).hexdigest()
            print(getQueryString)
            print("get query string: ",getQueryString)
            print("type pf get query: ",type(getQueryString))
            #print("** query: ", type(**getQueryString))
            course_qs = users_new.objects.filter(**getQueryString)
            print("course qs: ", course_qs)
            print("type of course qs: ", type(course_qs))
            if (course_qs.exists()):
                print("\n\n query set: ", course_qs)
                model = None
                for course in course_qs:
                    model = course
                sample = list(course_qs.values_list()[0])
                print("get start function")

                print(sample) # has the data of the logged in user as a list
                return Response("Logged In ", status=status.HTTP_200_OK)

            else:
                return Response("fail",status=status.HTTP_400_BAD_REQUEST)

#----------------get user code-----------------------------------
    def get_user(self, userId):
            print("inside get user")
            try:
                print("inside try")
                model = users_new.objects.get(userId=userId)
                print("model get user ", model)
                return model



            except users_new.DoesNotExist:
                print("get user id ",userId)
                return Response(f'User with employee id {userId} is not found in Database',status=status.HTTP_404_NOT_FOUND)

#--------------------delete user code--------------------
    def delete(self, request, userId):
            print("inside delete1")
            model = self.get_user(userId)
            print("inside delete2")
            model.delete()
            print("inside delete3")
            print("deleted user", userId)
            return Response("User Deleted ",status=status.HTTP_204_NO_CONTENT)


#-------------login code end-----------------------------------


#-------------login code-------------------------------

class verifyOtp(APIView):
    #print("\n\ninside userD\n\n")
    def post(self,request):
           # print("received value",self.request.data)
            getQueryString = self.request.data
            print("get query string verify : ",getQueryString)
           # print("type pf get query: ",type(getQueryString))
            #print("** query: ", type(**getQueryString))
            course_qs = users_new.objects.filter(**getQueryString)
            print("course qs: ", course_qs)
            #print("type of course qs: ", type(course_qs))
            if (course_qs.exists()):
                print("\n\n query set verify: ", course_qs)
                model = None
                for course in course_qs:
                    model = course
                sample = list(course_qs.values_list()[0])
                print("verify sample: ")

                print(sample) # has the data of the logged in user as a list
                return Response("OTP verified: ", status=status.HTTP_200_OK)

            else:
                return Response("Otp verification fail",status=status.HTTP_400_BAD_REQUEST)

# ---------verify otp done-----------------------------

#-------------------otp--------------------------------------

class emailOtp(APIView):
    def get_user(self, userId):
        print("inside getuser")
        try:
            model = users_new.objects.get(userId=userId)
            print("inside try")
            print("model get user ", model)
            return model



        except users_new.DoesNotExist:
            print("get user id ", userId)
            return Response(f'User with employee id {userId} is not found in Database',
            status=status.HTTP_404_NOT_FOUND)



    print("\n\ninside userD\n\n")


#----------------try otp naman---------------

    def put(self, request):
        print("inside put email otp")

        number = random.randint(1111, 9999)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.login('franzosocialmedia@gmail.com', 'apurva87654321')
        print(s.login('franzosocialmedia@gmail.com', 'apurva87654321'))

        print("otp generate: ", number)


        #print("received value otp: ", self.request.data)
      #  user_put_data = JSONParser().parse(request) #type is class dict
      #  print("user put data",user_put_data)
      #  print("ite dict: ",user_put_data['emailid'])
       # print("type of json parser: ",type(user_put_data))
        getQueryString = self.request.data
        print("get query type req.data: ",type(getQueryString))
        #getQueryString= user_put_data
        print("type of req.data: ",type(self.request.data))

        #userPut=users_new.objects.get(userId=user_put_data['emailid'])
        #print("user put print: ",userPut)
        course_qs = users_new.objects.filter(**getQueryString) #enter ** then class dict which will make it iterable
        print("course qs: ",course_qs)
        if (course_qs.exists()):
            print("\n\n query set otp: ", course_qs)
            model = None
            for course in course_qs:
                model = course
            sample = list(course_qs.values_list()[0])
            print("inside otp if")

            print("sample: ",sample)  # has the data of the logged in user as a list

            #userPut= users_new.objects.get(userID=user_put_data['emailid'])
            print("user put executed")
            #user_serializer=OtpserializerClass(userPut,data=self.request.data)
            print("user serializer done ")

            #if user_serializer.is_valid():
            #    user_serializer.save()
             #   print("save done!!!")
            s.sendmail('franzosocialmedia@gmail.com', sample[4], str(number))
            return Response("OTP sent successfully check your email ", status=status.HTTP_200_OK)

        else:
            return Response("email ID does not exist", status=status.HTTP_400_BAD_REQUEST)

    #-----------------try otp naman end-----------------
'''
    def put(self, request, userId):
        if not self.get_user(userId):
            return Response(f'User with{userId}is Not Found in Database', status=status.HTTP_404_NOT_FOUND)
            print("inside put")
        serializer = OtpserializerClass(self.get_user(userId), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("OTP put sucessfull", status=status.HTTP_201_CREATED)
        return Response("OTP unsuccessfull", status=status.HTTP_400_BAD_REQUEST)

'''




#-------------------------------OTP---------------------------------
class OTP2(APIView):


    def put(self,request):
            #number = random.randint(1111, 9999)
            #print("otp: ", number)
            print("received value",self.request.data)
            #getQueryString = self.request.data
            getQueryString = self.request.data


            course_qs = users_new.objects.filter(**getQueryString)
            if (course_qs.exists()):
                print("\n\n query set: ", course_qs)
                model = None
                for course in course_qs:
                    model = course
                sample = list(course_qs.values_list()[0])
                print("get start function")

                #print(sample) # has the data of the logged in user as a list
                return Response("Logged In ", status=status.HTTP_200_OK)

            else:
                return Response("fail",status=status.HTTP_400_BAD_REQUEST)

#------------------otp end-----------------------------------




#-----------------signup get post put delete-----------------

@csrf_exempt
def User(request,id=0):
    if request.method=='GET':
        userGet = users_new.objects.all()
        user_serializer = user_Serialization_Class(userGet,many=True)
        return JsonResponse(user_serializer.data,safe=False)





    elif request.method=='PUT':
        user_put_data= JSONParser().parse(request)
        print("user_pput: ",user_put_data)

        userPut= users_new.objects.get(userId=user_put_data['userId'])
        print("user put id data: ",userPut)
        print("type user put ",type(userPut))
        user_serializer= user_Serialization_Class(userPut,data=user_put_data)
        #print("put serial data: ",user_serializer.data)

        if user_serializer.is_valid():
            user_serializer.save()
            print("put serial data: ", user_serializer.data)
            return  JsonResponse("Password changed successfully!!!",safe=False)

        return JsonResponse("Failed to change password",safe=False)
    #elif request.method=='DELETE':
        #user_delete= users_new.objects.get(userId=id)
       # users_new.delete()
       # return JsonResponse("deleted!!")
#-----------------------signup end------------------------


#-------------------OTP-----------------------------------







#--------------------------------------------------------

'''

class UserList(APIView):
    print("class user list started")
    def get(self, request):
        model = users_new.objects.all()
        print("get start function")
        #serializer = serializerClass(model,many=True)
        serializer= serializerClass(model,many=True)

        #----login serializer----
       # ss=serializerLoginClass(model)
       # print("ss.data",ss.data)
        #------------------

        test1=(serializer.data)
        print(type(test1))
        print(type(serializer.data))

        #tuple_list = list(test1.items())
        #print(tuple_list[0])

        #an_iterator = itertools.islice(test1.items(), 0, 1)
        #key_value = next(an_iterator)

        #print(key_value)
        print("json slice: ")
        json_object = json.dumps(test1, indent=4)

        print(json_object)

        #return "done!!"
        print("\nend get function 1")
        #return Response("sample")
        return Response(serializer.data)

    print("\nend get function2")
    def post(self,request):
        # model = Users.objects.all()
        serializer = serializerClass(data=request.data)

        if (serializer.is_valid()):
            serializer.save()
            print("\n\n---------------------")
            print("data post: ",serializer.data)
            print("data post type : ", type(serializer.data))
            print("\n-----------------------")
            #return "SignUp successfull!!!"
            return Response("SignUp successfull!!!", status.HTTP_201_CREATED)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


print("Userlist class exited")

class UserDetail(APIView):
    def get_user(self, userId):
        try:
            model = users_new.objects.get(id=userId)
            print("model get user ", model)
            return model

        except users_new.DoesNotExist:
            print("get user id ", userId)
            return Response(f'User with employee id {userId} is not found in Database',
                            status=status.HTTP_404_NOT_FOUND)

    def get(self, request, userId):
        if not self.get_user(userId):
            return Response(f'User with emp id {userId} is not found in database',
                            status=status.HTTP_404_NOT_FOUND)
        serializer = serializerClass(self.get_user(userId))
        return Response(serializer.data)

    def put(self, request, employee_id):
        serializer = serializerClass(self.get_user(employee_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       

    def delete(self, request, userId):
        model = self.get_user(userId)
        model.delete()
        print("deleted ",userId)
        return Response(status=status.HTTP_204_NO_CONTENT)

'''


#-----api.py end

'''
        Name=input("Enter name: ")
        Mobile=input("Enter mobile number: ")
        Password= input("Enter password: ")
        Confirm_password= input("Enter password again: ")
        if (Password==Confirm_password):
            Emailid = input("Enter emailid: ")
            Acc_created = ""
            FList = ""
            private = input("Enter 0 to make public or 1 to make private: ")
        else:
            print("enter same password again to confirm")
            return post()
'''