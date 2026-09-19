from django.http import HttpResponse

def call_counter(func):
    count = 0
    def wrapper(*args):
        nonlocal count
        count += 1
        print(f'Функция вызвана {count} раз')
        return func(*args)
    return wrapper

def post_only(func):
    def wrapper(request, task_id):
        if request.method == 'POST':
            return func(request, task_id)
        else:
            return HttpResponse('Разрешены только POST запросы', status=405)
    return wrapper


