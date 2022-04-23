import re
from urllib import response
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import  JsonResponse

from EmployeeApp.models import Department, Employee
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

from django.core.files.storage import default_storage
# Create your views here.
@csrf_exempt
def departmentApi(request, id=0):
    if request.method == "GET":
        departments = Department.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == "POST":
        print(request)
        department_data = JSONParser().parse(request)
        print(department_data)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to added", safe=False)
    elif request.method == "PUT":
        department_data = JSONParser().parse(request)
        department = Department.objects.get(DepartmentId=department_data["DepartmentId"])
        departments_serializer = DepartmentSerializer(department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method == "DELETE":
        department = Department.objects.get(DepartmentId = id)
        department.delete()
        return JsonResponse("Deleted Successfullt", safe=False)




@csrf_exempt
def employeeApi(request, id=0):
    if request.method == "GET":
        employees = Employee.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method == "POST":
        print(request)
        employee_data = JSONParser().parse(request)
        print(employee_data)
        employees_serializer =EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to added", safe=False)
    elif request.method == "PUT":
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(EmployeeId=employee_data["EmplyeeId"])
        employees_serializer = EmployeeSerializer(employee, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method == "DELETE":
        employee = Employee.objects.get(EmployeeId = id)
        employee.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def SaveFile(request):
    print(request.FILES)
    file = request.FILES['file']
    print(default_storage.path)
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)