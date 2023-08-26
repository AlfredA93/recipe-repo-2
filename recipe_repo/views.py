from django.shortcuts import render


def error404(request, exception):
    "Error 404 - Display this page"
    return render(request, "404.html")
