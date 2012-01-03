""" Thanks to http://digitalx.org/ for test examples
"""
import unittest
import json
import os

from tools import cuetool


class TestCueSheets(unittest.TestCase):

    def setUp(self):
        curdir = os.path.dirname(__file__) or '.'
        cue_examples = curdir + '/examples'
        examples = os.listdir(cue_examples)
        for file in examples:
            filename = cue_examples + '/' + file
            with open(filename, 'r') as file:
                data = cuetool.loads(file.read())

    def test_minimal_cue(self):
        with open('examples/minimal.cue', 'r') as file:
            data = cuetool.loads(file.read())
        self.assertEqual(data,
            {'files': [
                {'tracks': [
                    {'track': '01',
                     'index': '00:00:00',
                     'performer': 'The Specials',
                     'title': 'Gangsters'}],
                'file': 'The Specials - Singles.wav'}]})

    def test_nopause_cue(self):
        with open('examples/nopause.cue', 'r') as file:
            data = cuetool.loads(file.read())
        self.assertEqual(data,
            {'files': [
                {'tracks': [{'track': '01', 'index': '00:00:00'},
                            {'track': '02', 'index': '05:50:65'},
                            {'track': '03', 'index': '09:47:50'},
                            {'track': '04', 'index': '15:12:53'}],
                 'file': 'C:\\TRACK1.WAV'},
                {'tracks': [{'track': '05', 'index': '00:00:00'},
                            {'track': '06', 'index': '02:31:40'},
                            {'track': '07', 'index': '06:56:13'},
                            {'track': '08', 'index': '10:06:25'}],
                'file': 'C:\\TRACK2.WAV'}]})

    def test_pertrack_cue(self):
        with open('examples/pertrack.cue', 'r') as file:
            data = cuetool.loads(file.read())
        self.assertEqual(data,
            {'files': [
                {'tracks': [{'track': '01', 'index': '00:00:00'}],
                    'file': 'C:\\TRACK1.WAV'},
                {'tracks': [{'track': '02', 'index': '00:00:00'}],
                    'file': 'C:\\TRACK2.WAV'},
                {'tracks': [{'track': '03', 'index': '00:00:00'}],
                    'file': 'C:\\TRACK1.AIF'},
                {'tracks': [{'track': '04', 'index': '00:00:00'}],
                    'file': 'C:\\TRACK2.AIF'},
                {'tracks': [{'track': '05', 'index': '00:00:00'}],
                    'file': 'C:\\TRACK1.MP3'},
                {'tracks': [{'track': '06', 'index': '00:00:00'}],
                    'file': 'C:\\TRACK2.MP3'}]})

    def test_pertrack2_cue(self):
        with open('examples/pertrack2.cue', 'r') as file:
            data = cuetool.loads(file.read())
        self.assertEqual(data,
            {'files': [
                {'tracks': [
                    {'track': '01', 'index': '00:00:00', 'pregap': '00:01:00'}
                    ],
                 'file': 'C:\\MYAUDIO1.WAV'},
                {'tracks': [
                    {'track': '02', 'index': '00:00:00', 'pregap': '00:02:00'}
                    ],
                 'file': 'C:\\MYAUDIO2.WAV'},
                {'tracks': [
                    {'track': '03',
                     'index': '00:01:00',
                     'gap': '00:00:00',
                     'pregap': '00:01:00'}],
                 'file': 'C:\\MYAUDIO3.WAV'}]})

    def test_pregap_cue(self):
        with open('examples/pregap.cue', 'r') as file:
            data = cuetool.loads(file.read())
        self.assertEqual(data,
            {'files': [
                {'tracks': [{'track': '01', 'index': '00:00:00'},
                {'track': '02', 'index': '05:50:65', 'gap': '05:49:65'},
                {'track': '03', 'index': '09:47:50', 'gap': '09:45:50'},
                {'track': '04', 'index': '15:12:53', 'gap': '15:09:53'}],
            'file': 'C:\\MYAUDIO1.WAV'}]})

    def test_singlewav_cue(self):
        with open('examples/singlewav.cue', 'r') as file:
            data = cuetool.loads(file.read())
        self.assertEqual(data,
            {'files': [
                {'tracks': [{'track': '01', 'index': '00:00:00'},
                            {'track': '02', 'index': '05:50:65'},
                            {'track': '03', 'index': '09:47:50'},
                            {'track': '04', 'index': '15:12:53'},
                            {'track': '05', 'index': '25:02:40'},
                            {'track': '06', 'index': '27:34:05'},
                            {'track': '07', 'index': '31:58:53'},
                            {'track': '08', 'index': '35:08:65'}],
                 'file': 'C:\\MYAUDIO.WAV'}]})


if __name__ == '__main__':
    unittest.main()
