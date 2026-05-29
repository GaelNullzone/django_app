from django.shortcuts import redirect, render

EMPLOYEES = []
GENDER_CHOICES = ["Female", "Male", "Non-binary", "Prefer not to say"]


def employee_list(request):
    error = ""

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        gender = request.POST.get("gender", "").strip()

        if not name:
            error = "Please enter an employee name."
        elif gender not in GENDER_CHOICES:
            error = "Please select a valid gender."
        else:
            EMPLOYEES.append({"name": name, "gender": gender})
            return redirect("employee_list")

    return render(
        request,
        "employees/index.html",
        {
            "employees": EMPLOYEES,
            "gender_choices": GENDER_CHOICES,
            "error": error,
        },
    )
