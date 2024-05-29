# myapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
import requests

def index(request):
    # FastAPI 서버의 URL
    fastapi_url = "https://manseryuk-api-fsjoo.run.goorm.site/calendadata/"
    
    # 요청 매개변수 설정
    params = {
        "year": 1982,
        "month": "10",
        "day": "26",
        "sl": "음력",
        "gen": "male"
    }
    
    # FastAPI로 요청 보내기
    response = requests.get(fastapi_url, params=params)
    
    # 응답 데이터 처리
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Failed to retrieve data'}, status=response.status_code)
