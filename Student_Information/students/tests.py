from django.test import SimpleTestCase
from django.urls import reverse

class StudentFormTests(SimpleTestCase):
    def test_form_widgets(self):
        response = self.client.get(reverse("students:form"))
        for widget in ['type="text"', '<select', 'type="radio"', 'type="checkbox"', 'type="number"', '<textarea', 'type="submit"']:
            self.assertContains(response, widget)

    def test_blank_and_whitespace_required_fields(self):
        for value in ["", "   "]:
            response = self.client.post(reverse("students:results"), {
                "student_name": value, "student_id": value})
            self.assertContains(response, "Student Name cannot be blank.")
            self.assertContains(response, "Student ID cannot be blank.")
            self.assertTemplateUsed(response, "students/form.html")

    def test_success_multiple_languages_and_escaped_comments(self):
        response = self.client.post(reverse("students:results"), {
            "student_name": "Alex Smith", "student_id": "00123",
            "major": "Computer Science", "class_standing": "Sophomore",
            "languages": ["Python", "Java"], "graduation_year": "2028",
            "comments": "<script>alert(1)</script>"})
        self.assertTemplateUsed(response, "students/results.html")
        for text in ["Alex Smith", "00123", "Python, Java", "2028", "&lt;script&gt;"]:
            self.assertContains(response, text)
        self.assertNotContains(response, "<script>")

    def test_optional_fields_and_results_get(self):
        response = self.client.post(reverse("students:results"), {
            "student_name": "Alex", "student_id": "123"})
        self.assertContains(response, "None selected")
        self.assertRedirects(self.client.get(reverse("students:results")), reverse("students:form"))

    def test_invalid_year_preserves_input(self):
        response = self.client.post(reverse("students:results"), {
            "student_name": "Alex", "student_id": "123", "graduation_year": "bad"})
        self.assertTemplateUsed(response, "students/form.html")
        self.assertContains(response, "Enter a whole number.")
        self.assertContains(response, 'value="Alex"')
