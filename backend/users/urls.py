from django.urls import path
from .views import SignupView, LoginView, UserInfoView
from .views import AuthenticatedUserView


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserInfoView.as_view(), name='user-info'),
    path("auth/user/", AuthenticatedUserView.as_view()),
]
