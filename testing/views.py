from django.shortcuts import get_object_or_404, render

from testing.models import Testing

def test_python(request):
    return render(request, 'testing/test_python.html')
