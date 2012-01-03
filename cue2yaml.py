import sys
from jinja2 import Template

from tools import cuetool


def main():
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        data = cuetool.loads(file.read())
    with open('templates/album.yaml') as yaml:
        template = Template(yaml.read())
    print(template.render(data=data))


if __name__ == '__main__':
    main()
