# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Achievement(models.Model):
    achievement_id = models.AutoField(db_column='Achievement_id', primary_key=True)  # Field name made lowercase.
    events_name = models.CharField(db_column='Events_name', max_length=64)  # Field name made lowercase.
    description_of_the_achievement = models.TextField(db_column='Description_of_the_Achievement')  # Field name made lowercase. This field type is a guess.
    certificate = models.BinaryField(db_column='Certificate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Achievement'


class Company(models.Model):
    company_id = models.AutoField(db_column='Company_id', primary_key=True)  # Field name made lowercase.
    company_name = models.CharField(db_column='Company_name', max_length=32)  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Company'


class Direction(models.Model):
    direction_id = models.AutoField(db_column='Direction_id', primary_key=True)  # Field name made lowercase.
    direction_name = models.CharField(db_column='Direction_name', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Direction'


class Education(models.Model):
    education_id = models.AutoField(db_column='Education_id', primary_key=True)  # Field name made lowercase.
    student = models.ForeignKey('Student', models.DO_NOTHING, db_column='Student_id')  # Field name made lowercase.
    specialization = models.ForeignKey('Specialization', models.DO_NOTHING, db_column='Specialization_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Education'


class Employer(models.Model):
    employer_id = models.AutoField(db_column='Employer_id', primary_key=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=32)  # Field name made lowercase.
    employer_name = models.CharField(db_column='Employer_name', max_length=32)  # Field name made lowercase.
    middlename = models.CharField(db_column='Middlename', max_length=32)  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=25)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=15)  # Field name made lowercase.
    company = models.ForeignKey(Company, models.DO_NOTHING, db_column='Company_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Employer'


class Events(models.Model):
    events_id = models.AutoField(db_column='Events_id', primary_key=True)  # Field name made lowercase.
    events_name = models.CharField(db_column='Events_name', max_length=64)  # Field name made lowercase.
    events_type = models.CharField(db_column='Events_type', max_length=32)  # Field name made lowercase.
    events_data = models.DateTimeField(db_column='Events_data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Events'


class Faculty(models.Model):
    faculty_id = models.AutoField(db_column='Faculty_id', primary_key=True)  # Field name made lowercase.
    faculty_name = models.CharField(db_column='Faculty_name', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Faculty'


class Group(models.Model):
    group_id = models.AutoField(db_column='Group_id', primary_key=True)  # Field name made lowercase.
    group_name = models.CharField(db_column='Group_name', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Group_'


class ListOfAchievementsreferences(models.Model):
    list_of_achievementsreferences_id = models.AutoField(db_column='List_of_Achievementsreferences_id', primary_key=True)  # Field name made lowercase.
    achievement = models.ForeignKey(Achievement, models.DO_NOTHING, db_column='Achievement_id')  # Field name made lowercase.
    student = models.ForeignKey('Student', models.DO_NOTHING, db_column='Student_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'List_of_Achievementsreferences'


class Profile(models.Model):
    profile_id = models.AutoField(db_column='Profile_id', primary_key=True)  # Field name made lowercase.
    profile_name = models.CharField(db_column='Profile_name', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Profile'


class Project(models.Model):
    project_id = models.AutoField(db_column='Project_id', primary_key=True)  # Field name made lowercase.
    project_name = models.CharField(db_column='Project_name', max_length=64)  # Field name made lowercase.
    project_description = models.TextField(db_column='Project_description')  # Field name made lowercase. This field type is a guess.
    project_content = models.TextField(db_column='Project_content')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Project'


class ProjectList(models.Model):
    project_list_id = models.AutoField(db_column='Project_list_id', primary_key=True)  # Field name made lowercase.
    project = models.ForeignKey(Project, models.DO_NOTHING, db_column='Project_id')  # Field name made lowercase.
    student = models.ForeignKey('Student', models.DO_NOTHING, db_column='Student_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Project_list'


class Skills(models.Model):
    skills_id = models.AutoField(primary_key=True)
    skills_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'Skills'


class Specialization(models.Model):
    specialization_id = models.AutoField(db_column='Specialization_id', primary_key=True)  # Field name made lowercase.
    profile = models.ForeignKey(Profile, models.DO_NOTHING, db_column='Profile_id')  # Field name made lowercase.
    faculty = models.ForeignKey(Faculty, models.DO_NOTHING, db_column='Faculty_id')  # Field name made lowercase.
    direction = models.ForeignKey(Direction, models.DO_NOTHING, db_column='Direction_id')  # Field name made lowercase.
    events = models.ForeignKey(Events, models.DO_NOTHING, db_column='Events_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Specialization'


class Student(models.Model):
    student_id = models.AutoField(db_column='Student_id', primary_key=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=32)  # Field name made lowercase.
    student_name = models.CharField(db_column='Student_name', max_length=32)  # Field name made lowercase.
    middlename = models.CharField(db_column='Middlename', max_length=32)  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=25)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=15)  # Field name made lowercase.
    group = models.ForeignKey(Group, models.DO_NOTHING, db_column='Group_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student'


class Vacancy(models.Model):
    vacancy_id = models.AutoField(db_column='Vacancy_id', primary_key=True)  # Field name made lowercase.
    vacancy_name = models.CharField(db_column='Vacancy_name', max_length=32)  # Field name made lowercase.
    post = models.CharField(db_column='Post', max_length=32)  # Field name made lowercase.
    requirements = models.TextField(db_column='Requirements')  # Field name made lowercase. This field type is a guess.
    company = models.ForeignKey(Company, models.DO_NOTHING, db_column='Company_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vacancy'


class Work(models.Model):
    work_id = models.AutoField(db_column='Work_id', primary_key=True)  # Field name made lowercase.
    student = models.ForeignKey(Student, models.DO_NOTHING, db_column='Student_id')  # Field name made lowercase.
    vacancy = models.ForeignKey(Vacancy, models.DO_NOTHING, db_column='Vacancy_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Work'


class AuthGroup(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
