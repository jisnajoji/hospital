from django.shortcuts import render,redirect,get_object_or_404
from dean.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist

def book_details(request,tot=0,count=0,cart_items=None):
     
     try:
         ct=Booklist.objects.get(book_id=b_id(request))
         ct_items=Bkd_doc.objects.filter(booking=ct,active=True)
         for i in ct_items:
             tot += (i.doct.con_fee)
             count += 1
     except ObjectDoesNotExist:
        pass
     return render(request,'booking.html',{'ci':ct_items,'t':tot,'cn':count})

def b_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id

def add_book(request,doct_id):
    prodt=doctor.objects.get(id=doct_id)
    s_item=doctor.objects.get(id=doct_id)
    # prodt.stock-=1
    try:
        ct=Booklist.objects.get(book_id=b_id(request))
    except Booklist.DoesNotExist:
        ct=Booklist.objects.create(book_id=b_id(request))
        s_item.max_book-=1
        ct.save()
    try:
        c_items=Bkd_doc.objects.get(doct=prodt,booking=ct)
        # print(c_items.prodt.name)
        # s_item.stock-=1
        if 1 < c_items.doct.max_book:
            s_item.max_book-=1
            # print(s_item.stock)
            # c_items.quan+=1
            # print(c_items.quan)
            # c_items.save()
            s_item.save()
    except Bkd_doc.DoesNotExist:
        c_items=Bkd_doc.objects.create(doct=prodt,booking=ct)
        s_item.max_book-=1
        c_items.save()
        s_item.save()
    return redirect('bookDetails')    
    

def book_delete(request,doct_id):
     ct=Booklist.objects.get(book_id=b_id(request))
     doct=get_object_or_404(doctor,id=doct_id)
     s_item=doctor.objects.get(id=doct_id)
     c_items=Bkd_doc.objects.get(doct=doct,booking=ct)
     s_item.max_book+=1
     s_item.save()
     c_items.delete()
     return redirect('bookDetails')