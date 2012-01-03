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

Thanks to Hydrogenaudio:
http://wiki.hydrogenaudio.org/index.php?title=EAC_and_Cue_Sheets
"""


def _tracks(cue, file):
    file['tracks'] = []
    track = {}
    while cue and cue[0][0] != 'FILE':
        command = cue.pop(0)
        if command[0] == 'TRACK':
            if track:
                file['tracks'].append(track)
                track = dict()
            if command[-1] in ('AUDIO', 'MODE1/2048', 'MODE1/2352', 'CDI/2352',
                               'MODE2/2336', 'MODE2/2352', 'CDI/2336', 'CDG'):
                command.pop(-1).lower()
            track['track'] = ' '.join(command[1:]).strip('"')
        elif command[0] == 'INDEX':
            # index (or subindex) within a track
            if command[1] == '01':
                track['index'] = command[2]
            if command[1] == '00':
                track['gap'] = command[2]
        else:
            track[command[0].lower()] = ' '.join(command[1:]).strip('"')
    file['tracks'].append(track)
    return file


def loads(cuesheet):
    cue = [line.split() for line in cuesheet.splitlines()]
    cue_dict = dict(files=[])
    while cue:
        command = cue.pop(0)
        if command[0] == 'REM':
            # comments in a cue sheet
            cue_dict[command[1].lower()] = ' '.join(command[2:]).strip('"')
        elif command[0] == 'FILE':
            # it's filename
            if command[-1] in ('WAVE', 'BINARY', 'MOTOROLA', 'AIFF', 'MP3'):
                #  WavPack or FLAC, can be used under the WAVE file type
                command.pop(-1).lower()
            filename = ' '.join(command[1:]).strip('"')
            cue_dict['files'].append(_tracks(cue, dict(file=filename)))
        else:
            # it's only strings
            cue_dict[command[0].lower()] = ' '.join(command[1:]).strip('"')
    return cue_dict
