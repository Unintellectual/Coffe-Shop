from django.shortcuts import render


def home_view(request):
    return render(request, "pages/home.html", {})

def footer_view (request):
    return render(request, "pages/footer_content.html", {})
