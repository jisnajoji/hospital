from . models import *
from . views import *

def count(request):
    item_count=0
    if 'admin' in request.path:
        return()
    else:
        try:
            ct=Booklist.objects.filter(book_id=b_id(request))
            cti=Bkd_doc.objects.all().filter(booking=ct[:1])
            for c in cti:
                item_count+=1
        except Booklist.DoesNotExist:
            item_count=0
    return dict(itc=item_count)