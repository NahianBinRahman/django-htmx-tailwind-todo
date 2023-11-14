from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Todo
from django.views.decorators.http import require_http_methods


def todos(request):
    todos = Todo.objects.all()  # Assuming Todo is your model
    return render(request, 'todos.html', {'todos': todos})


@require_http_methods(['GET', 'POST'])
def edit_todo(request, pk):
    todo = Todo.objects.get(pk=pk)

    if request.method == 'POST':
        todo.title = request.POST.get('title', '')
        todo.due_date = request.POST.get('due_date', None)
        todo.save()

        return render(request, 'partials/todo.html', {'todo': todo})

    return render(request, 'partials/edit.html', {'todo': todo})


@require_http_methods(['POST'])
def add_todo(request):
    title = request.POST.get('title', '')
    due_date = request.POST.get('due_date', None)
    priority = request.POST.get('priority', Todo.MEDIUM)

    if title:
        todo = Todo.objects.create(
            title=title, due_date=due_date, priority=priority)
        return JsonResponse({'html': render(request, 'partials/todo.html', {'todo': todo}).content})
    else:
        return JsonResponse({'error': 'Invalid form data'}, status=400)


@require_http_methods(['PUT'])
def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_done = True
    todo.save()

    return render(request, 'partials/todo.html', {'todo': todo})


@require_http_methods(['DELETE'])
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()

    return HttpResponse()
