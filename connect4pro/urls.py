import debug_toolbar
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import TokenRefreshView

from react_app.views import ReactAppView
from users.views import MyTokenObtainPairView, LogoutView
from . import settings
from .yasg import urlpatterns as yasg_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('users.urls')),
    path('', include('events.urls')),
    path('', include('faq.urls')),
    path('', include('blog.urls')),
    # path('', include('forum.urls')),
    path('', include('grants_and_investments.urls')),
    path('', include('adverts.urls')),
    path('', include('polls.urls')),
    path('', include('payments.urls')),
    path('', include(('social_auth.urls', 'social_auth'), namespace="social_auth")),
    path('', include('newsletter.urls')),
    path('', include('links.urls')),

    path('api/login', csrf_exempt(MyTokenObtainPairView.as_view()), name='token_obtain_pair'),
    path('api/login/refresh', csrf_exempt(TokenRefreshView.as_view()), name='token_refresh'),
    path('api/logout/', LogoutView.as_view(), name='auth_logout'),

    # path('',ReactAppView.as_view()),

]

urlpatterns += yasg_urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns.append(re_path(r'^', ReactAppView.as_view()))
