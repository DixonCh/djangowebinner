from django.shortcuts import render,redirect
from news.models import News
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login
def home(request):
    context = {
        'news':News.objects.all()  # SELECT * FROM news
    }
    return render(request,'index.html',context)


def signin(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('signin')



def signup(request):
    if request.method=='GET':
        form = CustomUserCreationForm()
        context = {
            'form':form
        }
        return render(request,'signup.html',context)
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
            context = {
                'form':form,
            }
            return render(request,'signup.html',context)