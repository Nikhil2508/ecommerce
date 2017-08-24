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
from .views import TweetListView,TweetDetailView,TweetCreateView,TweetUpdateView,TweetDeleteView, RetweetView


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^$', home, name="home"),
    url(r'^$', RedirectView.as_view(url="/")),
    url(r'^search/$', TweetListView.as_view(), name="list"),
    url(r'^create/$', TweetCreateView.as_view(), name="create"),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name="detail"),
    url(r'^(?P<pk>\d+)/retweet/$', RetweetView.as_view(), name="retweet"),
    url(r'^(?P<pk>\d+)/update$', TweetUpdateView.as_view(), name="update"),
    url(r'^(?P<pk>\d+)/delete$', TweetDeleteView.as_view(), name="delete"),
]

if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
