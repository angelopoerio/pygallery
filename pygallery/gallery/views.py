from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from gallery.models import Picture
from gallery.forms import UploadPictureForm

def upload_view(request):
	if request.method == 'POST':
		form = UploadPictureForm(request.POST, request.FILES)
		if form.is_valid():
			img = request.FILES['image']
			notes = request.POST['notes']
			new_picture = Picture(image=img, 
					      notes=notes)
			new_picture.save()
			return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/err')			

def add_picture(request):
	return render(request, "upload.html")

def main_view(request):
    	picture_list = Picture.objects.all()
    	paginator = Paginator(picture_list, 9)

   	page = request.GET.get('page')
    	try:
        	pictures = paginator.page(page)
    	except PageNotAnInteger:
        	pictures = paginator.page(1)
    	except EmptyPage:
        	pictures = paginator.page(paginator.num_pages)
    	return render(request, 'index.html', {"pictures": pictures})

def err_view(request):
	return render(request, 'err.html')
	
def detail_view(request, id):
	picture = get_object_or_404(Picture, pk=id)
	return render(request, 'detail.html', {'picture': picture})

def delete_view(request, id):
	picture = get_object_or_404(Picture, pk=id)
	picture.delete()
	return redirect('/')
