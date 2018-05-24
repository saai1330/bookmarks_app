from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
def main_page(request):
    output = '''
    <html>
    <head><title>%s</title></head>
    <body>
    <h1>%s</h1>
    <p>%s</p>
    </body>
    </html>''' % (
        'Django Bookmarks',
        'Welcome to Django Bookmarks',
        'Where you can store add share bookmarks!')

    return HttpResponse(output)