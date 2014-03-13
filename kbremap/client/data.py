from PySide.QtGui import QColor
from PySide.QtCore import  QObject
from collections import namedtuple
from kbremap import cst


SHORTCUT_MODE, REMAPPING_MODE = range(2) 

GR_TEXT, GR_ICON = range(2)



t = namedtuple('t', 'title icon')

tr = QObject().tr

DATA_TYPE = {
            cst.TEXT: t(tr("Text"), 'text'),
            cst.KEY: t(tr("Key"), 'keys'),
            cst.COMMAND: t(tr("Command"), 'utilities-terminal'),
            cst.SHORTCUT: t(tr("Shortcut"), 'shortcuts'),
            cst.LOAD: t(tr("Load"), 'document-open'),
            cst.PAUSE: t(tr("Pause/Resume"), 'media-playback-pause'),
            cst.STOP: t(tr("Stop"), 'media-playback-stop'),
            cst.RUN_EDITOR: t(tr("Launch the editor"), 'speedy-keyboard'),
            }

KEYBOARD_COLOR = {
    'border': QColor(50, 50, 50),
    'default': QColor(240, 240, 230),
    'content': QColor(205, 235, 205),
    'special-key': QColor(210, 215, 200),
    'no-char': QColor(220, 215, 200),
    'not-used': QColor(200, 200, 200),
    'modifier-on': QColor(180, 200, 240),
    'modifier-off': QColor(220, 235, 240),
    'bg': QColor(100, 110, 110),
    'unused': QColor(192, 192, 192),
}



