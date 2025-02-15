from django.urls import path

from core import views

app_name = "users"
urlpatterns = [
    path("~redirect/", view=views.UserRedirectView.as_view(), name="redirect"),
    path("~update/", view=views.UserUpdateView.as_view(), name="update"),
    path("<str:username>/", view=views.UserDetailView.as_view(), name="detail"),
]
