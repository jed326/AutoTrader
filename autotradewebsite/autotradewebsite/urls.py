from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('stocks/', include('choosestock.urls')),
    path('stats/' , include('stats.urls')),

]