

YAML tags for audio files
=========================

A set of scripts to work with YAML tags for audio files. This project offers an alternative to use the outdated `cue sheet <http://en.wikipedia.org/wiki/Cue_sheet_(computing)>`_ format.

YAML tags example
-----------------

::

    title:              Nightbook
    artist:             Ludovico Einaudi
    tags:               [classical, neoclassical, contemporary classical]
    release_date:       2009-09-20
    label:              Sony Classical
    country:            United Kingdom
    barcode:            028947636397
    cover:              cover.jpg
    
    files:
      - file:           Nightbook.flac
        tracks:
            - track:    1
              title:    In Principio
              ISRC:     ITB280900001
              index:    00:00:00
    
            - track:    2
              title:    Lady Labyrinth
              ISRC:     ITB280900002
              index:    02:51:43
    
            - track:    3
              title:    Nightbook
              ISRC:     ITB280900003
              index:    08:21:60
            ...

`Full example <https://gist.github.com/1554384>`_


YAML tags specification
-----------------------
YAML tags format does not require some "required tags", but have some recommended.

Recommended tags
****************

+------------+---------------+------------------------------------------------+ 
| Tag        | Format        | Description                                    | 
+============+===============+================================================+ 
| file       | file path     | A path to a file containing audio data, and to |
|            |               | which subsequent commands apply, equivalent to |
|            |               | FILE in cue sheets e.g., the_best_of.flac      | 
+------------+---------------+------------------------------------------------+ 
| track      | integer       | A number between 01 and 99, indicating         |
|            |               | the track number., equivalent to TRACK         |
|            |               | in cue sheets e.g., 12                         |
+------------+---------------+------------------------------------------------+ 
| index      | time [*]_     | The start point (index 01) for each track,     |
|            |               | time-wise (MM:SS:FF format)., equivalent to    |
|            |               | INDEX 01 in cue sheets e.g., 02:34:50          |
+------------+---------------+------------------------------------------------+ 

.. [*] mm:ss:ff – time in minutes, seconds, and frames (75 frames/second).

Popular tags
************

+------------+---------------+------------------------------------------------+ 
| Tag        | Format        | Description                                    | 
+============+===============+================================================+ 
| catalog    | integer       | A 13-digit UPC/EAN code, equivalent to         |
|            |               | CATALOG in cue sheets e.g., 4898347789130      | 
+------------+---------------+------------------------------------------------+ 
| cdtextfile | file path     | A path to a file containing CD-Text info,      |
|            |               | equivalent to CDTEXTFILE in cue sheets         |
|            |               | e.g., DISC.CDT                                 |
+------------+---------------+------------------------------------------------+ 
| flags      | string        | Per-track subcode flag(s), equivalent to FLAGS |
|            |               | in cue sheets e.g., DCP2, 4CH, PRE, SCMS       |
+------------+---------------+------------------------------------------------+ 
| ISRC       | string        | Per-track International Standard Recording Code|
|            |               | equivalent to ISRC in cue sheets e.g.,         |
|            |               | ABCDE1234567                                   |
+------------+---------------+------------------------------------------------+
| artist     | string        | Per-disc or per-track performer name for       |
|            |               | CD-Text data, equivalent to PERFORMER in       |
|            |               | cue sheets e.g., Fabrizio Paterlini            |
+------------+---------------+------------------------------------------------+
| gap        | time          | Commands specify the pre-gap of a track,       |
|            |               | equivalent to INDEX 00 in cue sheets e.g.,     |
|            |               | 02:34:50                                       |
+------------+---------------+------------------------------------------------+
| pregap     | time          | Used to specify the length of a track pre-gap, |
|            |               | in MM:SS:FF format, equivalent to PREGAP       |
|            |               | in cue sheets e.g., 02:34:50                   |
+------------+---------------+------------------------------------------------+
| postgap    | time          | Used to specify the length of a track post-gap,|
|            |               | in MM:SS:FF format, equivalent to POSTGAP      |
|            |               | in cue sheets e.g., 02:34:50                   |
+------------+---------------+------------------------------------------------+
| author     | string        | Per-disc or per-track songwriter name for      |
|            |               | CD-Text data, equivalent to SONGWRITER         |
|            |               | in cue sheets e.g., Chris Martin               |
+------------+---------------+------------------------------------------------+
| title      | string        | Title of disc or track, equivalent to TITLE    |
|            |               | in cue sheets e.g., We Played Some Open        |
+------------+---------------+------------------------------------------------+

Useful Tags
***********
+------------+---------------+------------------------------------------------+ 
| Tag        | Format        | Description                                    | 
+============+===============+================================================+ 
| tags       | list          | Useful genre tags, e.g.,                       |
|            |               | [classical, neoclassical, piano]               |
|            |               | (firs tag converted to the REM GENRE in cue)   |
+------------+---------------+------------------------------------------------+ 
|release_date| date or year  | Release date of the disc, e.g.,                |
|            |               | 2009-09-20 or 2009                             |
|            |               | (converted to the year in REM DATE in the cue) |
+------------+---------------+------------------------------------------------+
| discid     | string        | Disc ID, e.g., 34103B15                        |
|            |               | (converted to the REM DISCID in the cue)       |
+------------+---------------+------------------------------------------------+ 
| cover      | file path     | A path to a file containing cover image e.g.,  |
|            |               | the_best_of.jpg                                | 
+------------+---------------+------------------------------------------------+ 

...and many other tags, be free!

YAML tags tools
---------------

- **cue2json** - convert cue sheet file to JSON.
- **cue2yaml** - convert cue sheet file to YAML.
- **yaml2cue** - convert YAML file to cue sheet.
- **yaml2json** - convert YAML file to JSON.

Some examples::

    cue2json old_file.json > new_file.yaml
    yaml2json yaml_file.yaml > dump.json

Requirements:
    - Python 3 - http://python.org/
    - pyyaml - http://pyyaml.org/
    - jinja2 - http://jinja.pocoo.org/
    
Installation
************

::

        git clone git@github.com:0xKirill/yamlaudio.git
        cd yamlaudio
        python3 setup.py install

Useful links
------------
- http://digitalx.org/cue-sheet/ - information on the cue sheet pages was taken from the helpfile of CDRWIN.
- http://wiki.hydrogenaudio.org/index.php?title=Cue_sheet - information on the cue sheet from Hydrogenaudio.
- http://www.yaml.org/ - The Official YAML Web Site.
