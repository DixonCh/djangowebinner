from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Category,News
# Create your views here.
@login_required(login_url='signin')
def dashboard(request):
    context = {
        'news':News.objects.filter(created_by=request.user)
    }
    return render(request,'dashboard.html',context)

def createNews(request):
    if request.method=='GET':
        context = {
            'cat':Category.objects.all()
        }
        return render(request,'create_news.html',context)
    else:
        t = request.POST.get('title')
        c = request.POST.get('content')
        i = request.FILES.get('image')
        cat = request.POST.get('cat')
        n = News(title=t,content=c,image=i,category_id=cat,created_by_id=request.user.id)
        n.save()
        return redirect('dashboard')
