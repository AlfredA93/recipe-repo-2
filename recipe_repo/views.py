from django.shortcuts import render


def error404(request, exception):
    "Error 404 - Display this page"
    return render(request, "404.html")


def error500(request):
    """Error 500 - Display this page"""
    return render(request, "500.html")
