from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer

# Create your views here.
@api_view(['GET'])
def api_overview_view(request):
    api_base_url = '/api/'
    api_urls = {
        'API Overview': '',
        'Tasks List': 'task-list/',
        'Task Creation': 'task-create/',
        'Task Details': 'task-detail/<int:id>/',
        'Task Updation': 'task-update/<int:id>/',
        'Task Deletion': 'task-delete/<int:id>/',
    }

    for url_name in api_urls:
        api_urls[url_name] = api_base_url + api_urls[url_name]

    return Response(api_urls)

@api_view(['GET'])
def task_list_view(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True) # as many tasks are there, so many=True is given
    return Response(serializer.data)

@api_view(['GET','POST'])
def task_add_view(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data) # request.data works here as we use Rest Framework
        # else we would use request.GET or request.POST

        if serializer.is_valid(): # if valid then save
            serializer.save()
            return Response(serializer.data)
    else:
        # for responding to GET request
        return Response('Enter details')

@api_view(['GET'])
def task_detail_view(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def task_update_view(request, id):
    task = Task.objects.get(id=id)

    # updating on same instance and just passing updated data that user passed
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid(): # if valid then update
        serializer.save()
        
        return Response(serializer.data)

@api_view(['DELETE'])
def task_delete_view(request, id):
    task = Task.objects.get(id=id)
    task.delete() # deleting on the model
    return Response('Deletion of task')