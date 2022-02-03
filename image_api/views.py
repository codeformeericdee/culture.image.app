from django.http import HttpResponse
from database_models.models import GlobalSymbol

def global_symbol_page(request, **kwargs):
    # Change to a dynamic class finder if urlpatterns can pass arguments
    # print(str(kwargs['id']))
    try:
        query = GlobalSymbol.objects.get(id=kwargs['id']).upload
        image = bytes(query.read())
    except Exception as error:
        print(error)
        change_me_to_a_404 = "Image not found"
        return HttpResponse(change_me_to_a_404)
    return HttpResponse(image, content_type="image/jpeg")
