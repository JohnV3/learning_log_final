from django.contrib import admin
from django.urls import path, include
from learning_logs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('topics/', include('learning_logs.urls')),
    path('accounts/', include('accounts.urls')),
]



