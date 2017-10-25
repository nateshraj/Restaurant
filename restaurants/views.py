from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def home(request):
# 	qwe = """
# 	<hmtl>
# 	<head><title>First page</title>
# 	</head>
# 	<body>
# 	<p><b>This is a paragraph </b></p>
# 	</body>
# 	</hmtl>
# 	"""
# 	return HttpResponse(qwe)

def home(request):
	return render(request, 'restaurants/index.html')

def music(request):
	return render(request, 'restaurants/index.html')
	# return HttpResponse("Yo")

# def index(request):
# 	return HttpResponse("Working")