from django.shortcuts import render

def index(request):
    return render(request, 'mysite/templates/mainApp/homePage.html', locals())

def contact(request):
    return render(request, 'mysite/templates/mainApp/basic.html', {'values': ['Если у Вас остались вопросы, то задавайте их мне по телефону','(068) 068-68-68']}, locals())
# Create your views here.
