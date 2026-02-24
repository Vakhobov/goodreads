from idlelib.rpc import response_queue

from django.contrib.auth.models import User
from django.template.defaultfilters import first
from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user

# Create your tests here.
class RegistrationTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(reverse("users:register"),
                         data={"username":"bakhrom",
                         "first_name":"Bakhrom",
                         "last_name":"Vakhobov",
                         "email":"bahromvakhobov@gmail.com",
                         "password":"paswwfkof"
                               }
        )

        user = User.objects.get(username="bakhrom")
        self.assertEqual(user.first_name, "Bakhrom")
        self.assertEqual(user.last_name, "Vakhobov")
        self.assertEqual(user.email, "bahromvakhobov@gmail.com")
        self.assertNotEqual(user.password, "paswwfkof")

    def test_required_fields(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "first_name": "Bakhrom",
                "email":"bahromvakhobov@gmail.com"
            }
        )

        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "username", "This field is required.")
        self.assertFormError(response, "form", "password", "This field is required.")

    def test_invalid_email(self):
        response = self.client.post(
            reverse("users:register"),
            data={"username": "bakhrom",
                  "first_name": "Bakhrom",
                  "last_name": "Vakhobov",
                  "email": "djdkmail.com",
                  "password": "paswwfkof"
                  }
        )
        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "email", "Enter a valid email address.")



    def test_unique_username(self):
        user = User.objects.create(username="bakhrom", first_name="Bakhrom")
        user.set_password("somepass")
        user.save()


        response = self.client.post(
            reverse("users:register"),
            data={"username": "bakhrom",
                  "first_name": "Bakhrom",
                  "last_name": "Vakhobov",
                  "email": "djdkmail.com",
                  "password": "paswwfkof"
                  }
        )
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)


        self.assertFormError(response, "form", "username", "A user with that username already exist.")


class LoginTestCase(TestCase):
    def setUp(self):
        self.db_user = User.objects.create(username="bakhrom", first_name="Bakhrom")
        self.db_user.set_password("somepass")
        self.db_user.save()
    def test_successful_login(self):
        self.client.post(
            reverse("users:login"),
            data={
                "username":"bakhrom",
                "password":"somepass"
            }
        )
        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_wrong_credentials(self):
        self.client.post(
            reverse("users:login"),
            data={
                "username": "bakhrom",
                "password": "somepass"
            }
        )

        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)
    def test_logout(self):
        self.client.post(
            reverse("users:login"),
            data={
                "username": "bakhrom",
                "password": "somepass"
            }
        )
        self.client.login(username="bahrom", password="somepass")
        self.client.get(reverse("users:logout"))
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)


class ProfileTestCase(TestCase):
    def test_login_request(self):
        response = self.client.get(reverse("users:profile"))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("users:login") + "?next=/users/profile/")

    def test_profile_details(self):
        user = User.objects.create(
            username='baxrom', first_name='bahrombek', last_name='vaxabov', email='haskd@gmail.com'
        )
        user.set_password("sonmpass")
        user.save()

        self.client.login(username='baxrom', password='sonmpass')

        response = self.client.get(reverse("users:profile"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, user.username)
        self.assertContains(response, user.first_name)
        self.assertContains(response, user.last_name)
        self.assertContains(response, user.email)

    def test_update_profile(self):
        user = User.objects.create(
            username="bahrom", first_name="bahrom", last_name="Vakhobov", email="bahrom@gmail.com"
        )
        user.set_password("somepass")
        user.save()

        self.client.login(username='bahrom', password='somepass')

        response = self.client.post(
            reverse("users:profile_edit"),
            data={
                "username":"bahrom",
                "first_name":"bahrom",
                "last_name":"kjybjnn",
                "email":"bahro23m@gmail.com"
            }
        )
        user = User.objects.get(pk=user.pk)
        self.assertEqual(user.last_name, "kjybjnn")
        self.assertEqual(user.email, "bahro23m@gmail.com")
        self.assertEqual(response.url, reverse("users:profile"))

