from django.contrib import admin
from django.urls import path
from app1.views import new_emp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', new_emp, name='Home_page'),
]