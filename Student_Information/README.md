# Student Information — Django assignment

## Run on Windows
1. Extract this ZIP (do not run from inside the ZIP).
2. Open the extracted Student_Information folder in VS Code.
3. Open Terminal > New Terminal. Make sure manage.py is in this folder.
4. Run:

```powershell
py -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe manage.py runserver
```

5. Open http://127.0.0.1:8000/ in your browser.
6. Stop the server with Ctrl+C.

Python 3.10 or newer is required. No virtual environment activation or database migration is needed for this form-only app. No records are saved to a database.

macOS/Linux: use `python3 -m venv .venv`, then `.venv/bin/python` in place of `.venv\Scripts\python.exe` in the two remaining commands.

## How it works
- student_project/urls.py connects the project to the students application.
- students/urls.py maps / to the form view and /results/ to the submission view.
- students/forms.py defines each field and its HTML widget. Name and ID are required; all other fields are optional. Whitespace-only names and IDs are rejected. The ID stays text so leading zeros are preserved.
- students/views.py handles requests. Clicking Submit causes the browser to send a POST request. The view validates it with is_valid(). Invalid input returns the form with errors and the previous values. Valid input is passed through cleaned_data to the results template.
- students/templates/students/form.html displays the input form.
- students/templates/students/results.html displays the summary, including comments.
- The CSRF token protects form submissions; template autoescaping keeps user input as text.
- students/static/students/style.css supplies simple styling.

This is event-driven programming: the Submit event triggers an HTTP request, and the view handles that request. JavaScript is not required.

## Check your assignment
- Submit an empty form: errors must appear for both Name and ID.
- Submit spaces for either required field: it must be rejected.
- Complete the form and select several languages: verify every selection appears in the summary.
- Leave optional fields empty: the summary should use readable placeholders.
- Try an invalid graduation year: the form should show an error.

To run the included automated checks:
```powershell
.venv\Scripts\python.exe manage.py test
```

If screenshots are requested, capture the filled form, a validation error, and the completed summary. Follow your instructor's submission instructions for source files.

Reference: https://docs.djangoproject.com/en/5.2/topics/forms/
