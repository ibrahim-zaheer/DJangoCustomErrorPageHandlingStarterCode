from django.http import HttpResponse
from django.shortcuts import redirect, render



def home(request):
	return HttpResponse('Hello, World!')


def error_404(request, exception):
	# print(hh)
	return render(request, 'error_404.html', status=404)

def error_500(request):
	return render(request, 'error_505.html', status=500)
