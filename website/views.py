from django.shortcuts import render

def inicio(request):
   return render(request, 'index.html')

def test(request):
   return render(request, 'test.html')
