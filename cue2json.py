import sys
import json

from tools import cuetool

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        data = cuetool.loads(file.read())
    print(json.dumps(data))
