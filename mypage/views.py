from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def mypage(request):
    # 🔧 DB 연결 전 임시 데이터
    reservations = []
    visits = []

    return render(request, 'mypage/mypage.html', {
        'reservations': reservations,
        'visits': visits,
    })