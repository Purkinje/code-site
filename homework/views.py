import os
import subprocess, chardet
from django.template import RequestContext
from django.shortcuts import render_to_response

HW_PATH = '/hw/'
EXTENSIONS = ['.c', '.cpp', '.java', '.txt', '.images']



def weeks(request):
    filedir = os.listdir(HW_PATH)
    weeks = []
    
    for fd in filedir:
        if os.path.isdir(HW_PATH + fd):
            weeks.append(fd)
            
    return render_to_response('homework/weeks.html', { 'weeks': weeks }, context_instance=RequestContext(request))

def week(request, week):
    filedir = os.listdir(HW_PATH + week)
    assignments = []
    
    for fd in filedir:
        file, ext = os.path.splitext(fd)
        if ext in EXTENSIONS and os.path.isfile(os.path.join(HW_PATH, week, fd)) and file not in assignments:
            assignments.append(file)
    
    return render_to_response('homework/week.html', { 'assignments': assignments, 'week': week }, context_instance=RequestContext(request))

def hw(request, week, hw):
    file_c = os.path.join(HW_PATH, week, hw + '.c') # source file
    file_txt = os.path.join(HW_PATH, week, hw + '.txt') # Question/Answer
    file_images = os.path.join(HW_PATH, week, hw + '.images') # Images
    file_sh = os.path.join(HW_PATH, week, hw) # linux executable
    file_exe = os.path.join(HW_PATH, week, hw + '.exe') # win exectable
    output = None
    source = None
    text = None
    images = None
    
    if os.path.isfile(file_c):
        source = open(file_c).read()
    if os.path.isfile(file_txt):
        text = open(file_txt).read()
    if os.path.isfile(file_images):
        images = open(file_images).read()
    
    if os.path.isfile(file_sh):
        output = subprocess.Popen(file_sh, stdout=subprocess.PIPE).communicate()[0]
    elif os.path.isfile(file_exe):
        output = subprocess.Popen(file_exe, stdout=subprocess.PIPE).communicate()[0]

    if output is not None:
        encoding = chardet.detect(output)['encoding']
        output = output.decode(encoding).encode('utf-8')
    
    assignment = {
        'title': hw,
        'code': source,
        'output': output,
        'text': text,
        'images': images,
        'week': week,
    }
    
    return render_to_response('homework/assignment.html', assignment, context_instance=RequestContext(request))


