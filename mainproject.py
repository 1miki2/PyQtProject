import random
import sqlite3
import sys

from PyQt5.QtCore import Qt, QByteArray, QBuffer, QIODevice
from PyQt5.QtGui import QColor, QPixmap, QPainter, QPen, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow, QColorDialog, QFileDialog, QInputDialog, QMessageBox
from ui import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        super().__init__()
        self.setupUi(self)
        self.color = cur.execute('SELECT color FROM colors').fetchmany(-1)[0][0]
        self.fillColor = cur.execute('SELECT fill_color FROM colors').fetchmany(-1)[0][0]
        self.spray_particles = None
        self.pixmap = None
        self.flag = False
        self.setWindowState(Qt.WindowMaximized)
        self.setMouseTracking(True)
        self.scaled_pixmap = None
        self.n, self.m, self.width = 25, 10, 3
        self.pos1, self.pos2 = [0, 0], [0, 0]

        image = QPixmap(1500, 1000)
        image.fill(Qt.white)
        self.label.resize(1500, 1000)
        self.label.setPixmap(image)
        self.label.move(190, 0)

        self.widthButton.clicked.connect(self.choiceWidth)
        self.colorButton.clicked.connect(self.choiceColor)
        self.colorButton.setStyleSheet("color:white;"
                                       "background-color: {}".format(self.color))
        self.fillCheckBox.clicked.connect(self.choiceFill)
        self.fillColorButton.clicked.connect(self.fillChoice)
        self.fillColorButton.setStyleSheet("background-color: {}".format(self.fillColor))
        self.tools.buttonClicked.connect(self.choiceTool)
        self.stylus.toggle()
        self.tool = 'ручка'
        self.choicePhotos.clicked.connect(self.choicePhoto)
        self.saveButton.clicked.connect(self.save)
        self.clearButton.clicked.connect(self.clear)
        con.commit()
        cur.close()
        con.close()

    def choiceWidth(self):
        n, ok_pressed = QInputDialog.getInt(self, 'Введите толщину', 'Толщина: ', 10, 1, 100, 5)
        if ok_pressed:
            self.n = n
            self.m = n
            self.width = n

    def choiceColor(self):
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        color = QColorDialog.getColor()
        if color.isValid():
            self.colorButton.setStyleSheet(
                "background-color: {}".format(color.name())
            )
        if color.name() == '#000000':
            self.colorButton.setStyleSheet("color: white;"
                                           "background-color: black")
        self.color = color.name()
        cur.execute(f'UPDATE colors\n'
                    'SET color = ?\n'
                    'WHERE id = 1', (self.color,))
        con.commit()
        cur.close()
        con.close()

    def choiceFill(self):
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        color = self.fillColorButton.palette().button().color()
        if self.fillCheckBox.isChecked():
            if color == '#ffffff':
                color = QColorDialog.getColor()
                if color.isValid():
                    self.fillColorButton.setStyleSheet(
                        "background-color: {}".format(color.name())
                    )
                    if color.name() == '#000000':
                        self.fillColorButton.setStyleSheet("color: white;"
                                                           "background-color: black")
            self.fillColor = color.name()
        if type(self.fillColor) is tuple:
            self.fillColor = '#{:02x}{:02x}{:02x}'.format(int(self.fillColor[0]), int(self.fillColor[1]),
                                                          int(self.fillColor[2]))
        cur.execute('UPDATE colors\n'
                    'SET fill_color = ?\n'
                    'WHERE id = 1', (self.fillColor,))
        con.commit()
        cur.close()
        con.close()

    def fillChoice(self):
        if not self.fillCheckBox.isChecked():
            self.fillCheckBox.toggle()
        color = QColorDialog.getColor()
        if color.isValid():
            self.fillColorButton.setStyleSheet(
                "background-color: {}".format(color.name())
            )
            if color.name() == '#000000':
                self.fillColorButton.setStyleSheet("color: white;"
                                                   "background-color: black")
        self.fillColor = color.name()
        self.choiceFill()

    def choiceTool(self, button):
        self.tool = button.text().lower()
        if self.tool == 'спрей':
            sp, ok_pressed = QInputDialog.getInt(self, 'Выберите густоту спрея', 'Густота: ', 100, 1, 700, 100)
            if ok_pressed:
                self.spray_particles = sp

    def choicePhoto(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        if not fname:
            return
        self.pixmap = QPixmap(fname)
        width = 1000
        height = 1000
        a, ok_pressed = QInputDialog.getText(self, 'Введите размеры',
                                             'Размер картинки(Ширина и высота через точку): ')
        if ok_pressed:
            try:
                width = int(a[:a.find('.')])
                height = int(a[a.find('.') + 1:])
            except ValueError:
                width = 1000
                height = 1000
        self.scaled_pixmap = self.pixmap.scaled(width, height, aspectRatioMode=Qt.KeepAspectRatio)
        self.label.resize(self.scaled_pixmap.width(), self.scaled_pixmap.height())
        self.label.setPixmap(self.scaled_pixmap)
        self.label.setStyleSheet("{border-image: {self.scaled_pixmap};}")
        self.flag = True

    def save(self):
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        pixmap = self.label.pixmap()
        ba = QByteArray()
        buff = QBuffer(ba)
        buff.open(QIODevice.WriteOnly)
        ok = pixmap.save(buff, 'PNG')
        assert ok
        im = ba.data()
        cur.execute('''INSERT INTO pictures(name) VALUES (?)''', [im])
        con.commit()
        cur.close()
        con.close()

    def clear(self):
        reply = QMessageBox.question(self, 'Очистка', 'Очистить?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            image = QPixmap(1500, 1000)
            image.fill(Qt.white)
            self.label.setPixmap(image)
            self.flag = False

    def mouseMoveEvent(self, event):
        painter = QPainter(self.label.pixmap())
        if type(self.color) == str:
            self.color = tuple(int(self.color.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))
        painter.setPen(QPen(QColor(*self.color)))
        n = 0
        if self.tool == 'ручка':
            painter.drawPoint(event.x() - 190, event.y())
            self.update()
        elif self.tool == 'кисть':
            n = self.n
        elif self.tool == 'стёрка':
            n = self.m
            painter.setPen(QColor('#FFFFFF'))
        if self.tool == 'кисть' or self.tool == 'стёрка':
            for i in range(n, 0, -1):
                painter.drawEllipse(event.x() - 190 - i // 2, event.y() - i // 2, i, i)
                self.update()
        if self.tool == 'спрей':
            for n in range(self.spray_particles):
                xo = random.gauss(0, self.n)
                yo = random.gauss(0, self.n)
                painter.drawPoint(event.x() - 190 + xo, event.y() + yo)
            self.update()
        painter.end()
        self.flag = True

    def mousePressEvent(self, event):
        painter = QPainter(self.label.pixmap())
        if type(self.color) == str:
            self.color = tuple(int(self.color.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))
        painter.setPen(QPen(QColor(*self.color)))
        n = 0
        if self.tool == 'ручка':
            painter.drawPoint(event.x() - 190, event.y())
            self.update()
        elif self.tool == 'кисть':
            n = self.n
        elif self.tool == 'стёрка':
            n = self.m
            painter.setPen(QColor('#FFFFFF'))
        if self.tool == 'кисть' or self.tool == 'стёрка':
            for i in range(n, 0, -1):
                painter.drawEllipse(event.x() - 190 - i // 2, event.y() - i // 2, i, i)
                self.update()
        if self.tool == 'спрей':
            for n in range(self.spray_particles):
                xo = random.gauss(0, self.n)
                yo = random.gauss(0, self.n)
                painter.drawPoint(event.x() - 190 + xo, event.y() + yo)
            self.update()
        self.pos1[0], self.pos1[1] = event.x() - 190 // 2, event.y()
        painter.end()
        self.flag = True

    def mouseReleaseEvent(self, event):
        self.pos2[0], self.pos2[1] = event.x() - 190, event.y()
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(self.width)
        if type(self.color) == str:
            self.color = tuple(int(self.color.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))
        pen.setColor(QColor(*self.color))
        painter.setPen(pen)
        if type(self.fillColor) == str:
            self.fillColor = tuple(int(self.fillColor.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))
        if self.tool == 'прямоугольник':
            brush = QBrush()
            if self.fillCheckBox.isChecked():
                brush.setColor(QColor(*self.fillColor))
                brush.setStyle(Qt.SolidPattern)
            else:
                brush.setColor(QColor('#ffffff'))
                brush.setStyle(Qt.SolidPattern)
            painter.setBrush(brush)
            painter.drawRect(self.pos1[0] - 95, self.pos1[1], event.x() - self.pos1[0] - 95, event.y() - self.pos1[1])
        if self.tool == 'линия':
            painter.drawLine(self.pos1[0] - 95, self.pos1[1], event.x() - 190, event.y())
        self.update()
        painter.end()

    def keyPressEvent(self, event):
        if Qt.Key_Control:
            self.pos1[1] = self.pos1[0]

    def closeEvent(self, event):
        if self.flag:
            reply = QMessageBox.question(self, "Закрытие", "Сохранить рисунок?",
                                         QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                         QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.save()
            elif reply == QMessageBox.Cancel:
                event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
