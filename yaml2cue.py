"""
Copyright (c) 2012 0xKirill <0xkirill@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""


import sys
import datetime
import yaml
from jinja2 import Template


def dict2cue(yamldict):
    cuedict = dict()
    if 'catalog' in yamldict:
        cuedict['catalog'] = yamldict['catalog']
    if 'tags' in yamldict:
        cuedict['genre'] = yamldict['tags'][0].title()
    if 'date' in  yamldict:
        if isinstance(yamldict['date'], int):
            cuedict['date'] = yamldict['date']
        elif isinstance(yamldict['date'], datetime.datetime):
            cuedict['date'] = yamldict['date'].year
    if 'discid' in yamldict:
        cuedict['discid'] = yamldict['date']
    if 'artist' in yamldict:
        cuedict['performer'] = yamldict['artist']
    if 'title' in yamldict:
        cuedict['title'] = yamldict['title']
    cuedict['files'] = []
    for file in yamldict['files']:
        cuefile = dict()
        cuefile['file'] = file['file']
        if file['file'][-3:].lower() == 'mp3':
            cuefile['type'] = 'MP3'
        else:
            cuefile['type'] = 'WAVE'
        cuefile['tracks'] = file['tracks']
        cuedict['files'].append(cuefile)
    with open('templates/album.cue') as cue:
        template = Template(cue.read())
    return template.render(data=cuedict)


if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        yamldict = yaml.load(file.read())
        print(dict2cue(yamldict))
