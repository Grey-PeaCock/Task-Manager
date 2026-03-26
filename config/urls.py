from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),     # Main app routes
    path('admin/', admin.site.urls),    
]