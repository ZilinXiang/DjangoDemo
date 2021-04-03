from django.http import HttpResponse
from django.shortcuts import render
import time, json


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def demo(request):
    """
    ：todo 输入和输出的形式是什么？
    """
    # res = ''
    # content = ''
    # if request.method == 'POST':
    #     print(request.POST)
    #     input = request.POST.get('input')
    #     content = input
    #     res = "input: " + input
    #     return render(request, 'vision/test.html', locals())
    return render(request, "vision/test.html")

@csrf_exempt
def test(request):
    time.sleep(1)
    if request.method == 'POST':
        return HttpResponse(json.dumps({"res": "Hello world ! "}))
    return HttpResponse(json.dumps({"res": "Hello world ! "}))