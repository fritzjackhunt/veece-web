from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'veece/index.html')

def privacyPolicy(request):
    return render(request, 'veece/privacy-policy.html')
