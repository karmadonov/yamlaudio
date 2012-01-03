import sys
from jinja2 import Template

from tools import cuetool

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        data = cuetool.loads(file.read())
    with open('templates/album.yaml') as yaml:
        template = Template(yaml.read())
    print(template.render(data=data))
