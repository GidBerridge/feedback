from urllib import request
from reviews.models import Review
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import is_valid_path
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView


class ReviewView(CreateView):
    model = Review
    fields = "__all__"
    template_name = "reviews/review.html"
    success_url = "/thank-you"


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This Works!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favourite_id = request.session.get("favourite_review")
        context["is_favourite"] = favourite_id == str(loaded_review.id)
        return context


class AddFavouriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favourite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
