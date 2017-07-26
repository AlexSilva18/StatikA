#!/bin/sh
import shell_command
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, Context
from django.shortcuts import get_object_or_404, render
from testing.models import Testing
import bandit
python_code = __import__('django-lint')

def test_python(request):
    return render(request, 'testing/upload_python.html',)

def test_test(request):
    if (request.GET.get('mybtn')):
        if len(('mytextbox').get()) == 0:
            print('Please inser textbox with code')
        else:
            exec(bandit)

    return render(request, 'testing/output.html')



"""def test_test(request):
    html_result = ''
    if request.method == "POST":
        # this checks that a file exists
        if len(request.FILES) != 0:
            file1 = request.FILES['file1']
            test = exec("django-lint.py", file1)
            for sentence in test:
                html_result += '<p>{}</p>'.format(sentence)
    return render(request, 'testing/output.html')"""


"""def test_test(request):
    response = HttpResponse()
    if(request.GET.get('mybtn')):
        script =  py-find-injection.Script('mytxt' )
        completion = script.unit.core()
        if completion:
            return HttpResponseRedirect(Testing.get_absolute_url())
    return render(request, 'testing/output.html')"""