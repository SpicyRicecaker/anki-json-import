# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def importJson():
    # Open dialog
    mw.col.

# create a new menu item, "test"
action = QAction("Import from JSON", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(importJson)
# and add it to the tools menu
mw.form.menuTools.addAction(action)