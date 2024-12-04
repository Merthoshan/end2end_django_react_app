
from django.contrib import admin
from django.urls import include, path
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(),name="register"), # registration is done here for new users
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"), # u get both the tokens here
    path("api/token/refresh/", TokenRefreshView.as_view(), name = "refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),
]


