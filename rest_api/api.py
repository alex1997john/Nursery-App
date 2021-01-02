from rest_api.models import Order, Plant
from django.http.response import JsonResponse
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializer import OrderSerializer, PlantSerializer, RegisterSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "data": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
            "status": "Success",
        })

# User API
class UserApi(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        userData = request.user
        return Response({
            "data": UserSerializer(userData).data,
            "status": "Success",
        })

# Plants API - All
class PlantsApi(APIView):
    serializer_class = PlantSerializer

    def get(self, request):
        plants = Plant.objects.all()
        # return JsonResponse(serializer.data, safe=False)
        if plants.count():
            return Response({
                "data": PlantSerializer(plants,many=True).data,
                "status": "Success",
            })
        else :
            return Response({
                "message": "No Data Available",
                "status": "Success",
            })

    

# Plants API - Id
class PlantApi(APIView):
    serializer_class = PlantSerializer

    def get(self, request,id):
        try:
            plant = Plant.objects.get(id=id)
            return Response({
                "data": PlantSerializer(plant).data,
                "status": "Success",
            })
        except Plant.DoesNotExist:
            return Response({
                "message": "No Data Available",
                "status": "Success",
            })

# Plant API - Store
class PlantCreateApi(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        plant = Plant.objects.create(name=request.data['name'], image=request.data['image'],price=request.data['price'], created_by=request.user)
        return Response({
            "data": PlantSerializer(plant, context=self.get_serializer_context()).data,
            "status": "Success",
        })

# User API - Orders
class OrdersApi(APIView):
    serializer_class = OrderSerializer

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        if orders.count():
            return Response({
                "data": OrderSerializer(orders,many=True).data,
                "status": "Success",
            })
        else :
            return Response({
                "message": "No Data Available",
                "status": "Success",
            })


# Order API - Store
class OrderCreateApi(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def post(self, request, *args,  **kwargs):
        order = Order.objects.create(user=request.user, plant=Plant.objects.get(id=request.data['plant_id']),quantity=request.data['quantity'], address=request.data['address'])
        return Response({
            "data": OrderSerializer(order, context=self.get_serializer_context()).data,
            "status": "Success",
        })

