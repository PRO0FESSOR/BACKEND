from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.views import View
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Function-based views

def home_view(request):
    return HttpResponse('This is home page !!')

def simple_view(request):
    return HttpResponse('Hello From First Task')

def template_view(request):
    return render(request, 'random.html')

def dynamic_view(request, name):
    return HttpResponse(f"Hello, {name}")  

def json_view(request):
    return JsonResponse({'status': 'success', 'message': 'JSON response'})

@csrf_exempt
@require_http_methods(["POST"])
def post_only_view(request):
    return HttpResponse("ONLY POST ALLOWED")  

def error_view(request):
    return HttpResponseNotFound("THIS PAGE DOES NOT EXIST !!")

# Class-based views

class HelloCBV(View):
    def get(self, request):
        return HttpResponse("Hello from the class based view")

class TemplateCBV(View):
    def get(self, request):
        return render(request, 'random.html')

@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(require_http_methods(["POST"]), name='dispatch')
class PostonlyCBV(View):
    def post(self, request):
        return HttpResponse("POST FROM CBV")  

# Handling different HTTP methods in a FBV

@csrf_exempt
def method_view(request):
    if request.method == 'GET':
        return HttpResponse("GET request")
    elif request.method == 'POST':
        return HttpResponse("POST request")
    elif request.method == 'PUT':
        return HttpResponse("PUT request")
    elif request.method == 'PATCH':
        return HttpResponse("PATCH request")
    elif request.method == 'DELETE':
        return HttpResponse("DELETE request")
    else:
        return HttpResponse("Unknown method")

# Handling different HTTP methods in a CBV

@method_decorator(csrf_exempt, name='dispatch')
class MethodCBV(View):
    def get(self, request):
        return HttpResponse("GET from CBV")
    
    def post(self, request):
        return HttpResponse("POST from CBV")

    def put(self, request):
        return HttpResponse("PUT from CBV")

    def patch(self, request):
        return HttpResponse("PATCH from CBV")

    def delete(self, request):
        return HttpResponse("DELETE from CBV")

