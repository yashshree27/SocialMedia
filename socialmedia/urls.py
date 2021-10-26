
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from user.views import UserD, User, emailOtp, OTP2, verifyOtp
from user.signup_post_view import Signup_Post
#from user.views import LogIn#User
#UserList, UserDetail, User
#from user.views import try1

urlpatterns = [
    path('admin/', admin.site.urls),
   # url(r'^api/show/(?P<userId>\d+)/$', UserDetail.as_view(),name='user_list'),


  #  path('view/', showData(),name='show data')


   # url(r'^api/show/$', UserList.as_view(), name='user_list'),

    url(r'^api/signup$',view=User),
    url(r'^api/put$',view=User),
    url(r'^api/signup/post$',Signup_Post.as_view(),name="signup post"),
    url(r'^api/emailOtp2$',view=emailOtp),

    url(r'^api/otp/(?P<userId>\d+)/$',emailOtp.as_view(),name = 'otp store'),
   # url(r'^api/otp$',view=OTP2.as_view()),
    url(r'^api/emailOtp$',emailOtp.as_view()),
    url(r'^api/delete/(?P<userId>\d+)/$',UserD.as_view(),name='delete user'),

    url(r'^api/login$', UserD.as_view()),
    url(r'^api/verify$', verifyOtp.as_view())
    #url(r'^api/login$',view= LogIn)

]
