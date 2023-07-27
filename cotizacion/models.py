from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.

class Insumo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Color(models.Model):
    color = models.CharField(max_length=15)

    def __str__(self):
        return self.color


class Tipo(models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo


class Ventana(models.Model):
    ancho = models.DecimalField(max_digits=5, decimal_places=2)
    alto = models.DecimalField(max_digits=5, decimal_places=2)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Ventana tipo: {self.tipo} Color: {self.color} - Ancho: {self.ancho} - Alto: {self.alto}"
    

class Presupuesto(models.Model):
    numero_presupuesto = models.PositiveBigIntegerField(
        null=True, blank=True, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ventanas = models.ManyToManyField(Ventana, through='DetallePresupuesto')
    def __str__(self):
        return f"Numero Presupuesto: {self.numero_presupuesto} - Cliente: {self.cliente}"
    
class DetallePresupuesto(models.Model):
    presupuesto=models.ForeignKey(Presupuesto, on_delete=models.CASCADE)
    ventana=models.ForeignKey(Ventana, on_delete=models.CASCADE)
    cantidad=models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.presupuesto} - {self.ventana} - Cantidad: {self.cantidad}"



@receiver(pre_save, sender=Presupuesto)
def numerador_presupuesto(sender, instance, **kwargs):
    if not instance.numero_presupuesto:
        ultimo_numero_presupuesto = Presupuesto.objects.all().order_by(
            '-numero_presupuesto').first()
        print(ultimo_numero_presupuesto)
        if ultimo_numero_presupuesto:
            instance.numero_presupuesto = ultimo_numero_presupuesto.numero_presupuesto + 1
        else:
            instance.numero_presupuesto = 1


"""
class Cliente(models.Model):
    nombre_cliente=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre_cliente

class Presupuesto(models.Model):
    COMUN = 1
    VIP = 2
    ROLE_CHOICE = (
        (COMUN, 'Cliente Comun'),
        (VIP, 'Cliente VIP'),
    )
    id = models.AutoField(primary_key=True)
    numero= models.IntegerField(unique=True)
    nombre_cliente=models.OneToOneField(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    
    # required fields
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    is_completed= models.BooleanField(default=False)

    class Meta:
        ordering=['nombre_cliente', 'numero']
    
    def __str__(self):
        return f'Nombre: {self.nombre_cliente} - Numero Presupuesto: {self.numero}'
"""

"""
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email')
        if not username:
            raise ValueError('User must have a username')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        # lo salva en la base de datos no en una nueva si le pongo using=self._db
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    RESTAURANT = 1
    CUSTOMER = 2
    ROLE_CHOICE = (
        (RESTAURANT, 'Restaurant'),
        (CUSTOMER, 'Cliente'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICE, blank=True, null=True)
    
    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True)
    cover_photo = models.ImageField(upload_to='users/cover_photos', blank=True, null=True)
    address_line1 = models.CharField(max_length=50, blank=True, null=True)
    address_line2 = models.CharField(max_length=50, blank=True, null=True)
    country= models.CharField(max_length=15, blank=True, null=True)
    state= models.CharField(max_length=15, blank=True, null=True)
    city= models.CharField(max_length=15, blank=True, null=True)
    pin_code= models.CharField(max_length=6, blank=True, null=True)
    latitude= models.CharField(max_length=20, blank=True, null=True)
    longitude= models.CharField(max_length=20, blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    modified_at= models.DateTimeField(auto_now=True)


"""
# Create your models here.
