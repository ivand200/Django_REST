from django.shortcuts import render
from django.http import request, JsonResponse, Http404
from .models import SP500
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import SP500Serializer


class ListSP500(APIView):
    def get(self,request):
        obj = SP500.objects.all()
        serializer_obj = SP500Serializer(obj,many=True)
        return Response(serializer_obj.data)

    def post(self,request):
        data = request.data
        serializer_obj = SP500Serializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)

class UpdateSP500(APIView):

    def get_object(self,pk):
        try:
            obj = SP500.objects.get(pk=pk)
            return obj
        except:
            raise Http404

    def put(self,request,pk):
        data = request.data
        obj = SP500.objects.get(pk=pk)
        serializer_obj = SP500Serializer(obj,data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)

    def delete(self,request,pk):
        obj = SP500.objects.get(id=id)
        obj.delete()
        return Response({"return":"Component is successfully deleted"})


# Create your views here.
