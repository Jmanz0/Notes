from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home_view(request):
	if request.user.is_authenticated:
		user = request.user
		notes = Note.objects.filter(user = user)
	else:
		notes = Note.objects.filter(user = None)
	return render(request, 'note_list.html', { 'notes' : notes })

def delete_view(request, id):
	note = get_object_or_404(Note, id = id)
	note.delete()
	return redirect('../../')

def update_view(request, id):
	note = get_object_or_404(Note, id = id)
	note.title = request.POST['title']
	note.description = request.POST['description']
	note.tag = request.POST['tag']
	note.time = datetime.now()
	note.save()
	return redirect('../../')

def create_view(request):
	item = Note()
	if request.user.is_authenticated:
		item.user = request.user
	item.save()
	return redirect('../')

def filter_view(request):
	filt = request.POST['tag']
	notes = Note.objects.filter(tag = filt)
	return render(request, 'note_list.html', { 'notes' : notes })

def login_page_view(request):
	page = 'login'
	if request.method == 'POST':
		un = request.POST['username']
		pw = request.POST['password']
		user = authenticate(request, username = un, password = pw)
		if user is not None:
			login(request, user)
			return redirect('../')
	return render(request, 'login.html', {'page' : page})

def logout_user(request):
	logout(request)
	return redirect('note-list')


def register_user(request):
	page = 'register'
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit = False)
			user.save() 
			user = authenticate(request, username = user.username, password = request.POST['password1'])

			if user is not None:
				login(request, user)
				return redirect('note-list')
	else:
		form = UserCreationForm()
	context = {'form': form, 'page': page}
	return render(request,'login.html', context)

