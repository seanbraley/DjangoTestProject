"""
Definition of views.
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.template import RequestContext
from django.views import View
from datetime import datetime
from .models import ImportantButton

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def button(request):
    """renders the button page."""
    return render(
        request,
        'app/button.html',
        {
            'title':'Press the Button',
            'message':'Seriously press the button',
            'year':datetime.now().year,
        }
    )

class ButtonView(View):
    initial = {'id': '1'}
    title = 'Press the button'
    message = 'Seriously'
    template_name = 'app/button.html'

    def get (self, request):
        button = get_object_or_404(ImportantButton, pk='1')
        return render(request, self.template_name, dict(title=self.title, message=self.message, year=datetime.now().year, count=button.press_count))

    def post(self, request, *args, **kwargs):
        button = get_object_or_404(ImportantButton, pk=request.POST.get('id'))
        button.press_count += 1
        button.expiry_time = datetime.utcnow()
        button.save()
        return render(request, self.template_name, dict(title=self.title, message=self.message, year=datetime.now().year, count=button.press_count))
        
