from asyncio.constants import DEBUG_STACK_DEPTH
from django.shortcuts import render
from django.urls import is_valid_path
from django.views import View
from django.http import HttpResponseRedirect
from .models import UserProfile
from django.views.generic.edit import CreateView

from .forms import ProfileForm
# Create your views here.


# def store_file(file):
#     with open("temp/image.jpg", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"
