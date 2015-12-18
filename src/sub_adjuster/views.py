from django.shortcuts import render
from .forms import InitializeSubtitlesBaseForm, InitializeParametersBlueprintForm, InitializeParametersForm, \
    BaseSubUploadForm, BlueprintSubUploadForm, SubUploadForm
from .models import Subtitles, Parameters, Adjuster
from django.http import HttpResponseRedirect
from django.core.files import File
from django.core.files.base import ContentFile


# Create your views here.
def upload_file_view(request):
    context = {
        # 'base_sub_upload_form': BaseSubUploadForm(),
        # 'blueprint_sub_upload_form': BlueprintSubUploadForm(),
        'base_sub_upload_form': SubUploadForm(prefix='base'),
        'blueprint_sub_upload_form': SubUploadForm(prefix='blueprint'),
        # 'base_sub_upload_form': form1,
        # 'blueprint_sub_upload_form': form2,

    }

    if request.method == 'POST':
        request.session['post'] = request.files.items()
        # form1 = BaseSubUploadForm(request.POST, request.FILES)
        # form2 = BlueprintSubUploadForm(request.POST, request.FILES)

        form1 = SubUploadForm(request.POST, request.FILES, prefix='base')
        form2 = SubUploadForm(request.POST, request.FILES, prefix='blueprint')

        # form1 = BaseSubUploadForm(request.POST, request.FILES, prefix='base')
        # form2 = BlueprintSubUploadForm(request.POST, request.FILES, prefix='blueprint')

        form1_valid = form1.is_valid()
        form2_valid = form2.is_valid()


        # if form1_valid and form2_valid:
        if form2_valid:
        # if form1.is_valid() and form2.is_valid():
        #     form1.save()
        #     baseSub = Subtitles.objects.latest('id')
        #     base_sub_id = baseSub.id
        #     request.session['base_sub_id'] = base_sub_id

            form2.save()
            blueprintSub = Subtitles.objects.latest('id')
            blueprint_sub_id = blueprintSub.id
            request.session['blueprint_sub_id'] = blueprint_sub_id

            # a = form1.save()
            # baseSub = Subtitles.objects.latest('id')
            # base_sub_id = baseSub.id
            # request.session['base_sub_id'] = base_sub_id
            # b = form2.save(commit=False)
            #
            # b.foreignkeytoA = a
            # b.save()
            # blueprintSub = Subtitles.objects.latest('id')
            # blueprint_sub_id = blueprintSub.id
            # request.session['blueprint_sub_id'] = blueprint_sub_id


            return HttpResponseRedirect('/get_parameters/')

        # else:
        #     form1 = BaseSubUploadForm(prefix='base')
        #     form2 = BlueprintSubUploadForm(prefix='blueprint')

    return render(request, 'sub_adjuster/upload.html', context)

def download_file_view(request):
    # context = {
    #
    # }
    pass

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

def adjust_file_view(request):
    context = {

    }

    base_sub_id, blueprint_sub_id = request.session.get('base_sub_id', None), request.session.get(
        'blueprint_sub_id', None)

    baseSub, blueprintSub = Subtitles.objects.get(id=base_sub_id), Subtitles.objects.get(id=blueprint_sub_id)
    adjusterObj = Adjuster(baseSub, blueprintSub)

    if adjusterObj.initial_deley == 0:
        adjusterObj.get_initial_deley()
    if adjusterObj.multiplier == 1:
        adjusterObj.get_multiplyer()

    adjusted_filename = get_adjusted_filename(baseSub.sub_file.name)
    adjusted_file_content = ContentFile(adjusterObj.adjust_content())

    adjustedSub = Subtitles()
    adjustedSub.sub_file.save(adjusted_filename, adjusted_file_content, save=True)

    adjustedSub = Subtitles.objects.latest('id')
    adjusted_sub_id = adjustedSub.id
    request.session['adjusted_sub_id'] = adjusted_sub_id

    return render(request, 'sub_adjuster/download.html', context)

def get_adjusted_filename(filename):
    return str(filename[2:-4] + "ADJUSTED" + ".srt")

def get_parameters_view(request):

    base_sub_id = request.session.get('base_sub_id', None)
    baseSub = Subtitles.objects.get(id=base_sub_id)
    base_file_lines = handle_file_to_display(baseSub.sub_file.path)
    base_file_name = baseSub.sub_file.name

    blueprint_sub_id = request.session.get('blueprint_sub_id', None)
    blueprintSub = Subtitles.objects.get(id=blueprint_sub_id)
    blueprint_file_lines = handle_file_to_display(blueprintSub.sub_file.path)
    blueprint_file_name = blueprintSub.sub_file.name

    context = {
        "base_file_lines": enumerate(base_file_lines),
        "blueprint_file_lines": enumerate(blueprint_file_lines),
        "sub_base_form": InitializeSubtitlesBaseForm,
        "sub_blueprint_form": InitializeParametersBlueprintForm,
        "par_form": InitializeParametersForm,
        "base_file_name": str(base_sub_id),
        "blueprint_file_name": str(blueprint_sub_id),
        # "post_data": request.session['post'],
    }

    return render(request, 'sub_adjuster/get_parameters.html', context)
