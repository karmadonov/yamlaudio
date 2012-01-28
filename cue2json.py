import sys
import json

from tools import cuetool


def main():
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        data = cuetool.loads(file.read().decode('utf-8'))
    print(json.dumps(data))


if __name__ == '__main__':
    main()
