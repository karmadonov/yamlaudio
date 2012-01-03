from setuptools import setup, find_packages

version = '0.0.1'
long_description = '\n\n'.join([open('README.rst').read(), ])

setup(name='yamlaudio',
      version=version,
      description="YAML tags for audio files",
      long_description=long_description,
      classifiers=[],
      keywords='yamlaudio',
      author='0xKirill',
      author_email='0xkirill@gmail.com',
      url='https://github.com/0xKirill/yamlaudio',
      license='MIT',
      py_modules=['cue2json', 'cue2yaml', 'yaml2cue', 'yaml2json',
                  'tools.cuetool'],
      namespace_packages=[],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'pyyaml',
          'jinja2',
          # -*- Extra requirements: -*-
      ],
      entry_points={
          'console_scripts': [
              'cue2json = cue2json:main',
              'cue2yaml = cue2yaml:main',
              'yaml2cue = yaml2cue:main',
              'yaml2json = yaml2json:main',
              ],
          },
      )
