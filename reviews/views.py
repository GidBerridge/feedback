from tkinter.tix import InputOnly
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import is_valid_path
from .forms import ReviewForm
from .models import Review
from django.views import View


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/review.html", {
            "form": form
        })


def thank_you(request):
    return render(request, "reviews/thank_you.html", {
        "has_error": False
    })
