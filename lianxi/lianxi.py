from django.http import HttpResponse
def index(request):
    print(123456)

def hehe(request):
    return HttpResponse("我是在dev里新键的demo视图")