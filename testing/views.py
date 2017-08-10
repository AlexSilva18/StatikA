#!/bin/sh
import os
import subprocess
import tempfile
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, Context
from django.shortcuts import get_object_or_404, render, redirect
from testing.models import Testing
from django import forms
from codemirror2.widgets import CodeMirrorEditor

def test_python(request):
    return render(request, 'testing/upload_python.html',)

def TESTING(request):
    return render(request, 'testing/test_python.html',)


def test_test(request):
    context = {}
    if request.method == 'POST':
        input_text = request.POST.get('mytextbox')
        if len(input_text) == 0:
            print('Please insert textbox with code')
            # Could send this error message to the test_python view
        else:
            fd, file_name = tempfile.mkstemp()
            with open(file_name, 'w') as input_file:
                input_file.write(input_text)
            args = [
                "flake8",
                file_name,
            ]
            process = subprocess.Popen(args, stdout=subprocess.PIPE)
            results = process.communicate()[0]
            os.remove(file_name)
            results = results.replace(bytes('{}:'.format(file_name), 'ascii'), b'')
            context['results'] = results
            return render(request, 'testing/output.html', context)
    return redirect('testing:test_python')

class TestFrom(forms.Form):
    css = forms.CharField(widget=CodeMirrorEditor(options={'mode': 'css'}))