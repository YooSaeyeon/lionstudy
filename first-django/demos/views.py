from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculator(reqeust):
    #return HttpResponse('계산기 기능 구현 시작입니다.')
    
    # 데이터 확인
    num1 = reqeust.GET.get('num1')
    num2 = reqeust.GET.get('num2')
    operators = reqeust.GET.get('operators')
    
    #계산
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0
    
    #응답
    return render(reqeust, 'calculator.html', {'result': result})