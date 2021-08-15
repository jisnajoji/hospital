from dean.models import doctor,dept
from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
def home(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(dept,slug=c_slug)
        prodt=doctor.objects.filter(dept=c_page,available=True)#fK in products model
    else:
        prodt=doctor.objects.all().filter(available=True)
    ct=dept.objects.all()
    paginator=Paginator(prodt,4)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)
    # prod=products.objects.all()
    return render(request,'index.html',{'pr':prodt,'ct':ct,'pg':pro})


def doctDetails(request,c_slug,doct_slug):
    try:
        prod=doctor.objects.get(dept__slug=c_slug,slug=doct_slug)
    except Exception as e:
        raise e
    return render(request,'doctor.html',{'pr':prod})


def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=doctor.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request,'search.html',{'qr':query,'pr':prod})