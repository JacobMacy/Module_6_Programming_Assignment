from django import forms

class StudentForm(forms.Form):
    # CharField strips whitespace and rejects blank required values.
    student_name = forms.CharField(
        label="Student Name", max_length=100,
        error_messages={"required": "Student Name cannot be blank."})
    student_id = forms.CharField(
        label="Student ID", max_length=30,
        error_messages={"required": "Student ID cannot be blank."})
    major = forms.ChoiceField(required=False, choices=[
        ("", "Select a major"), ("Computer Science", "Computer Science"),
        ("Business", "Business"), ("Engineering", "Engineering"),
        ("Nursing", "Nursing"), ("Undecided", "Undecided")])
    class_standing = forms.ChoiceField(
        label="Class Standing", required=False, widget=forms.RadioSelect,
        choices=[(s, s) for s in ["Freshman", "Sophomore", "Junior", "Senior"]])
    languages = forms.MultipleChoiceField(
        label="Programming Languages Known", required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[(s, s) for s in ["Python", "Java", "JavaScript", "C++", "C#"]])
    graduation_year = forms.IntegerField(
        label="Expected Graduation Year", required=False,
        min_value=1900, max_value=9999, widget=forms.NumberInput)
    comments = forms.CharField(required=False, max_length=2000,
                               widget=forms.Textarea(attrs={"rows": 4}))
