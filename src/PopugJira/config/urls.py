from django.contrib import admin
from django.urls import path, include

from popug_jira.views import custom_login_view, PopugDetailedView, PopugListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signin/', custom_login_view, name='login'),
    path('popug/', PopugListView.as_view(), name='popug'),
    path('popug/<uuid:pk>/', PopugDetailedView.as_view(), name='popug'),

]
