from django.db import models


class Skills(models.Model):
    skills_id = models.AutoField(primary_key=True)
    skills_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'Skills'

    def __str__(self):
        return self.skills_name

class Group(models.Model):
    group_id = models.AutoField(db_column='Group_id', primary_key=True)  # Field name made lowercase.
    group_name = models.CharField(db_column='Group_name', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Group_'

    def __str__(self):
        return self.group_name


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

    def __str__(self):
        return self.surname


class Direction(models.Model):
    direction_id = models.AutoField(db_column='Direction_id', primary_key=True)  # Field name made lowercase.
    direction_name = models.CharField(db_column='Direction_name', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Direction'

    def __str__(self):
        return self.direction_name


class Profile(models.Model):
    profile_id = models.AutoField(db_column='Profile_id', primary_key=True)  # Field name made lowercase.
    profile_name = models.CharField(db_column='Profile_name', max_length=64)  # Field name made lowercase.

    def __str__(self):
        return self.profile_name

    class Meta:
        managed = False
        db_table = 'Profile'


class Faculty(models.Model):
    faculty_id = models.AutoField(db_column='Faculty_id', primary_key=True)  # Field name made lowercase.
    faculty_name = models.CharField(db_column='Faculty_name', max_length=64)  # Field name made lowercase.

    def __str__(self):
        return self.faculty_name

    class Meta:
        managed = False
        db_table = 'Faculty'


class Events(models.Model):
    events_id = models.AutoField(db_column='Events_id', primary_key=True)  # Field name made lowercase.
    events_name = models.CharField(db_column='Events_name', max_length=64)  # Field name made lowercase.
    events_type = models.CharField(db_column='Events_type', max_length=32)  # Field name made lowercase.
    events_data = models.DateTimeField(db_column='Events_data', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.events_name

    class Meta:
        managed = False
        db_table = 'Events'


class Specialization(models.Model):
    specialization_id = models.AutoField(db_column='Specialization_id', primary_key=True)  # Field name made lowercase.
    profile = models.ForeignKey(Profile, models.DO_NOTHING, db_column='Profile_id')  # Field name made lowercase.
    faculty = models.ForeignKey(Faculty, models.DO_NOTHING, db_column='Faculty_id')  # Field name made lowercase.
    direction = models.ForeignKey(Direction, models.DO_NOTHING, db_column='Direction_id')  # Field name made lowercase.
    events = models.ForeignKey(Events, models.DO_NOTHING, db_column='Events_id')  # Field name made lowercase.

    def __str__(self):
        return str(self.specialization_id)

    class Meta:
        managed = False
        db_table = 'Specialization'


class Education(models.Model):
    education_id = models.AutoField(db_column='Education_id', primary_key=True)  # Field name made lowercase.
    student = models.ForeignKey('Student', models.DO_NOTHING, db_column='Student_id')  # Field name made lowercase.
    specialization = models.ForeignKey('Specialization', models.DO_NOTHING,
                                       db_column='Specialization_id')  # Field name made lowercase.

    def __str__(self):
        return str(self.education_id)

    class Meta:
        managed = False
        db_table = 'Education'


class Achievement(models.Model):
    achievement_id = models.AutoField(db_column='Achievement_id', primary_key=True)  # Field name made lowercase.
    events_name = models.CharField(db_column='Events_name', max_length=64)  # Field name made lowercase.
    description_of_the_achievement = models.TextField(
        db_column='Description_of_the_Achievement')  # Field name made lowercase. This field type is a guess.
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


class ListOfAchievementsreferences(models.Model):
    list_of_achievementsreferences_id = models.AutoField(db_column='List_of_Achievementsreferences_id',
                                                         primary_key=True)  # Field name made lowercase.
    achievement = models.ForeignKey(Achievement, models.DO_NOTHING,
                                    db_column='Achievement_id')  # Field name made lowercase.
    student = models.ForeignKey('Student', models.DO_NOTHING, db_column='Student_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'List_of_Achievementsreferences'


class Project(models.Model):
    project_id = models.AutoField(db_column='Project_id', primary_key=True)  # Field name made lowercase.
    project_name = models.CharField(db_column='Project_name', max_length=64)  # Field name made lowercase.
    project_description = models.TextField(
        db_column='Project_description')  # Field name made lowercase. This field type is a guess.
    project_content = models.TextField(
        db_column='Project_content')  # Field name made lowercase. This field type is a guess.

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
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MainTask(models.Model):
    title = models.CharField(max_length=50)
    task = models.TextField()

    class Meta:
        managed = False
        db_table = 'main_task'