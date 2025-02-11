from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, permissions
from rest_framework import viewsets, filters
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from .models import Customer, Product, Employee, Task
from .serializers import CustomerSerializer, ProductSerializer, EmployeeSerializer, TaskSerializer
from .serializers import UserSerializer


class BaseModelViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user)
    #
    # def perform_update(self, serializer):
    #     serializer.save(updated_by=self.request.user)
    #
    # def perform_destroy(self, instance):
    #     instance.deleted_by = self.request.user
    #     instance.deleted_at = now()
    #     instance.save()


class CustomerViewSet(BaseModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_fields = ['name', 'phone']

class ProductViewSet(BaseModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['name', 'price']


class EmployeeViewSet(BaseModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_fields = ['hired_date', 'position']


class TaskViewSet(BaseModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_fields = ['status', 'assigned_to']
    search_fields = ['title', 'description']



class RegisterView(APIView):
    @extend_schema(
        request=UserSerializer,  # Xác định request body trong Swagger
        responses={201: "User registered successfully!", 400: "Bad request"},
        auth=None
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


