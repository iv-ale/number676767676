from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import NoteForm
from .models import Note


def home(request):
    notes = Note.objects.select_related("author")
    return render(request, "notes/home.html", {"notes": notes})


@login_required
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect("profile")
    else:
        form = NoteForm()
    return render(request, "notes/note_form.html", {"form": form})
