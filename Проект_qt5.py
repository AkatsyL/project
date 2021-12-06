import sys
import sqlite3
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import QLabel, QMainWindow, QSlider, QPushButton, QLineEdit
from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog, QFileDialog
from PIL import Image
from PyQt5 import QtGui, QtWidgets, QtCore
flag = False
start = True
copy = ''
fname = ''
h_z = 800
v_z = 400


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI_2()

    def initUI_2(self):

        self.setGeometry(600, 400, 450, 300)
        self.setWindowTitle('Вход')

        self.log = QLineEdit(self)
        self.log.resize(200, 30)
        self.log.move(120, 60)

        self.pas = QLineEdit(self)
        self.pas.resize(200, 30)
        self.pas.move(120, 100)

        self.l_log = QLabel(self)
        self.l_log.setText('Логин:')
        self.l_log.move(75, 65)
        self.l_log.resize(50, 20)

        self.star_r = QPushButton('', self)
        self.star_r.move(10, 10)
        self.star_r.resize(5, 5)
        self.star_r.clicked.connect(self.rez)

        self.l_pas = QLabel(self)
        self.l_pas.setText('Пороль:')
        self.l_pas.move(70, 105)
        self.l_pas.resize(50, 20)

        self.dive = QLabel(self)
        self.dive.setText('')
        self.dive.move(150, 30)
        self.dive.resize(200, 20)

        self.star = QPushButton('Вход', self)
        self.star.move(100, 140)
        self.star.clicked.connect(self.start)

        self.reg = QPushButton('Регистрация', self)
        self.reg.move(240, 140)
        self.reg.clicked.connect(self.regis)

    def rez(self):
        self.close()
        self.test = Craft()
        self.test.show()

    def regis(self):
        self.close()
        self.test = Regis()
        self.test.show()

    def start(self):
        logs = self.log.text()
        pas = self.pas.text()
        log = []
        con = sqlite3.connect("ПРОЕКТ__Редактор_изображений/login.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM Name_foto""").fetchall()
        for elem in result:
            log.append(elem[1::1])

        con.close()
        print(log)
        for i in log:
            if str(logs) == str(i[0]) and str(pas) == str(i[-1]):
                self.close()
                self.test = Craft()
                self.test.show()
            else:
                self.dive.setText('Неверный логин или пороль')


class Regis(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI_0()

    def initUI_0(self):
        self.setGeometry(600, 400, 450, 250)
        self.setWindowTitle('Регистрация')
        self.retorn = QPushButton('Зарегистрироваться', self)
        self.retorn.move(300, 180)

        self.log = QLineEdit(self)
        self.log.resize(200, 30)
        self.log.move(120, 60)

        self.pas = QLineEdit(self)
        self.pas.resize(200, 30)
        self.pas.move(120, 100)

        self.l_log = QLabel(self)
        self.l_log.setText('Логин:')
        self.l_log.move(75, 70)

        self.l_pas = QLabel(self)
        self.l_pas.setText('Пороль:')
        self.l_pas.move(70, 110)

        self.res = QLineEdit(self)
        self.res.resize(200, 30)
        self.res.move(120, 140)

        self.l_pas = QLabel(self)
        self.l_pas.setText('Повторение пороля:')
        self.l_pas.move(10, 150)

        self.passive = QLabel(self)
        self.passive.resize(300, 20)
        self.passive.move(130, 30)
        self.retorn.clicked.connect(self.prov)

    def prov(self):
        global result
        logs = self.log.text()
        pas = self.pas.text()
        res = self.res.text()
        if logs == '' or pas == '' or res == '':
            self.passive.setText('Вы не ввели логин или пороль')
        elif not pas == res or not logs == '' and pas == '':
            if len(pas) <= 8:
                self.passive.setText('Пороль должен быть не неньше 8 символов')
            else:
                self.passive.setText('Пороли не совпадают')
        else:
            con = sqlite3.connect("ПРОЕКТ__Редактор_изображений/login.db")
            cur = con.cursor()
            result = cur.execute("""INSERT INTO Name_foto (name, password) VALUES(?, ?)""", (logs, pas))
            con.commit()

            con.close()
            self.passive.setText('готово')
            self.close()
            self.test = Example()
            self.test.show()


class Craft(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # сама программа

        self.setGeometry(400, 100, 850, 500)
        self.setWindowTitle('Py_foto')

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 100, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 255, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 212, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 113, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 212, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 212, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 113, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 212, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 212, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 113, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 100, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 250, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)


# кнопка выбора изображения
        self.btn_foto = QPushButton('Выбрать фото', self)
        self.btn_foto.resize(120, 30)
        self.btn_foto.move(10, 10)

        self.btn_color = QPushButton('цвет ', self)
        self.btn_color.resize(self.btn_color.sizeHint())
        self.btn_color.resize(120, 30)
        self.btn_color.move(170, 10)

        self.bth_h_l = QPushButton('Маштаб ', self)
        self.bth_h_l.resize(120, 30)
        self.bth_h_l.move(330, 10)
# место вывода и работы с изображением
        self.imag = QLabel(self)
        self.imag.move(10, 50)
        self.imag.resize(800, 400)
        self.finish = QPushButton('сохранить', self)
        self.finish.move(740, 460)

# действия кнопок и всякого
        self.btn_foto.clicked.connect(self.run_foto)
        if flag:
            self.btn_color.clicked.connect(self.run_color)
            self.bth_h_l.clicked.connect(self.run_h_l)
            self.finish.clicked.connect(self.run_save)

        self.pixmap = QtGui.QPixmap(copy).scaled(h_z, v_z)
        self.imag.setPixmap(self.pixmap)

    def run_save(self):
        imgs = Image.open(copy)
        cop = QtWidgets.QFileDialog.getSaveFileName(
            self, "где сохранить?", filter="Картинка (*.jpg;*.png)"
        )[0]
        imgs.save(cop)

# вывод изображения

    def run_foto(self):
        global flag
        global fname
        global fname_1
        global copy
        fname = QtWidgets.QFileDialog.getOpenFileName(
            self, "выбрать картинку", filter="Картинка (*.jpg;*.png)"
        )[0]
        fname_1 = fname
        copy = fname_1
        self.pixmap = QtGui.QPixmap(fname).scaled(h_z, v_z)
        self.imag.setPixmap(self.pixmap)

        self.btn_color.clicked.connect(self.run_color)
        self.bth_h_l.clicked.connect(self.run_h_l)
        self.finish.clicked.connect(self.run_save)
        flag = True

    def run_color(self):

        self.first = SecondForm()
        self.first.show()
        self.close()

    def run_h_l(self):
        self.second = TheyForm()
        self.second.show()
        self.close()


class SecondForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI_1()

    def initUI_1(self):

        self.setGeometry(600, 100, 820, 500)
        self.setWindowTitle('Палитра')

        self.imag_1 = QLabel(self)
        self.imag_1.move(10, -35)
        self.imag_1.resize(800, 480)
        self.pixmap = QtGui.QPixmap(fname).scaled(h_z, v_z)
        self.imag_1.setPixmap(self.pixmap)

        self.res = QPushButton('изменить', self)
        self.res.move(700, 420)

        self.exet = QPushButton('применить ', self)
        self.exet.move(700, 450)
        self.retorn = QPushButton('Сброс', self)
        self.retorn.move(700, 480)


# r регулятор
        self.sli_r = QSlider(Qt.Horizontal, self)
        self.sli_r.setGeometry(10, 415, 370, 17)
        self.sli_r.setMinimum(-255)
        self.sli_r.setMaximum(255)

        self.cl_r = QLineEdit(self)
        self.cl_r.setText(f'{int(0)}')
        self.cl_r.move(385, 410)

        self.label_r = QLabel(self)
        self.label_r.setText('Изменения тона R')
        self.label_r.move(535, 415)
# g регулятор
        self.sli_g = QSlider(Qt.Horizontal, self)
        self.sli_g.setGeometry(10, 445, 370, 17)
        self.sli_g.setMinimum(-255)
        self.sli_g.setMaximum(255)

        self.cl_g = QLineEdit(self)
        self.cl_g.setText(f'{int(0)}')
        self.cl_g.move(385, 440)

        self.label_g = QLabel(self)
        self.label_g.setText('Изменения тона G')
        self.label_g.move(535, 445)
# b регулятор
        self.sli_b = QSlider(Qt.Horizontal, self)
        self.sli_b.setGeometry(10, 475, 370, 17)
        self.sli_b.setMinimum(-255)
        self.sli_b.setMaximum(255)

        self.cl_b = QLineEdit(self)
        self.cl_b.setText(f'{int(0)}')
        self.cl_b.move(385, 470)

        self.label_b = QLabel(self)
        self.label_b.setText('Изменения тона B')
        self.label_b.move(535, 475)

        self.sli_r.valueChanged[int].connect(self.color_r)
        self.sli_g.valueChanged[int].connect(self.color_g)
        self.sli_b.valueChanged[int].connect(self.color_b)
        self.res.clicked.connect(self.result)
        self.retorn.clicked.connect(self.run_ret)
        self.exet.clicked.connect(self.clos)

    def run_ret(self):
        global copy
        self.pixmap = QtGui.QPixmap(fname_1).scaled(h_z, v_z)
        self.imag_1.setPixmap(self.pixmap)
        copy = fname_1

    def clos(self):
        global fname
        fname = copy
        self.close()
        self.color = Craft()
        self.color.show()

    def color_r(self, value_r):
        self.cl_r.setText(f'{int(value_r)}')

    def color_g(self, value_g):
        self.cl_g.setText(f'{int(value_g)}')

    def color_b(self, value_b):
        self.cl_b.setText(f'{int(value_b)}')

    def result(self):
        global copy
        r_2 = self.cl_r.text()
        g_2 = self.cl_g.text()
        b_2 = self.cl_b.text()
        img = Image.open(fname)
        pix = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pix[i, j]
                pix[i, j] = r + int(r_2), g + int(g_2), b + int(b_2)
        self.new_file = f"1{fname.split('/')[-1]}"
        img.save(self.new_file)
        self.pixmap = QtGui.QPixmap(self.new_file).scaled(h_z, v_z)
        copy = self.new_file
        self.imag_1.setPixmap(self.pixmap)


class TheyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI_2()

    def initUI_2(self):
        self.setGeometry(400, 100, 840, 470)
        self.setWindowTitle('Маштаб')
        self.info = QPushButton('Проверить', self)
        self.info.move(650, 440)

        self.res = QPushButton('Применить', self)
        self.res.move(750, 440)

        self.imag_3 = QLabel(self)
        self.imag_3.move(10, 10)
        self.imag_3.resize(810, 400)
        self.pixmap = QtGui.QPixmap(fname).scaled(h_z, v_z)
        self.imag_3.setPixmap(self.pixmap)

        self.sli_h = QSlider(Qt.Horizontal, self)
        self.sli_h.setGeometry(12, 413, 798, 20)
        self.sli_h.setMinimum(0)
        self.sli_h.setMaximum(800)
        self.sli_h.setTickPosition(QSlider.TicksAbove)
        self.sli_h.setTickInterval(20)

        self.sli_v = QSlider(Qt.Vertical, self)
        self.sli_v.setGeometry(813, 12, 20, 398)
        self.sli_v.setMinimum(0)
        self.sli_v.setMaximum(400)
        self.sli_v.setTickPosition(QSlider.TicksLeft)
        self.sli_v.setTickInterval(20)

        self.res.clicked.connect(self.run_res)
        self.info.clicked.connect(self.run_info)
        self.sli_h.valueChanged[int].connect(self.hor)
        self.sli_v.valueChanged[int].connect(self.ver)

    def hor(self, h):
        global h_z
        h_i = 800
        h_z = h_i - h

    def ver(self, v):
        global v_z
        v_i = 400
        v_z = v_i - v

    def run_res(self):
        global copy
        copy = fname
        self.close()
        self.color = Craft()
        self.color.show()

    def run_info(self):
        self.pixmap = QtGui.QPixmap(fname).scaled(h_z, v_z)
        self.imag_3.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())