# myapp/views.py
from django.shortcuts import render
from .calculator import determine_zodiac_hour_str
from .forms import PersonForm
from .models import Person
from datetime import datetime
from django.http import JsonResponse
import requests

def index(request):
    # FastAPI 서버의 URL
    fastapi_url = "https://namaste23.cafe24.com/calendadata/"
    submitForm = PersonForm(request.POST or None)
    
    if request.method == "POST":
        # 제출된 폼 검증
        if submitForm.is_valid(): 
            obj = submitForm.save(commit=False)            
            time = determine_zodiac_hour_str(obj.hour, obj.min)
            # 요청 매개변수 설정
            params = {
                "year": int(obj.year),
                "month": obj.month,
                "day": obj.day,
                "time": time,
                "sl": obj.sl,
                "gen": obj.gen
            }
            # FastAPI로 요청 보내기
            response = requests.get(fastapi_url, params=params)
            
            # 응답 데이터 처리
            if response.status_code == 200:
                data = response.json()
                grouped_chunks = data['cycles_100']
                current_year = datetime.now().year
                groups_with_visibility = []
                grouped_data_visibility = []
                for group in grouped_chunks:
                    visible = any(year == current_year for year, _, _ in group)
                    groups_with_visibility.append((group, visible))
                    grouped_data_visibility.append(visible)
                grouped_data = zip(
                        data['daewoon_num_list'],
                        data['daewoon'][1],
                        data['daewoon'][2],
                        grouped_data_visibility
                    )
                all_false = all(not value for value in grouped_data_visibility)
                context = {
                    'obj':obj,
                    'datas': data,
                    'grouped_data': grouped_data,
                    'groups_with_visibility': groups_with_visibility,
                    'all_false': all_false,
                }
                return render(request, 'base/home_result.html', context)  
            else:
                return JsonResponse({'error': 'Failed to retrieve data'}, status=response.status_code)

    # GET 요청 또는 유효하지 않은 폼의 경우 초기 폼 표시
    context = {'submit': submitForm}
    return render(request, 'base/home.html', context)
     