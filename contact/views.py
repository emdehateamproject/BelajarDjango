from django.shortcuts import render

def contact(request):
    context = {
        'judul' : 'Contact Pages',
    }

    return render(request, 'contact/contact.html', context)
