from django.shortcuts import render
from django.http import HttpResponse 
#from django.shortcuts import redirect
#from .models import Friend
from .forms import HelloForm
#from .forms import FriendForm
#from .forms import FindForm

def index (request):
    params = {
            'title':'★副業サイト★',
            'msg': 'なにをする？？',
            'form': HelloForm()
            }
    if (request.method == 'POST'):
        params['message'] = '名前' + request.POST['name'] + \
            '<br>メール:' + request.POST['mail'] + \
            '<br>年齢:' + request.POST['age']
        params['form'] = HelloForm(request.POST)
    return render(request,'hello/mainpage.html', params)

## create model
#    
#def form(request):
#    msg = request.POST['msg']
#    params ={
#        'title' : 'Hellloooo★',
#        'msg': 'こんにちは' + msg + 'さん',
#            }
#    return render(request, 'hello/index.html', params)