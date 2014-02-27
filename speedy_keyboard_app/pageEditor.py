
from PySide.QtGui import *
from PySide.QtCore import Qt
from widgets import ShortcutWidget
import os

class PageBase(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self._data = None
        self.layout = QHBoxLayout(self)
        
    def data(self):
        return None
    
    def isValid(self):
        return False
    
    def setData(self, data):
        pass
    
    def start(self):
        pass
    
#     def finish(self):
#         pass
    
    def errorMessage(self):
        return ''
    
class PageEmpty(PageBase):
    def __init__(self):
        PageBase.__init__(self)


class PageText(PageBase):
    def __init__(self):
        PageBase.__init__(self)
        self.lineEdit = QLineEdit(self)
        self.checkClipboard = QCheckBox(self.tr("Use clipboard"))
        
        self.layout.addWidget(QLabel(self.tr("Text:")))
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.checkClipboard)
    
    def start(self):
        self.lineEdit.setFocus(Qt.OtherFocusReason)
    
    def data(self):
        return (self.lineEdit.text(), self.checkClipboard.isChecked())
    
    def setData(self, data):
        text, clipboard = data
        self.lineEdit.setText(text)
        self.checkClipboard.setChecked(clipboard)
    
    def isValid(self):
        return bool(self.lineEdit.text())
    
    def errorMessage(self):
        return self.tr("You must enter a text to send.")
    
    
class PageLauncher(PageBase):
    def __init__(self, iconChooser):
        PageBase.__init__(self)
        self.iconChooser = iconChooser
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setAcceptDrops(False)
        self.layout.addWidget(QLabel(self.tr("Command:")))
        self.layout.addWidget(self.lineEdit)
        self.setAcceptDrops(True)
    
    def dragEnterEvent(self, e):
      
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
             
        else:
            e.ignore() 

    def start(self):
        self.lineEdit.setFocus(Qt.OtherFocusReason)

    def dropEvent(self, e):
        mime = e.mimeData()
        text = str(mime.data('text/plain')).strip()
        path = text[7:]
        if os.path.exists(path) and os.path.splitext(path)[1] == '.desktop':
            with open(path) as f:
                command = ''
                icon = ''
                for line in f:
                    if line.startswith('Exec='):
                        command = line.split('=')[1]
                    if line.startswith('Icon='):
                        icon = line.split('=')[1]
                
                self.lineEdit.setText(command.strip())
                self.iconChooser.setIcon(icon.strip())
        else:
            self.lineEdit.setText(text)
        
    def data(self):
        return self.lineEdit.text()
    
    def setData(self, data):
        self.lineEdit.setText(data)
    
    def isValid(self):
        return bool(self.lineEdit.text())
    
    def errorMessage(self):
        return self.tr("You must enter a command.")   
    
        
class PageShortcut(PageBase):
    def __init__(self):
        PageBase.__init__(self)
        self.shortcutWidget = ShortcutWidget()
        self.layout.addWidget(self.shortcutWidget)
    
    def start(self):
        self.shortcutWidget.setFocus(Qt.OtherFocusReason)
        
    def data(self):
        return self.shortcutWidget.data()
    
    def setData(self, data):
        self.shortcutWidget.setData(*data)
        
    def isValid(self):
        return bool(self.shortcutWidget.text())
    
    def errorMessage(self):
        return self.tr("You must enter a shortcut.")   

        
        
        