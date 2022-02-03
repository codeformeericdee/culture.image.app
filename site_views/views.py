from django.template import loader
from django.http import HttpResponse

def index(request):
    html = loader.get_template('site_views/index.html')
    context = {}
    return HttpResponse(html.render(context, request))
    ## Change index to preload x amount of view requested images into RAM.
    # then utilize the cached images using the API logic.