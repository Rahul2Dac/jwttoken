from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from .models import item
from .serializers import itemSerializer
from rest_framework.decorators import api_view

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class itemList(APIView):
    permission_classes = (IsAuthenticated,) 
    def get(self,request):
        item1=item.objects.all()
        serializer=itemSerializer(item1,many=True)
        return Response(serializer.data)

    def post(self):
        id = request.POST.get  

class itemrice(APIView):
    permission_classes = (IsAuthenticated,) 
    def get(self,request):
        rice=item.objects.get(id=1) 
        serializer=itemSerializer(rice)
        return Response(serializer.data)

    def post(self,request):
        price = request.POST.get("price")
        item2=item.objects.get(price=price) 
        serializer=itemSerializer(item2)
        return Response(serializer.data)

    def post(self,request):
        itemname = request.POST.get("itemname")
        item3=item.objects.get(itemname=itemname) 
        serializer=itemSerializer(item3)
        return Response(serializer.data)
        



@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})


