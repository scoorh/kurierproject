from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect

from tracking.models import Package
from .forms import NewEntryForm

# Create your views here.
def index(request):
    '''open index page with 2 buttons'''
    return render(request, 'tracking/index.html')

def track_start(request):
    '''open new page for package tracking purpose'''
    return render(request, 'tracking/trackform.html', {'newcall': 'true'})

def track_id(request, id):
    '''open page with tracking data in table'''
    id = request.GET.get('id')
    noResult = 0

    try:
        result = Package.objects.filter(package_id=id).order_by('-change_date')
        if not result:
            noResult = 1
    except:
        noResult = 1

    context = { 'track_list' : result, 'no_result' : noResult }
    return render(request, 'tracking/trackform.html', context)

def create_start(request):
    '''open page with form for creating new data'''
    form = NewEntryForm()
    return render(request, 'tracking/createform.html', {'form': form})

def create_pck(request):
    '''redirect to index after post'''
    form = NewEntryForm(request.POST);
    if form.is_valid():
        entry = Package()
        entry.package_id = form.cleaned_data['package_id']
        entry.change_date = form.cleaned_data['change_date']
        entry.place = form.cleaned_data['place']
        entry.message = form.cleaned_data['message']
        try:
            entry.save()
        except:
            return render(request, 'tracking/createform.html', {'form': form})

        return HttpResponseRedirect('/tracking')
    else:
        return render(request, 'tracking/createform.html', {'form': form})
