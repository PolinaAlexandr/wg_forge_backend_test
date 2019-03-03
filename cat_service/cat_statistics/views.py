from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cats
from .serializers import CatsSerializer


def ping(request):
    return HttpResponse('"Cats Service. Version 0.1"')


@api_view(['GET'])
def cat_list(request):
    sort_attribute_attr = request.GET.get('attribute', '') 

    sort_order_attr = request.GET.get('order', '') 

    limit_attr = request.GET.get('limit', Cats.objects.count())

    offset_attr = request.GET.get('offset', 0)

    try:
        limit = int(limit_attr)

        if limit < 0:
           raise ValueError()
    except ValueError:
        return HttpResponse(f'Error parsing "limit" parameter ({limit_attr}). Provide a positive number')

    try:
        offset = int(offset_attr)

        if offset < 0:
           raise ValueError()
    except ValueError:
        return HttpResponse(f'Error parsing "offset" parameter ({offset_attr}). Provide a positive number')

    if not sort_attribute_attr or sort_order_attr == 'asc':
        sort_order = ''
    elif sort_order_attr == 'desc':
        sort_order = '-'
    else:
        sort_order = ''

    order_by_query = f'{sort_order}{sort_attribute_attr}'

    cats = Cats.objects.all().order_by(order_by_query)[offset:limit]

    cats_serializer = CatsSerializer(cats, many=True)

    return Response(cats_serializer.data)


@api_view(['POST'])
def cat_create(request):
    data = JSONParser().parse(request) 

    serializer = CatsSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
