from django.urls import path
from django.contrib.auth.views import LogoutView
from core.views import login_page, home_page

urlpatterns = [
    path('', home_page, name="home"),
    path('login/', login_page, name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
]
