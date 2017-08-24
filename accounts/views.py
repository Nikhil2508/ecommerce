from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from .models import UserProfile
from django.views.generic.edit import FormView
from .forms import UserRegisterForm
# Create your views here.
User = get_user_model()

class UserRegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'accounts/user_register_form.html'
    success_url = '/login'

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        return super(UserRegisterView, self).form_valid(form)



class UserDetailView(DetailView):
    queryset = User.objects.all()
    template_name = 'accounts/user_detail.html'

    def get_object(self):
        return get_object_or_404(User, username__iexact=self.kwargs.get("username"))

    def get_context_data(self, *args, **kwargs):
        context = super(UserDetailView, self).get_context_data(*args, **kwargs)
        context['following'] = UserProfile.object.is_following(self.request.user,self.get_object())
        context['recommended'] = UserProfile.object.recommend(self.request.user)
        return context

class UserFollowView(View):

    def get(self, request, username, *args, **kwargs):
        toggle_user = get_object_or_404(User, username__iexact=username)
        if request.user.is_authenticated():
            UserProfile.object.toggle_user(request.user, toggle_user)
        return redirect("profiles:detail", username = username)
