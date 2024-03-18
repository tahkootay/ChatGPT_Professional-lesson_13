from django.shortcuts import render
#from .models import MyModel
from django.http import HttpRequest, HttpResponse
from collections import defaultdict
import requests


# Create your views here.
#def index(request):
#    items = MyModel.objects.all()
#    return render(request, 'index.html', {'items': items})

def main(request: HttpRequest):
    return render(request, 'index.html')
    
def about(request: HttpRequest):
    return render(request, 'about.html')

# def fstring(request: HttpRequest):
#     with open("templates/index_fstring.html") as file:
#         text = file.read()
#      #   text = "You are: "
#         return HttpResponse(text.format(name=request.GET["name"]))
    
def fstring(request):
    # Получаем значение параметра 'name' из GET-запроса или 'Unknown', если параметра 'name' нет
    context = {'name': request.GET.get('name', 'Unknown')}
    return render(request, 'index_fstring.html', context)

def test(request):
    return HttpResponse("Hello, world. You're at the test webpage.")

def chat_view(request):
    # Если запрос - POST, можно здесь обработать данные формы
    if request.method == "POST":
        # Ваша логика для обработки данных формы здесь
        pass
    # Если запрос - GET, просто отобразим страницу с формой
    return render(request, 'chat.html')

def stat(request):
    time_stamps = []
    hourly_counts = defaultdict(int)
    try:
        # Отправляем GET-запрос на заданный адрес
        response = requests.get('http://127.0.0.1:8000/how_many_requests')
        # Проверяем статус-код ответа
        if response.status_code == 200:
            # Действия в случае успешного запроса
            #return HttpResponse(response.text)
            time_stamps = response.json()  # Преобразование ответа из формата JSON в список
            # Обрабатываем каждую отметку времени в списке
            for ts in time_stamps:
                # Отбрасываем минуты, секунды и миллисекунды
                hour_mark = ts[:13]  # формат "YYYY-MM-DDTHH"
                #print('hour_mark: ', hour_mark)
                hourly_counts[hour_mark] += 1  # Увеличиваем счетчик для соответствующего часа
            # Создаем HTML-таблицу
            table_html = '<table border="1">'
            table_html += "<tr><th>Дата и время</th><th>Количество отметок за указанный час</th></tr>"
            for hour, count in sorted(hourly_counts.items()):
                table_html += f"<tr><td>{hour}</td><td>{count}</td></tr>"
            table_html += "</table>"
            table_html += f"<br>Итого запросов: {len(time_stamps)}"
            return HttpResponse(table_html)
        else:
            # Действия в случае ошибки
            return HttpResponse('Ошибка запроса. Статус-код: ' + str(response.status_code))
    except requests.exceptions.RequestException as e:
        # Обработка исключения в случае ошибки соединения
        return HttpResponse('Ошибка соединения: ' + str(e))

