from django.contrib.auth import get_user_model
from rest_framework.routers import DefaultRouter
from djoser import views
from django.urls import path
router = DefaultRouter()
router.register("users", views.UserViewSet)

User = get_user_model()

urlpatterns = router.urls


path(r"^token/login/?$", views.TokenCreateView.as_view(), name="login"),
path(r"^token/logout/?$", views.TokenDestroyView.as_view(), name="logout"),
"""
path(r"^activation/?$", views.activation.as_views(), name="activation"),
path(r"^resend_activation/?$", views.resend_activation.as_views(), name="resend_activation"),
path(r"^set_password/?$", views.set_password.as_views(), name="set_password"),
path(r"^reset_password/?$", views.reset_password.as_views(), name="reset_password"),
path(r"^reset_password_confirm/?$",  views.reset_password_confirm.as_views(), name="reset_password_confirm"),
path(r"^set_username/?$", views.set_username.as_views(), name="set_username"),
path(r"^reset_username/?$", views.reset_username.as_views(), name="reset_username"),
path(r"^reset_username_confirm/?$", views.reset_username_confirm.as_views(), name="reset_username_confirm"),"""



"""from . views import UserRegistrationView, UserLoginView, UserLogoutView
from django.urls import path



urlpatterns = [
    path('users/', UserRegistrationView.as_view(),name='register'),
    path('token/login/', UserLoginView.as_view(), name='login'),
    path('token/logout/', UserLogoutView.as_view(), name='logout'),

]"""