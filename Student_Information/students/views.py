from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_http_methods
from .forms import StudentForm

@require_GET
def student_form(request):
    return render(request, "students/form.html", {"form": StudentForm()})

@require_http_methods(["GET", "POST"])
def student_results(request):
    if request.method != "POST":
        return redirect("students:form")

    # Clicking Submit sends a POST request to this event handler.
    form = StudentForm(request.POST)
    if form.is_valid():
        # cleaned_data contains validated values, including all checked languages.
        return render(request, "students/results.html", {"student": form.cleaned_data})

    # A bound form preserves previous input and displays validation messages.
    return render(request, "students/form.html", {"form": form})
