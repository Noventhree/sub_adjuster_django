from django.test import TestCase
from .models import Adjuster, Subtitles, code, decode

# Create your tests here.

class codingTestCase(TestCase):
    # def codeTest(self):
    #     self.assertEqual()

    def test_decode(self):
        self.assertEqual((40271.111,40271.111), decode("11:11:11,111 --> 11:11:11,111"))
    def test_code(self):
        # self.assertEqual(code(40271.111,40271.111), "11:11:11,111 --> 11:11:11,111\n")
class SubtitlesTestCase(TestCase):
    def setUp(self):

        # Subtitles.objects.create(name="",line_A="", line_B="", line_C="")
        Subtitles.objects.create(name="base",line_A="", line_B="", line_C="")
        Subtitles.objects.create(name="blueprint",line_A="", line_B="", line_C="")
