{% if data.catalog %}CATALOG {{ data.catalog }}
{% endif %}{% if data.genre %}REM GENRE {{ data.genre }}
{% endif %}{% if data.date %}REM DATE {{ data.date }}
{% endif %}{% if data.discid %}REM DISCID {{ data.discid }}
{% endif %}REM COMMENT "Generated from YAML"
{% if data.performer %}PERFORMER "{{ data.performer }}"
{% endif %}{% if data.title %}TITLE "{{ data.title }}"
{% endif %}{% for file in data.files %}FILE "{{ file.file }}" {{ file.type }}{% for track in file.tracks %}
  TRACK {{ track.track }} AUDIO{% if track.isrc %}
    ISRC {{ track.isrc }}{% endif %}{% if track.pregap %}
    PREGAP {{ track.pregap }}{% endif %}{% if track.title %}
    TITLE "{{ track.title }}"{% endif %}{% if track.performer %}
    PERFORMER "{{ track.performer }}"{% endif %}{% if track.gap %}
    INDEX 00 {{ track.gap }}{% endif %}{% if track.index %}
    INDEX 01 {{ track.index }}{% endif %}{% if track.postgap %}
  POSTGAP {{ track.postgap }}{% endif %}{% endfor %}{% endfor %}
