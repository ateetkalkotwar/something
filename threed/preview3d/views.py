from django.shortcuts import render

def preview(request):
    return render(request, 'preview3d/preview.html')