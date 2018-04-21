from django.contrib import admin
from django.urls import include, path

from my_auth.views import login
from .views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', login, name="login"),
    path('', include('social_django.urls', namespace='social'))
]
