from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from homework.models import Homework
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, UpdateView
from homework.forms import HomeworkForm

# Create your views here.

#=============================================
#========== Homework View ===================
#=============================================
# class HomeworkView(generic.ListView, FormView):
#     model = Homework
#     template_name = "homework/homework.html"
#     context_object_name = "homework"
#     paginate_by = 5
#     form_class = HomeworkForm
#     success_url = reverse_lazy('homework')
    
#     def homework_done(self):
#         return Homework.objects.filter(done=True)
    
#     def homework_not_done(self):
#         return Homework.objects.filter(done=False)
    
#     def form_valid(self, form):
#         form.save()
#         messages.success(self.request, f'Homework added successfully by {self.request.user}')
#         return super().form_valid(form)

def homework_view(request):
# Handle form submission
    if request.method == "POST":
        form = HomeworkForm(request.POST)
        if form.is_valid():
            homework = form.save(commit=False)
            homework.user = request.user
            homework.save()
            messages.success(request, "Homework added successfully")
            return redirect("homework")  # reload the same page
    else:
        form = HomeworkForm()

    # Query homework for this user
    homework_not_done = Homework.objects.filter(user=request.user, is_finished=False)
    homework_done = Homework.objects.filter(user=request.user, is_finished=True)

    context = {
        "form": form,
        "homework": homework_not_done,  # for looping in the template
        "homework_not_done": homework_not_done,
        "homework_done": homework_done,
    }

    return render(request, "homework/homework.html", context)

#=============================================#
#========== Homework Update View =============#
#=============================================#
class HomeworkUpdateView(UpdateView):
    model = Homework
    form_class = HomeworkForm
    template_name = "homework/homework_update.html"
    success_url = reverse_lazy('homework')


    def home_work_done(self):
        return Homework.objects.filter(done=True)
    
    def  home_work_not_done(self):
        return Homework.objects.filter(done=False)
    
    def form_valid(self, form):
        messages.info(self.request, f'Homework updated successfully by {self.request.user}')
        return super().form_valid(form) 
    


#=======================================================#
#=======================Delete Homework=================#
# ======================================================#
class HomeworkDeleteView(generic.DeleteView):
    model = Homework
    template_name = "homework/homework_confirm_delete.html"
    success_url = reverse_lazy('homework')

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, f'Homework deleted successfully by {self.request.user}')
        return super().delete(request, *args, **kwargs)      