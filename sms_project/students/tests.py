from django.test import TestCase
from .models import Student

class StudentModelTest(TestCase):

    def test_student_creation(self):
        student = Student.objects.create(
            full_name='N Jhansi mahalakshmi',
            roll_number='4KV22CI030',
            email='jpnd1508@gmail.com',
            phone='7483930439',
            department='Computer Science (AI & ML)',
            course='B.Tech',
            year='4th Year',
            date_of_birth='2003-08-15'
        )

        self.assertEqual(student.full_name, 'N Jhansi mahalakshmi')