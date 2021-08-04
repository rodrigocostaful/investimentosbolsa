from django.shortcuts import render


# Create your views here.
def dashboard(request):
    data = {
        'titulo': "Dashboard"
    }
    return render(request, 'core/dashboard.html', data)
