from django.test import TestCase
from .models import Adjuster, Subtitles, code, decode



class codingTestCase(TestCase):
    # def codeTest(self):
    #     self.assertEqual()

    def test_decode(self):
        self.assertEqual((40271.111,40271.111), decode("11:11:11,111 --> 11:11:11,111"))
    def test_code(self):
        self.assertEqual(code(40271.111,40271.111), "11:11:11,111 --> 11:11:11,111")
class AdjusterTestCase(TestCase):
    def setUp(self):

        # Subtitles.objects.create(name="",line_A="", line_B="", line_C="")
        Subtitles.objects.create(name="base",line_A="00:00:20,000 --> 00:00:25,000", line_B="00:02:00,000 --> 00:02:15,000", line_C="01:00:43,000 --> 02:00:00,000")
        Subtitles.objects.create(name="blueprint",line_A="00:00:44,000 --> 00:00:50,500", line_B="00:02:54,000 --> 00:03:13,500", line_C="01:19:13,900 --> 02:36:18,000")

    def test_get_multiplier(self):

        sub_base = Subtitles.objects.get(name='base')
        sub_blue = Subtitles.objects.get(name='blueprint')
        adj1 = Adjuster(sub_base, sub_blue)
        adj1.get_multiplier()
        self.assertAlmostEqual(adj1.multiplier, 1.3)




