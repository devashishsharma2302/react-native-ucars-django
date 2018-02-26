from __future__ import unicode_literals, absolute_import
from django.conf.urls import include, url

from rest_framework.authtoken import views
from .views import UserImageAPIView

urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^user-profile/', UserImageAPIView.as_view()),

]
