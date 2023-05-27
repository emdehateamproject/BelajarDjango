from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul' : 'Home Pages',
    }
    return render(request, 'index.html', context)
