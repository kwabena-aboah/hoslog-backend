"""hoslog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.static import serve
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from clients.views import index, ClientViewset, TotalClients
from users.views import UserProfileViewset, UserViewset, MyObtainTokenPairView

router = routers.DefaultRouter()
router.register(r'clients', ClientViewset)
router.register(r'users', UserViewset)
router.register(r'profile', UserProfileViewset)
# router.register(r'charts', TotalClients)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('api/charts/', TotalClients.as_view(), name='charts'),
    path('api/login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)