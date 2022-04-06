from PyQt5 import QtGui


def get_dark_theme():
    white = QtGui.QColor(255, 255, 255)
    red = QtGui.QColor(255, 0, 0)
    grey = QtGui.QColor(40, 40, 40)
    black = QtGui.QColor(0, 0, 0)
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, grey)
    palette.setColor(QtGui.QPalette.WindowText, white)
    palette.setColor(QtGui.QPalette.Base, grey)
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ToolTipBase, white)
    palette.setColor(QtGui.QPalette.ToolTipText, white)
    palette.setColor(QtGui.QPalette.Text, white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ButtonText, black)
    palette.setColor(QtGui.QPalette.BrightText, red)
    palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
    palette.setColor(QtGui.QPalette.HighlightedText, black)
    return palette


def get_light_theme():
    white = QtGui.QColor(255, 255, 255)
    red = QtGui.QColor(255, 0, 0)
    black = QtGui.QColor(0, 0, 0)
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, white)
    palette.setColor(QtGui.QPalette.WindowText, black)
    palette.setColor(QtGui.QPalette.Base, white)
    palette.setColor(QtGui.QPalette.AlternateBase,QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ToolTipBase, white)
    palette.setColor(QtGui.QPalette.ToolTipText, white)
    palette.setColor(QtGui.QPalette.Text, black)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ButtonText, black)
    palette.setColor(QtGui.QPalette.BrightText, red)
    palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
    palette.setColor(QtGui.QPalette.HighlightedText, black)
    return palette
