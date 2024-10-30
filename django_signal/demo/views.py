
from django.http import JsonResponse,HttpRequest
from .utils import Rectangle

def rectangle_view(request):
    rect = Rectangle(10, 5)
    data = [dim for dim in rect]
    return JsonResponse(data, safe=False)
