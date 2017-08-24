"""tweetme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from .views import TweetListAPIView,TweetCreateAPIView, RetweetAPIView, LikeToggleAPIView,TweetDetailAPIView


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', TweetListAPIView.as_view(), name="list"),
    url(r'^create/$', TweetCreateAPIView.as_view(), name="create"),
    url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view(), name="retweet"),
    url(r'^(?P<pk>\d+)/like/$', LikeToggleAPIView.as_view(), name="like-toggle"),
    url(r'^(?P<pk>\d+)/$', TweetDetailAPIView.as_view(), name="detail"),
]

if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
