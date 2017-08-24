from django import template
from django.contrib.auth import get_user_model

from accounts.models import UserProfile

register = template.Library()


User = get_user_model()

@register.inclusion_tag("accounts/snippets/recommended.html")
def recommended(user):
    if isinstance(user, User):
        qs = UserProfile.object.recommend(user)
        return {"recommended": qs}
