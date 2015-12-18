from django.db import models
import os
import datetime


# Create your models here.

# for format hh:mm:ss,ms --> hh:mm:ss,ms'
def decode(line):
    time_start, time_end = line.split(' --> ')

    hours_start, minutes_start, secsplus_start = time_start.split(':')
    seconds_start, miliseconds_start = secsplus_start.split(',')

    hours_end, minutes_end, secsplus_end = time_end.split(':')
    seconds_end, milliseconds_end = secsplus_end.split(',')

    total_start = 3600 * float(hours_start) + 60 * float(minutes_start) + \
                  float(seconds_start) + (1 / 1000) * float(miliseconds_start)

    total_end = 3600 * float(hours_end) + 60 * float(minutes_end) + \
                float(seconds_end) + (1 / 1000) * float(milliseconds_end)

    return total_start, total_end


def code(total_start, total_end):
    hours_start = total_start // 3600
    total_start -= 3600 * hours_start

    minutes_start = total_start // 60
    total_start -= 60 * minutes_start

    seconds_start = total_start // 1
    total_start -= seconds_start

    miliseconds_start = total_start * 1000

    hours_end = total_end // 3600
    total_end -= 3600 * hours_end

    minutes_end = total_end // 60
    total_end -= 60 * minutes_end

    seconds_end = total_end // 1
    total_end -= seconds_end

    miliseconds_end = total_end * 1000

    line = '{:0>2}:{:0>2}:{:0>2},{:0>3} --> {:0>2}:{:0>2}:{:0>2},{:0>3}\\n'.format(int(hours_start), int(minutes_start),
                                                                                   int(seconds_start),
                                                                                   int(miliseconds_start),
                                                                                   int(hours_end), int(minutes_end),
                                                                                   int(seconds_end),
                                                                                   int(miliseconds_end))
    return line


class Subtitles(models.Model):
    sub_file = models.FileField()
    line_A = models.CharField(max_length=255, blank=True, default='1')
    line_B = models.CharField(max_length=255, blank=True, default='1')
    line_C = models.CharField(max_length=255, blank=True, default='1')

    # def filename(self):
    #     return os.path.basename(self.sub_file)


class Parameters(models.Model):
    initial_deley = models.FloatField(default=0)
    multiplier = models.FloatField(default=1.0)


class Adjuster(object):
    def __init__(self, subtitle_base, subtitle_blueprint,
                 initial_deley=0, multiplier=1):

        self.subtitle_base = subtitle_base
        self.subtitle_blueprint = subtitle_blueprint

        self.initial_deley = initial_deley
        self.multiplier = multiplier

    def get_initial_deley(self):

        self.initial_deley = decode(self.subtitle_base.line_A)[0] - decode(self.subtitle_blueprint.line_A)[0]

    def get_multiplyer(self):
        n = 0
        if self.subtitle_blueprint.line_B is not None and self.subtitle_base.line_B is not None:
            b = (decode(self.subtitle_blueprint.line_B)[0] - decode(self.subtitle_blueprint.line_A)[0]) / \
                (decode(self.subtitle_base.line_B)[0] - decode(self.subtitle_base.line_A)[0] - self.initial_deley)
            n += 1
        else:
            b = 0
        if self.subtitle_blueprint.line_C is not None and self.subtitle_base.line_C is not None:
            c = b = decode(self.subtitle_blueprint.line_C)[0] / (
            decode(self.subtitle_base.line_C)[0] - self.initial_deley)
            n += 1
        else:
            c = 0

        if n == 0:
            self.multiplier = 1
        else:
            self.multiplier = n / (b + c)

    def adjust_content(self):
        adjusted_content = []
        with open(self.subtitle_base.sub_file.path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if ' --> ' in line:
                    line = code(self.initial_deley + decode(line)[0] * self.multiplier,
                                self.initial_deley + decode(line)[1] * self.multiplier)
                adjusted_content.append(line)
        return adjusted_content
