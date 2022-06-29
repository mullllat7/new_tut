
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *
router = DefaultRouter()


router.register(r'info_users', InfoUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view()),
    # path('activate/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    # path('change_password/', ChangePasswordView.as_view()),
    # path('forgot_password/', ForgotPasswordView.as_view()),
    # path('forgot_password_complete/', ForgotPasswordCompleteView.as_view())
    ]
