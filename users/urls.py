from django.urls import path
from . import views

urlpatterns = (
    [
        path("users/", views.UserListView.as_view(), name="user_list"),
        path("register/", views.RegisterView.as_view(), name="registration_login"),
        path("login/", views.NewLoginView.as_view(), name="login"),
    ]
)

