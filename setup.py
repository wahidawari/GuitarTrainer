"""
Compilation worked with:

MacOs Catalina 15.5
Python 3.8.3
setuptools=44.1.0
py2app=0.21
pillow=6.2.2

zsh: python3.8 setup.py py2app
"""

from setuptools import setup
from tuner_settings.global_settings import APP_NAME

APP = ['main.py']

SOUND_FILES = ["assets/sounds/drop.wav"]

IMAGE_FILES = ["assets/images/arrowDown_hovered.png",
               "assets/images/arrowDown.png",
               "assets/images/arrowUp_hovered.png",
               "assets/images/arrowUp.png",
               "assets/images/bell_hovered.png",
               "assets/images/bell.png",
               "assets/images/mutedBell_hovered.png",
               "assets/images/mutedBell.png"]

OPTIONS = {'argv_emulation': False,
           'iconfile': 'assets/images/GuitarTunerDesign.icns',
           'plist': {
               'CFBundleName': APP_NAME,
               'CFBundleDisplayName': APP_NAME,
               'CFBundleExecutable': APP_NAME,
               'CFBundleGetInfoString': "Tune your guitar the most simplest way.",
               'CFBundleIdentifier': "com.TomSchimansky.GuitarTuner",
               'CFBundleVersion': "2.0.0",
               'CFBundleShortVersionString': "2.0.0",
               'NSHumanReadableCopyright': u"Copyright © 2020, Tom Schimansky, All Rights Reserved"
           }}

setup(
    name=APP_NAME,
    app=APP,
    author='Tom Schimansky',
    data_files=[("assets/images", IMAGE_FILES),
                ("assets/sounds", SOUND_FILES)],
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
