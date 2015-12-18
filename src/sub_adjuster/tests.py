from django.test import TestCase
import pytest
from .models import Adjuster, Subtitles, code, decode

# Create your tests here.


def test_decode():
    assert decode('00:00:11,111 --> 00:00:00,000') == (11.111, 0)
    assert decode('02:10:00,000 --> 01:01:01,001') == (7800, 3661.001)

def test_code():
    assert code(11.111, 0) == '00:00:11,111 --> 00:00:00,000\\n'
    assert code(7800, 3661.001) == '02:10:00,000 --> 01:01:01,001\\n'

subtitle_base = Subtitles(None, '00:00:11,111 --> 00:00:11,112')
subtitle_blueprint = Subtitles(None, '00:00:22,222 --> 00:00:22,223')


def test_get_initial_deley():
    subtitle_base = Subtitles(None, '00:00:11,111 --> 00:00:11,112')
    subtitle_blueprint = Subtitles(None, '00:00:22,222 --> 00:00:22,223')
    obj = Adjuster(subtitle_base, subtitle_blueprint)
    obj.get_initial_deley()
    assert obj.initial_deley == -11.111


def test_get_multiplier():
    subtitle_base = Subtitles(None, '00:00:11,111 --> 00:00:11,112','04:20:00,000 --> 01:01:01,000')
    subtitle_blueprint = Subtitles(None, '00:00:11,111 --> 00:00:11,112','02:10:00,000 --> 01:01:01,000')
    obj = Adjuster(subtitle_base, subtitle_blueprint, None)
    obj.get_initial_deley()
    obj.get_multiplyer()
    assert obj.multiplier == 2

