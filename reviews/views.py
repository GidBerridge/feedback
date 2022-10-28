from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import is_valid_path
from .forms import ReviewForm


def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")

    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html", {
        "has_error": False
    })
