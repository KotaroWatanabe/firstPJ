from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# ----IMPORT MODEL
from .models import Friend
from .models import ANKENTBL

# ----IMPORT FORM
from .forms import HelloForm
from .forms import FriendForm
from .forms import ANKENTBLForm
# from .forms import FriendForm,ANKENTBLForm,ANKENDTLTBLForm,\
# ICHIRANTBLForm,USERTBLForm,HYOKATBLForm,KOUMOKUMForm


def index(request):
    data = Friend.objects.all()

    params = {
        'title': 'Hello',
        'data': data,
    }
    return render(request, 'hello/index.html', params)

# create model


def create(request):

    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hellloooo',
        'form': FriendForm(),
    }
    return render(request, 'hello/create.html', params)


def edit(request, num):
    obj = Friend.objects.get(id=num)

    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hellloooo',
        'id': num,
        'form': FriendForm(instance=obj),
    }
    return render(request, 'hello/edit.html', params)


def delete(request, num):
    friend = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
        'title': 'Hellloooo',
        'id': num,
        'obj': friend,
    }
    return render(request, 'hello/delete.html', params)

# ------START


def mainpage(request):
    data1 = ANKENTBL.objects.all()

    params = {
        'title': 'Hello',
        'data1': data1,
    }
    return render(request, 'hello/mainpage.html', params)

# def detailpj (request):
#     data2 = ANKENTBL.objects.all()

#     params = {
#             'title':'Hello',
#             'data2': data2,
#             }
#     return render(request,'hello/detailpj.html', params)

# def yourprof (request):
#     data3 = ANKENTBL.objects.all()

#     params = {
#             'title':'Hello',
#             'data3': data3,
#             }
#     return render(request,'hello/yourprof.html', params)

# def jfinal (request):
#     data4 = ANKENTBL.objects.all()

#     params = {
#             'title':'Hello',
#             'data4': data4,
#             }
#     return render(request,'hello/jfinal.html', params)

# def loginpage (request):
#     data5 = ANKENTBL.objects.all()

#     params = {
#             'title':'Hello',
#             'data5': data5,
#             }
#     return render(request,'hello/loginpage.html', params)


def mypage(request):
    # data6 = ANKENTBL.objects.all()

    params = {
        'title': 'Hello',
        # 'data6': data6,
    }
    return render(request, 'hello/mypage.html', params)


def makepj(request):
    data7 = ANKENTBLForm.objects.all()

    params = {
        'title': 'Hello',
        'data7': data7,
    }
    return render(request, 'hello/makepj.html', params)

# def jlist (request):
#     data8 = ANKENTBL.objects.all()

#     params = {
#             'title':'Hello',
#             'data8': data8,
#             }
#     return render(request,'hello/jlist.html', params)


# def wantlist (request):
#     data9 = ANKENTBL.objects.all()

#     params = {
#             'title':'Hello',
#             'data9': data9,
#             }
#     return render(request,'hello/wantlist.html', params)

# def makeprof (request):
#     data10 = ANKENTBL.objects.all()

#     params = {
#             'title':'Hello',
#             'data10': data10,
#             }
#     return render(request,'hello/makeprof.html', params)

# def jhlist (request):
#     data11 = ANKENTBL.objects.all()

#     params = {
#             'title':'Hello',
#             'data11': data11,
#             }
#     return render(request,'hello/jhlist.html', params)

# def jreal (request):
#     data12 = ANKENTBL.objects.all()

#     params = {
#             'title':'Hello',
#             'data12': data12,
#             }
#     return render(request,'hello/jreal.html', params)

# def mdlreview (request):
#     data13 = ANKENTBL.objects.all()

#     params = {
#             'title':'Hello',
#             'data13': data13,
#             }
#     return render(request,'hello/mdlreview.html', params)

# def finreview (request):
#     data14 = ANKENTBL.objects.all()

#     params = {
#             'title':'Hello',
#             'data14': data14,
#             }
#     return render(request,'hello/finreview.html', params)

# def bothreview (request):
#     data15 = ANKENTBL.objects.all()

#     params = {
#             'title':'Hello',
#             'data15': data15,
#             }
#     return render(request,'hello/bothreview.html', params)

# def hreal (request):
#     data16 = ANKENTBL.objects.all()

#     params = {
#             'title':'Hello',
#             'data16': data16,
#             }
#     return render(request,'hello/hreal.html', params)


# def mainpage(request, num):
#    friend = Friend.objects.get(id=num)
#    if  (request.method == 'POST'):
#        friend.delete()
#        return redirect(to='/hello')
#    params ={
#        'title' : 'Hellloooo',
#        'id' :num,
#        'obj': friend,
#            }
#    return render(request, 'hello/delete.html', params)
