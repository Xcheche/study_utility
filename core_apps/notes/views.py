from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic

from notes.forms import NoteForm

from .models import Note

#========================================
#================ Notes View ================
#=======================================
def notes(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = Note(
                # user=request.user,  # Uncomment if you're associating the note with a user
                title=form.cleaned_data["title"],
                content=form.cleaned_data["content"],
            )
            note.save()
         
            messages.success(request, "Note created successfully")
            return redirect("notes")
        else:
            messages.error(request, "Failed to create note")
    else:
        form = NoteForm()

    # Fetch notes for the current user (if you want to filter by user, uncomment the line below)
    notes = Note.objects.filter()

    # Pagination
    paginator = Paginator(notes, 2)  # 1 note per page
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)  # Get the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer, assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty, return the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        "form": form,
        "notes": page_obj.object_list,  # Only pass the notes for the current page
        "page_obj": page_obj,
    }
    return render(request, "notes/notes.html", context)


#===================================================#
#=============== Detail View =======================#
#===================================================#

class NoteDetailView(generic.DetailView):
    model = Note
    template_name = "notes/note_detail.html"
    context_object_name = "note"


#===================================================#
#=============== Update View =======================#
#===================================================#

class NoteUpdateView(generic.UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/notes.html"
    success_url = reverse_lazy("notes")
    context_object_name = "note"

    def form_valid(self, form):
        messages.success(self.request, "Note updated successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to update note")
        return super().form_invalid(form)
    


#====================================================#
#============================== Delete==============#
#===================================================#
class NoteDeleteView(generic.DeleteView):
    model = Note
    template_name = "notes/note_confirm_delete.html"
    success_url = reverse_lazy("notes")

    def delete(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)
            messages.success(request, "Note deleted successfully")
            return response
        except Exception as e:
            messages.error(request, f"Failed to delete note: {e}")
            return redirect("notes")
        
        
        
        
##====================================================#
#============================== Search Notes ==============#
#===================================================#
def search_notes(request):
    query = request.GET.get('q')
    if query:
        results = Note.objects.filter(title__icontains=query) | Note.objects.filter(content__icontains=query)
    else:
        results = Note.objects.none()

    context = {
        "query": query,
        "results": results,
    }
    return render(request, "notes/search_results.html", context)