from django.shortcuts import render, redirect
from .models import Review

# Create your views here.


def index(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, "community/index.html", context)


def new(request):
    return render(request, "community/new.html")


def detail(request, pk):
    review = Review.objects.get(pk=pk)

    context = {
        "review": review,
    }
    return render(request, "community/detail.html", context)


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")

    Review.objects.create(title=title, content=content)
    return redirect("community:index")


def edit(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        "review": review,
    }
    return render(request, "community/edit.html", context)


def update(request, pk):
    review = Review.objects.get(pk=pk)

    title = request.GET.get("title")
    content = request.GET.get("content")

    review.title = title
    review.content = content

    review.save()

    return redirect("community:detail", review.pk)


def delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect("community:index")
