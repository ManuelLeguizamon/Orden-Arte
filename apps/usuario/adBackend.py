from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from ldap3 import Server, Connection, ALL

class ActiveDirectoryBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        # Servidor AD vinculado
        server = Server("192.168.0.55", get_info=ALL)

        user_upn = f"{username}@ifts.local"

        try:
            conn = Connection(
                server,
                user=user_upn,
                password=password,
                authentication="SIMPLE"
            )

            # Bind (login al AD)
            if not conn.bind():
                return None 

            # Si autenticó bien → obtener o crear usuario Django
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_unusable_password()
                user.save()

            return user

        except Exception as e:
            print("ERROR AUTH AD:", e)
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
