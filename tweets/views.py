from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from django.http import HttpResponseRedirect
from django.forms.utils import ErrorList
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Tweet
from django.urls  import reverse_lazy, reverse
from django.db.models  import Q
from django.views import View
# Create your views here.


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    # success_url = "/tweet/"
    login_url = "/admin/"

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    queryset = Tweet.objects.all()
    template_name = "tweets/delete_confirm.html"
    success_url = reverse_lazy("tweet:list")

class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    # success_url = reverse_lazy("tweet:detail")

    # def form_valid(self, form):
    #     if self.request.user.is_authenticated():
    #         form.instance.user = self.request.user
    #         return super(TweetCreateView, self).form_valid(form)
    #     else:
    #         form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue."])
    #         return self.form_invalid(form)

class TweetListView(LoginRequiredMixin,ListView):
    # queryset = Tweet.objects.all()
    template_name = "tweets/tweet_list.html"

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query =  self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(Q(content__icontains=query)|Q(user__username__icontains=query))
        return qs

    def get_context_data(self,*args,**kwargs):
        context = super(TweetListView,self).get_context_data(*args, **kwargs)
        print(context)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy("tweet:create")
        return context

class RetweetView(View):
    def get(self, request, pk, *args, **kwargs):
        tweet = get_object_or_404(Tweet, pk=pk)
        if request.user.is_authenticated():
            new_tweet = Tweet.objects.retweet(request.user, tweet)
            return HttpResponseRedirect("/")
        return HttpResponseRedirect(tweet.get_absolute_url())


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name = "tweets/tweet_detail.html"

    # def get_object(self):
    #     pk = self.kwargs["pk"]
    #     return Tweet.objects.get(id=pk)
