from django.db import models

# Create your models here.


class Student(models.Model):
    student_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.student_name


class Section(models.Model):
    student = models.OneToOneField(
        Student, on_delete=models.CASCADE, related_name="section")
    select_section = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("E", "E")
    )
    section_name = models.CharField(max_length=10, choices=select_section)


class Course(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="course")
    course_name = models.CharField(max_length=100, default="")


class Subject(models.Model):
    select_subject = (
        ("Hindi", "Hindi"),
        ("English", "English"),
        ("Math", "Math"),
        ("Physics", "Physics"),
        ("Social Science", "Social Science"),
        ("Chemistry", "Chemistry"),
    )
    student = models.ManyToManyField(Student, related_name="subject")
    subject_name = models.CharField(max_length=30, choices=select_subject)

    def all_name(self):
        return ", ".join([str(i) for i in self.student.all()])

    # class Meta:
    #     abstract = True
