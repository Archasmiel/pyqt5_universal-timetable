from PyQt5 import QtWidgets, uic, QtGui

from ui import themes, tablework

UIfile = 'ui/app.ui'


def load_colors():
    with open(r'data/colors.txt', 'r') as f:
        data = f.read().split('\n')
    return data[0], data[1], 1 if data[2] == 'dark' else 0


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(UIfile, self)

        self.tables = [self.textBrowser, self.textBrowser_2]
        with open('data/files.txt') as f:
            self.groups = tablework.init(f.read().split('\n'))

        self.themes = (
            (themes.get_light_theme, QtGui.QColor(0, 0, 0)),
            (themes.get_dark_theme, QtGui.QColor(255, 255, 255))
        )
        self.theme = 1

        for i in self.groups:
            self.comboBox.addItem(i.name)

        self.setWindowTitle('Расписание')
        self.setWindowIcon(QtGui.QIcon('ui/icon.png'))
        self.set_theme()
        self.comboBox.activated.connect(self.display_group)
        self.pushButton_2.clicked.connect(self.change_theme)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser_2.setOpenExternalLinks(True)
        self.show()

    def display_group(self):
        group = self.comboBox.currentText()
        for i in self.groups:
            if i.name == group:
                self.show_tables(i)

    def show_tables(self, group):
        self.textBrowser.setText(group.week1)
        self.textBrowser.show()
        self.textBrowser.raise_()
        self.textBrowser_2.setText(group.week2)
        self.textBrowser_2.show()
        self.textBrowser_2.raise_()

    def set_theme(self):
        self.setPalette(self.themes[self.theme][0]())
        self.textBrowser.setPalette(self.themes[self.theme][0]())

        self.textBrowser_2.setPalette(self.themes[self.theme][0]())
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.WindowText, self.themes[self.theme][1])
        self.statusBar.setPalette(palette)
        palette.setColor(QtGui.QPalette.Text, self.themes[0][1])
        self.comboBox.setPalette(palette)
        self.pushButton_2.setText('L' if self.theme == 0 else 'D')

    def change_theme(self):
        # 0 - light, 1 - dark
        self.theme = 1 if self.theme == 0 else 0
        self.set_theme()

