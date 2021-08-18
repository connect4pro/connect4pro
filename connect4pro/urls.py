from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include
import debug_toolbar
from django.views.decorators.csrf import csrf_exempt

from users.views import MyTokenObtainPairView, LogoutView
from . import settings
from .yasg import urlpatterns as yasg_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('users.urls')),
    path('', include('events.urls')),
    path('', include('faq.urls')),
    path('', include('blog.urls')),
    path('', include('forum.urls')),
    path('', include('grants_and_investments.urls')),
    path('', include('adverts.urls')),
    path('', include('polls.urls')),
    path('', include('payments.urls')),

    path('api/login', csrf_exempt(MyTokenObtainPairView.as_view()), name='token_obtain_pair'),
    path('api/login/refresh', csrf_exempt(TokenRefreshView.as_view()), name='token_refresh'),
    path('api/logout/', LogoutView.as_view(), name='auth_logout'),

]

urlpatterns += yasg_urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)