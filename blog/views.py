from django.shortcuts import render

# Create your views here.
def blog(request):
    context = {
        'judul' : 'Blog Pages',
    }

    return render(request, 'blog/blog.html', context)