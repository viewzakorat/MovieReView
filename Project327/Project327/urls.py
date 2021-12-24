"""Project327 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from Project327.ReviewMovie.views import RESETavg
from ReviewMovie import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Login',views.logins,name = 'Login'),
    path('Register',views.register,name = 'Register'),
    path('UserCreate',views.UserRegister.as_view(),name = 'RegisterCreate'),
    path('UserLogin',views.UserLogin.as_view(),name = 'Login'),
    path('MovieReviewPage',views.MovieReviewPage,name = 'Movie_review_page'),
    path('MovieReviewMessage',views.MoiveMessageReview.as_view(),name = 'Movie_review_message'),
    path('MovieReviewMessageList/<str:movie_id>',views.CommentList.as_view(),name = 'Movie_review_message_list'),
    path('Logout',views.logouts,name = 'Logout'),

    path('Ban/<str:user_username>/<str:movie_id>',views.DELETE_USER.as_view()),
    path('DeleteComment/<str:user_username>/<str:movie_id>',views.DELETE_COMMENT.as_view()),

    path('GET/<str:movie_id>',views.Fetchy.as_view()),
    path('MovieGet/<str:movie_id>',views.MovieGet.as_view()),


    path('',views.index,name = 'home'),
    path('gotoReview',views.MovieReviewPage, name= 'gotoReview'),

    path('RESETavg/<str:movie_id>',views.RESETavg.as_view(), name= 'RESET')


]
