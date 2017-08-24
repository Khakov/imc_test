# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework.parsers import JSONParser

from imc_test_rest.models import Animal, Area
from imc_test_rest.serialize import AnimalSerialize, AreaSerialize


def get_animal(request, animal_id):
    try:
        animal = Animal.objects.get(id=animal_id)
    except Animal.DoesNotExist:
        if request.method == 'PUT' or request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = AnimalSerialize(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AnimalSerialize(animal, context={'request': request})
        return HttpResponse(json.dumps(serializer.data, ensure_ascii=False, encoding="utf-8"),
                            content_type="application/json; encoding=utf-8")
    elif request.method == 'PUT' or request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AnimalSerialize(animal, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        animal.delete()
        return HttpResponse(status=200)


def get_area(request, area_id):
    try:
        area = Area.objects.get(id=area_id)
    except Area.DoesNotExist:
        if request.method == 'PUT' or request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = AreaSerialize(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AreaSerialize(area, context={'request': request})
        return HttpResponse(json.dumps(serializer.data, ensure_ascii=False, encoding="utf-8"),
                            content_type="application/json; encoding=utf-8")
    elif request.method == 'PUT' or request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AreaSerialize(area, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        area.delete()
        return HttpResponse(status=200)
