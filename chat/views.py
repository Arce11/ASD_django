from django.shortcuts import render


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'chat/error.html')
    return render(request, 'chat/index.html', context=locals())


def room(request, room_name):
    if not request.user.is_authenticated:
        return render(request, 'chat/error.html')

    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

