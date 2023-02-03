from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from .forms import CreateNoteForm, UpdateNoteForm
from .models import Notes

# def notes_views_nikita(request):
#     context = {'notes': [{'Caption': 'my new note', 'text': 'buy milk'}, {'Caption': 'my new note', 'text': 'buy milk'}]}
#     return render(request, 'notes_nikita/index.html', context=context)
# Create your views here.
def notes_views_nikita(request):
    notes = Notes.objects.all()
    context = {'notes': notes}
    print(context)
    return render(request, 'index.html', context=context)





def create_note(request):
    if request.method == "POST":
        print('post')
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/notes-nikita/')
    else:
        form = CreateNoteForm()
    context = {'form': form}
    return render(request, 'create_note.html', context=context)

def update_note(request, note_id):
    instance = get_object_or_404(Notes, id=note_id)
    form = UpdateNoteForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/notes-nikita/')

    return render(request, 'update_note.html', {'form': form})

def delete_note(request, note_id):
    instance = get_object_or_404(Notes, id=note_id)
    instance.delete()
    return HttpResponseRedirect('/notes-nikita/')
