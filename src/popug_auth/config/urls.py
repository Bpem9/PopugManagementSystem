from django.contrib import admin
from django.urls import path, include

from popugauth.views import get_user_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('o/user_info/', get_user_info, name='user_info'),
]
