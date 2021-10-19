
#----api.py code----

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
import json
from socialmedia import *
from .serialization import *

class UserList(APIView):
    print("class user list started")
    def get(self, request):
        model = users_new.objects.all()
        print("get start function")
        serializer = serializerClass(model,many=True)
        test1=(serializer.data)
        print(type(test1))
        print(type(serializer.data))

        #tuple_list = list(test1.items())
        #print(tuple_list[0])

        #an_iterator = itertools.islice(test1.items(), 0, 1)
        #key_value = next(an_iterator)

        #print(key_value)
        print("json slive:")
        json_object = json.dumps(test1, indent=4)

        print(json_object)

        #return "done!!"
        print("\nend get function 1")
        #return Response("sample")
        return Response(serializer.data)

    print("\nend get function2")
    def post(self, request):
        # model = Users.objects.all()
        serializer = serializerClass(data=request.data)
        print("\npost funct:",serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


print("Userlist class exited")
'''
class UserDetail(APIView):
    def get_user(self, employee_id):
        try:
            model = user.objects.get(id=employee_id)
            return model
        except user.DoesNotExist:
            return Response(f'User with employee id {userId} is not found in Database',
                            status=status.HTTP_404_NOT_FOUND)

    def get(self, request, employee_id):
        if not self.get_user(employee_id):
            return Response(f'User with emp id {emd} is not found in database',
                            status=status.HTTP_404_NOT_FOUND)
        serializer = UsersSerializer(self.get_user(employee_id))
        return Response(serializer.data)

    def put(self, request, employee_id):
        serializers = UsersSerializer(self.get_user(employee_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        '''
        #try:
         #   model = Users.objects.get(id=employee_id)

        #except Users.DoesNotExist:
         #   return Response(f'User with employee id {employee_id} is not found in Database', status=status.HTTP_404_NOT_FOUND)

        #serializer = UsersSerializer(data=request.data)

        #if serializer.is_valid():
         #   serializer.save()
          #  return Response(serializer.data, status=status.HTTP_201_CREATED)

        #return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
'''

    def delete(self, request, employee_id):
        model = self.get_user(employee_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''

#-----api.py end