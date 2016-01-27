from django.shortcuts import render
from .forms import InitializeParametersForm, SubUploadForm, GetLinesForm
from .models import Subtitles, Adjuster
from django.http import HttpResponseRedirect
from django.core.files.base import ContentFile
import os
from django.http import HttpResponse


# -*- coding: utf-8 -*-

def upload_file_view(request):
    context = {
        'base_sub_upload_form': SubUploadForm(prefix='base'),
        'blueprint_sub_upload_form': SubUploadForm(prefix='blueprint'),
    }

    if request.method == 'POST':

        form1 = SubUploadForm(request.POST, request.FILES, prefix='base')
        form2 = SubUploadForm(request.POST, request.FILES, prefix='blueprint')

        form1_valid = form1.is_valid()
        form2_valid = form2.is_valid()

        if form1_valid and form2_valid:
            form1.save()
            base_sub = Subtitles.objects.latest('id')
            base_sub_id = base_sub.id
            request.session['base_sub_id'] = base_sub_id

            form2.save()
            blueprint_sub = Subtitles.objects.latest('id')
            blueprint_sub_id = blueprint_sub.id
            request.session['blueprint_sub_id'] = blueprint_sub_id

            return HttpResponseRedirect('/get_parameters/')

    return render(request, 'sub_adjuster/upload.html', context)


def handle_file_to_display(path):
    file_lines = []
    with open(path) as f:
        counter = 0
        lines = f.readlines()
        lines[0] = '1\n'

        content = {
            'num': '',
            'timer': '',
            'text': '',
        }

        for line in lines:
            counter += 1

            if line == '\n':
                file_lines.append("""{num}{timer}{text}""".format(**content))
                counter = 0
                content['text'] = ''
            elif counter == 1:
                content['num'] = line
            elif counter == 2:
                content['timer'] = line
            elif counter > 2 and content['text'] == '':
                content['text'] = line
            elif counter > 2 and content['text'] != '':
                content['text'] += line
        return file_lines


def get_adjusted_filename(filename):
    return str(filename[2:-4] + "ADJUSTED" + ".srt")


def get_parameters_view(request):
    base_sub_id = request.session.get('base_sub_id', None)
    base_sub = Subtitles.objects.get(id=base_sub_id)
    base_file_lines = handle_file_to_display(base_sub.sub_file.path)

    blueprint_sub_id = request.session.get('blueprint_sub_id', None)
    blueprint_sub = Subtitles.objects.get(id=blueprint_sub_id)
    blueprint_file_lines = handle_file_to_display(blueprint_sub.sub_file.path)

    context = {
        "base_file_lines": enumerate(base_file_lines),
        "blueprint_file_lines": enumerate(blueprint_file_lines),
        "sub_base_form": GetLinesForm(prefix='base'),
        "sub_blueprint_form": GetLinesForm(prefix='blueprint'),
        "par_form": InitializeParametersForm,
        "base_file_name": str(base_sub_id),
        "blueprint_file_name": str(blueprint_sub_id),
    }

    form1 = GetLinesForm(request.POST, prefix='base')
    form2 = GetLinesForm(request.POST, prefix='blueprint')
    if request.method == 'POST':

        form1_valid = form1.is_valid()
        form2_valid = form2.is_valid()

        if form1_valid and form2_valid:
            base_sub, blueprint_sub = Subtitles.objects.get(id=base_sub_id), Subtitles.objects.get(id=blueprint_sub_id)

            base_sub.line_A = request.POST['base-line_A']
            base_sub.line_B = request.POST['base-line_B']
            base_sub.line_C = request.POST['base-line_C']
            base_sub.save()

            blueprint_sub.line_A = request.POST['blueprint-line_A']
            blueprint_sub.line_B = request.POST['blueprint-line_B']
            blueprint_sub.line_C = request.POST['blueprint-line_C']
            blueprint_sub.save()

            base_sub, blueprint_sub = Subtitles.objects.get(id=base_sub_id), Subtitles.objects.get(id=blueprint_sub_id)
            adjuster = Adjuster(base_sub, blueprint_sub)
            if adjuster.initial_deley == 0:
                pass

                # adjuster.get_initial_deley()
            if adjuster.multiplier == 1:
                # pass
                # adjuster.get_multiplyer()

                adjusted_filename = get_adjusted_filename(base_sub.sub_file.name)
                adjusted_file_content = ContentFile("".join(adjuster.adjust_content()))

                adjusted_sub = Subtitles()
                adjusted_sub.sub_file.save(adjusted_filename, adjusted_file_content, save=True)

                adjusted_sub = Subtitles.objects.latest('id')
                adjusted_sub_id = adjusted_sub.id
                request.session['adjusted_sub_id'] = adjusted_sub_id

            return HttpResponseRedirect('/confirm_adjustment/')

    return render(request, 'sub_adjuster/get_parameters.html', context)


def confirm_adjustment_view(request):
    base_sub_id = request.session['base_sub_id']
    adjusted_sub_id = request.session['adjusted_sub_id']
    blueprint_sub_id = request.session['blueprint_sub_id']

    base_sub = Subtitles.objects.get(id=base_sub_id)
    adjusted_sub = Subtitles.objects.get(id=adjusted_sub_id)
    blueprint_sub = Subtitles.objects.get(id=blueprint_sub_id)

    base_file_lines = handle_file_to_display(base_sub.sub_file.path)
    adjusted_file_lines = handle_file_to_display(adjusted_sub.sub_file.path)

    context = {
        "base_file_lines": enumerate(base_file_lines),
        "adjusted_file_lines": enumerate(adjusted_file_lines),
        "base_file_name": str(base_sub_id),
        "adjusted_file_name": str(adjusted_sub_id),

    }
    if request.method == 'POST':
        response = HttpResponse(adjusted_sub.sub_file)
        response['Content-Disposition'] = "attachment; filename={}".format(os.path.basename(adjusted_sub.sub_file.name))
        request.session.flush()
        base_sub.delete()
        adjusted_sub.delete()
        blueprint_sub.delete()

        return response
    return render(request, 'sub_adjuster/confirm_adjustment.html', context)
