import sys
import os
from jinja2 import Template

from tools import cuetool


def main():
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        data = cuetool.loads(file.read().decode('utf-8'))
    with open(os.path.dirname(__file__) + '/templates/album.yaml') as yaml:
        template = Template(yaml.read())
    print(template.render(data=data))


if __name__ == '__main__':
    main()
