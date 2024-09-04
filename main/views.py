from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306203204',
        'name': 'Nevin Thang',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
