from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from testing.models import Testing



def test_python(request):
    return render(request, 'testing/test_python.html',)


"""def request_page(request):
    if(request.Get.get('mybtn')):
        exec("setup.py")(int(request.Get.get('mytextbox')))

    return render(request, 'testing/output.html')"""

"""

def test_test(request):
    if(request.GET.get('mybtn')):
        if __name__ == '__main__':
            from bandit.bandit.cli import main as RunTest
            exec(RunTest)
            print(RunTest)
    return render(request, 'testing/output.html')"""

def test_test(request):
    response = HttpResponse()
    if(request.GET.get('mybtn')):
        script =  py-find-injection.Script('mytxt' )
        completion = script.unit.core()
        if completion:
            return HttpResponseRedirect(Testing.get_absolute_url())
    return render(request, 'testing/output.html')