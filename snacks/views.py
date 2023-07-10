from django.shortcuts import render
# from django.urls.generic import TemplateViews
# Create your views here.

# class HomeView(TemplateView):
#     template_name = 'home.html'

def home(request):
    return render(request, 'snacks/home.html')

def about(request):
    return render(request, 'snacks/about.html')