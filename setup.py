#!/usr/bin/env python

from distutils.core import setup

NAME='key-mon'
VER='0.14.1'
setup(
    name = NAME,
    version = VER,
    packages = ['keymon'],
    package_dir = {
      'keymon': 'src/keymon'},
    package_data = {
      'keymon': [
          'themes/**/*',
          '*.kbd'],
    },
    scripts=['src/key-mon'],
    author='Scott Kirkwood',
    author_email='scott+keymon@forusers.com',
    platforms=['POSIX'],
    license='LGPL',
    keywords='keyboard status monitor education',
    url='http://code.google.com/p/%s' % NAME,
    download_url='http://%s.googlecode.com/files/%s-%s.zip' % (NAME, NAME, VER),
    classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: X11 Applications',
      'Intended Audience :: Education',
      'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
      'Operating System :: POSIX :: Linux',
      'Topic :: Education :: Computer Aided Instruction (CAI)',
    ], 
    description='A small utility to display your current keyboard and mouse status.  Useful for screencasts.',
    long_description="""Key-mon is useful for teaching since it shows the current status of your 
    keyboard and mouse and you use them in another application.  No longer do you need to say
    'Now I'm pressing the Ctrl-D key', your students can just see the keystroke for themselves.
    """,
)
