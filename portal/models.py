from django.db import models


class Animalloss(models.Model):
    id = models.IntegerField(primary_key=True)
    animal_killed = models.IntegerField(blank=True, null=True)
    habitat_loss = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'animalloss'


class Humanloss(models.Model):
    id = models.IntegerField(primary_key=True)
    male_death = models.IntegerField(blank=True, null=True)
    female_death = models.IntegerField(blank=True, null=True)
    injured = models.IntegerField(blank=True, null=True)
    affected_family = models.IntegerField(blank=True, null=True)
    dispalced_male = models.IntegerField(blank=True, null=True)
    dispalced_female = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'humanloss'


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    tole = models.CharField(db_column='Tole', max_length=40, blank=True, null=True)  # Field name made lowercase.
    municipiality = models.CharField(db_column='Municipiality', max_length=40, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'


class Propertyloss(models.Model):
    id = models.IntegerField(primary_key=True)
    fully_damaged_building = models.IntegerField(blank=True, null=True)
    partially_damaged_building = models.IntegerField(blank=True, null=True)
    estimated_loss = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propertyloss'

class Disaster(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=40, blank=True, null=True)
    source = models.CharField(max_length=30, blank=True, null=True)
    animallossid = models.ForeignKey(Animalloss, models.DO_NOTHING, db_column='AnimalLossID', blank=True, null=True)  # Field name made lowercase.
    propertylossid = models.ForeignKey('Propertyloss', models.DO_NOTHING, db_column='PropertyLossID', blank=True, null=True)  # Field name made lowercase.
    humanlossid = models.ForeignKey('Humanloss', models.DO_NOTHING, db_column='HumanLossID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disaster'


class Disastergroup(models.Model):
    category = models.CharField(max_length=40, blank=True, null=True)
    disaster_group = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disastergroup'


class Disastertype(models.Model):
    type = models.CharField(primary_key=True, max_length=40)
    category = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disastertype'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    action_flag = models.PositiveSmallIntegerField()
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
    id = models.BigAutoField(primary_key=True)
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

