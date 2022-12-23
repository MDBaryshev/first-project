import sys

import sqlite3
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QCheckBox, QComboBox, QScrollArea, \
    QGridLayout, QProgressBar, QTableWidget, QVBoxLayout, QHeaderView, QTableWidgetItem, QDialog
from PyQt5.QtCore import pyqtSignal
import time

SHOP_LIST = []
COUNTER = []
NUM = []
A = []
NAME = []
BASKET = []
BASKET_PRICE = []
END = []


class OrderWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 400, 320, 290)
        self.setWindowTitle('Заказать')
        self.home = QLineEdit(self)
        self.home.resize(120, 20)
        self.home.move(100, 50)
        self.order_home = QLabel('Адрес', self)
        self.order_home.resize(160, 30)
        self.order_home.move(100, 20)

        self.order_name = QLineEdit(self)
        self.order_name.resize(120, 20)
        self.order_name.move(100, 100)
        self.name = QLabel('Ваше ИМЯ', self)
        self.name.resize(160, 30)
        self.name.move(100, 70)

        self.phone = QLabel('Ваш ТЕЛЕФОН', self)
        self.phone.resize(160, 30)
        self.phone.move(100, 120)
        self.order_phone = QLineEdit(self)
        self.order_phone.resize(120, 20)
        self.order_phone.move(100, 150)
        self.combo_phone = QComboBox(self)
        self.combo_phone.move(40, 150)
        self.combo_phone.addItems(['+7', '+375', '+380', '+90'])

        self.next = QPushButton('Продолжить', self)
        self.next.move(200, 200)
        self.next.clicked.connect(self.ordering)
        self.next.setStyleSheet('background: rgb(100,220,30);')

        self.end = QLabel(self)
        self.end.resize(350, 100)
        self.end.move(10, 220)

    def ordering(self):
        info = []
        home = self.home.text()
        if home != '':
            info.append(home)
            self.home.setStyleSheet("QLineEdit { color: black; background-color: white;}")
        else:
            self.home.setStyleSheet("QLineEdit { color: white; background-color: red;}")
        name = self.order_name.text()
        if name != '':
            info.append(name)
            self.order_name.setStyleSheet("QLineEdit { color: black; background-color: white;}")
        else:
            self.order_name.setStyleSheet("QLineEdit { color: white; background-color: red;}")
        phon = self.order_phone.text()
        if phon != '' and len(phon) == 10:
            num = self.combo_phone.currentText()
            info.append(num + phon)
            self.order_phone.setStyleSheet("QLineEdit { color: black; background-color: white;}")
        else:
            self.order_phone.setStyleSheet("QLineEdit { color: white; background-color: red;}")
        if len(info) == 3:
            math = int(A[-1]) / 100
            end = END[-1] - (END[-1] * math)
            self.end.setText(f'''{info[1]} мы приняли ваш заказ на сумму:{end}, и привезем 
            его по адресу {info[0]}''')


class EnterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 400, 300, 150)
        self.setWindowTitle('Вход')
        self.enter_but = QPushButton('ВОЙТИ', self)
        self.enter_but.move(30, 100)
        self.enter_but.clicked.connect(self.entry)

        self.aut_but = QPushButton('АВТОРИЗОВАТЬСЯ', self)
        self.aut_but.move(170, 100)
        self.aut_but.clicked.connect(self.autorize)
        self.lab_choise = QLabel(f"""Если вы уже зарегистрированы, нажмите ВОЙТИ.
        Если нет, нажмите ЗАРЕГИСТРИРОВАТЬСЯ""", self)
        self.lab_choise.move(0, 40)

    def autorize(self):
        self.flas = FalseWindow()
        self.flas.show()
        self.close()

    def entry(self):
        self.true = TrueWindow()
        self.true.show()
        self.close()


class FalseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 333, 300, 270)
        self.setWindowTitle('Войти')
        self.field_name = QLineEdit(self)
        self.field_name.resize(120, 20)
        self.field_name.move(100, 50)
        self.label_name = QLabel('Ваше ИМЯ', self)
        self.label_name.resize(160, 30)
        self.label_name.move(100, 20)

        self.field_surname = QLineEdit(self)
        self.field_surname.resize(120, 20)
        self.field_surname.move(100, 100)
        self.label_surname = QLabel('Ваша ФАМИЛИЯ', self)
        self.label_surname.resize(160, 30)
        self.label_surname.move(100, 70)

        self.field_phone = QLineEdit(self)
        self.field_phone.resize(120, 20)
        self.field_phone.move(100, 150)
        self.combo = QComboBox(self)
        self.combo.move(40, 150)
        self.combo.addItems(['+7', '+375', '+380', '+90'])
        self.label_phone = QLabel('Ваш ТЕЛЕФОН', self)
        self.label_phone.resize(160, 30)
        self.label_phone.move(100, 120)

        self.field_pass = QLineEdit(self)
        self.field_pass.resize(120, 20)
        self.field_pass.move(100, 200)
        self.label_pass = QLabel('Ваш ПАРОЛЬ', self)
        self.label_pass.resize(160, 30)
        self.label_pass.move(100, 170)

        self.new_but = QPushButton('Продолжить', self)
        self.new_but.move(200, 240)
        self.new_but.clicked.connect(self.next)

    def next(self):
        sps_info = []
        name = self.field_name.text()
        if name != '':
            sps_info.append(name)
            self.field_name.setStyleSheet("QLineEdit { color: black; background-color: white;}")
        else:
            self.field_name.setStyleSheet("QLineEdit { color: white; background-color: red;}")
        surname = self.field_surname.text()
        if surname != '':
            sps_info.append(surname)
            self.field_surname.setStyleSheet("QLineEdit { color: black; background-color: white;}")
        else:
            self.field_surname.setStyleSheet("QLineEdit { color: white; background-color: red;}")
        phone = self.field_phone.text()
        if phone != '' and len(phone) == 10:
            num = self.combo.currentText()
            sps_info.append(num + phone)
            self.field_phone.setStyleSheet("QLineEdit { color: black; background-color: white;}")
        else:
            self.field_phone.setStyleSheet("QLineEdit { color: white; background-color: red;}")
        password = self.field_pass.text()
        if password != '':
            sps_info.append(password)
            self.field_pass.setStyleSheet("QLineEdit { color: black; background-color: white;}")
        else:
            self.field_pass.setStyleSheet("QLineEdit { color: white; background-color: red;}")
        file = open('C:/Users/Dell/people.txt', 'w', encoding='utf8')
        if len(sps_info) == 4:
            sps_info = ' '.join(sps_info)
            file.write(sps_info)
            NAME.append(name)
            self.close()
        file.close()


class TrueWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 333, 300, 270)
        self.setWindowTitle('Войти')

        self.aut_fon = QLineEdit(self)
        self.aut_fon.resize(120, 20)
        self.aut_fon.move(100, 150)
        self.aut_phone = QLabel('Ваш ТЕЛЕФОН', self)
        self.aut_phone.resize(160, 30)
        self.aut_phone.move(100, 120)

        self.aut_pass = QLineEdit(self)
        self.aut_pass.resize(120, 20)
        self.aut_pass.move(100, 200)
        self.aut_sec = QLabel('Ваш ПАРОЛЬ', self)
        self.aut_sec.resize(160, 30)
        self.aut_sec.move(100, 170)

        self.aut_combo = QComboBox(self)
        self.aut_combo.move(40, 150)
        self.aut_combo.addItems(['+7', '+375', '+380', '+90'])

        self.aut_but = QPushButton('Продолжить', self)
        self.aut_but.move(200, 240)
        self.aut_but.clicked.connect(self.enter)

    def enter(self):
        file = open('C:/Users/Dell/people.txt', encoding='utf8')
        f = file.read()
        fi = f.split(' ')
        last_num = fi[2]
        last_pass = fi[3]
        name = fi[0]
        file.close()
        phone = self.aut_fon.text()
        password = self.aut_pass.text()
        file.close()
        num = self.aut_combo.currentText()
        if last_num == (num + phone):
            self.aut_fon.setStyleSheet("QLineEdit { color: black; background-color: white;}")
        else:
            self.aut_fon.setStyleSheet("QLineEdit { color: white; background-color: red;}")
        if last_pass == password:
            self.aut_pass.setStyleSheet("QLineEdit { color: black; background-color: white;}")
        else:
            self.aut_pass.setStyleSheet("QLineEdit { color: white; background-color: red;}")
        if last_num == (num + phone) and last_pass == password:
            NAME.append(name)
            self.close()


class AnotherWindow(QWidget):

    def __init__(self):
        super().__init__()
        lay = QVBoxLayout()
        self.setStyleSheet('background: rgb(10,200,200);')
        f = open('C:/Users/Dell/info.txt', encoding='utf8')
        text = f.read()
        f.close()
        self.label = QLabel(text)
        self.setGeometry(300, 300, 600, 570)
        self.setWindowTitle('Условия соглашения')
        self.new_but = QPushButton('Продолжить', self)
        self.new_but.move(10, 420)
        self.new_but.setStyleSheet('background: rgb(255, 102, 0);')
        self.new_but.clicked.connect(self.random)
        self.scroll1 = QScrollArea(self)
        self.scroll1.setStyleSheet('background: rgb(255,255,255);')
        lay.addWidget(self.label)

        self.check = QCheckBox('Я честно все прочитал, ОСОБЕННО последний пункт', self)
        self.check.move(10, 400)

        self.wrong = QLabel(self)
        self.wrong.resize(160, 30)
        self.wrong.move(10, 450)

        wi = QWidget()
        wi.setLayout(lay)
        self.scroll1.setWidget(wi)

    def random(self):
        A.append(1)
        if self.check.isChecked():
            NUM.append(random.randint(10, 50))
            self.close()
        else:
            self.wrong.setText('Галочка обязательна!!!')


class Button(QPushButton):
    mouseMoved = pyqtSignal()

    def mouseMoveEvent(self, event):
        self.mouseMoved.emit()


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 500)
        self.setWindowTitle('Магазинчк')
        self.setStyleSheet('background: rgb(10,200,200);')

        self.btn = QPushButton('Найти', self)
        self.btn.clicked.connect(self.finding)
        self.btn.resize(60, 20)
        self.btn.move(180, 30)
        self.btn.setStyleSheet('background: rgb(100,220,30);')

        self.btn = QPushButton('Стереть', self)
        self.btn.clicked.connect(self.clickEvent)
        self.btn.resize(60, 20)
        self.btn.move(100, 240)
        self.btn.setStyleSheet('background: rgb(255,0,0);')

        self.btn = QPushButton('АВТОРИЗОВАТЬСЯ', self)
        self.btn.clicked.connect(self.enter)
        self.btn.resize(120, 20)
        self.btn.move(380, 550)
        self.btn.setStyleSheet('background: rgb(255, 102, 0);')

        self.fieldOne = QLineEdit(self)
        self.fieldOne.resize(120, 20)
        self.fieldOne.move(120, 10)
        self.fieldOne.setStyleSheet('background: rgb(255, 102, 0);')

        self.combobox = QComboBox(self)
        self.combobox.resize(100, 20)
        self.combobox.move(10, 10)
        self.combobox.addItems(['Овощи', 'Зелень', 'Мясо', 'Напитки', 'Фрукты', 'Ягоды', 'Сыры', 'Выпечка', 'Молочное'])
        self.combobox.setStyleSheet('background: rgb(255, 102, 0);')

        self.scroll = QScrollArea(self)
        self.scroll.resize(150, 200)
        self.scroll.move(10, 40)
        self.scroll.setStyleSheet('background: rgb(255, 102, 0);')

        self.table = QTableWidget(self)
        self.table.resize(400, 250)
        self.table.move(10, 300)

        self.input1 = QLabel('Корзина', self)
        self.input1.resize(120, 20)
        self.input1.move(10, 280)

        self.name = QLabel(self)
        self.name.resize(200, 20)
        self.name.move(300, 70)

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.pbar.move(300, 100)

        self.clear = QPushButton('Стереть все', self)
        self.clear.move(320, 300)
        self.clear.clicked.connect(self.delete_all)
        self.clear.setStyleSheet('background: rgb(255,0,0);')

        self.ord = QPushButton('Заказать', self)
        self.ord.move(320, 520)
        self.ord.clicked.connect(self.order)
        self.ord.setStyleSheet('background: rgb(100,220,30);')


        self.coords = [350, 5]
        self.btn_size = [120, 40]
        self.d = 15
        self.w = 500
        self.h = 570
        self.setGeometry(300, 300, self.w, self.h)
        self.btn = Button(self)
        self.btn.setMouseTracking(True)
        self.btn.setText("Получить скидку")
        self.btn.resize(*self.btn_size)
        self.btn.move(*self.coords)
        self.btn.mouseMoved.connect(self.movebutton)
        self.show()

        self.combobox.activated.connect(self.selectionchange)

        self.button2 = QPushButton()
        self.button2.clicked.connect(self.Click)
        self.button2.setStyleSheet('background: rgb(10,200,200);')

        self.layout = QGridLayout()

    def finding(self):
        SHOP_LIST.clear()
        for i in range(self.layout.count()):
            self.layout.itemAt(i).widget().deleteLater()
        key_word = (str(self.fieldOne.text())).lower()
        con = sqlite3.connect('films_db .sqlite')
        cur = con.cursor()
        result = cur.execute(f'''SELECT name FROM shops WHERE name LIKE '%{key_word}%' ''').fetchall()
        for elem in result[:6]:
            SHOP_LIST.append(*elem)
        for i in SHOP_LIST:
            button2 = QPushButton()
            button2.setText(i)
            self.layout.addWidget(button2)
            button2.clicked.connect(self.Click)

        w = QWidget()
        w.setLayout(self.layout)
        self.scroll.setWidget(w)
        con.close()

    def selectionchange(self):
        inp = (self.combobox.currentText()).lower()
        con = sqlite3.connect('films_db .sqlite')
        cur = con.cursor()
        result = cur.execute(f'''SELECT name FROM shops
        WHERE type = (SELECT id FROM products WHERE title LIKE '{inp}');''').fetchall()
        for elem in result[:6]:
            SHOP_LIST.append(*elem)
        for i in SHOP_LIST:
            button2 = QPushButton()
            button2.setText(i)
            button2.setStyleSheet('background: rgb(10,200,200);')
            self.layout.addWidget(button2)
            button2.clicked.connect(self.Click)

        w = QWidget()
        w.setLayout(self.layout)
        self.scroll.setWidget(w)
        con.close()

    def Click(self):
        name = (self.button2.sender().text()).lower()
        con = sqlite3.connect('films_db .sqlite')
        oyt = con.cursor()
        result = oyt.execute(f'''SELECT price FROM shops WHERE name LIKE '{name}';''').fetchall()
        con.close()
        BASKET.append(name)
        BASKET_PRICE.append(*result)
        price = []
        for i in BASKET_PRICE:
            price.append(*i)
        a = 0
        b = 0
        length = len(SHOP_LIST)
        self.table.setColumnCount(3)
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.setHorizontalHeaderLabels([] + ['Предмет'] + ['Цена'] + ['Сумма'])
        self.table.setRowCount(0)
        for i in range(length):
            self.table.setRowCount(self.table.rowCount() + 1)
        for item in BASKET:
            self.table.setItem(0 + a, 0, QTableWidgetItem(item))
            a += 1
        for jem in price:
            print(jem)
            self.table.setItem(0 + b, 1, QTableWidgetItem(str(jem)))
            b += 1
        if len(price) > 0:
            self.table.setItem(0, 2, QTableWidgetItem(f'Сумма:{sum(price)}'))
        END.append(sum(price))
        self.table.resizeColumnsToContents()

    def movebutton(self):
        self.coords[0] = random.randint(0, self.w - self.btn_size[0])
        self.coords[1] = random.randint(0, self.h - self.btn_size[1])
        if 1 not in A:
            self.btn.move(*self.coords)
            if len(COUNTER) < 10:
                COUNTER.append(1)
            else:
                button_sale = QPushButton()
                button_sale.setText('Xотите скидку?')
                self.layout.addWidget(button_sale)
                w = QWidget()
                w.setLayout(self.layout)
                self.scroll.setWidget(w)
                button_sale.clicked.connect(self.sales)
        else:
            for i in range(random.randint(0, 100)):
                time.sleep(0.05)
                self.pbar.setValue(i)
                self.coords[0] = 1000
                self.coords[1] = 1000
                self.btn.move(*self.coords)
                SHOP_LIST.clear()
                for item in range(self.layout.count()):
                    self.layout.itemAt(item).widget().deleteLater()
                A.append(i)

    def clickEvent(self):
        SHOP_LIST.clear()
        for i in range(self.layout.count()):
            self.layout.itemAt(i).widget().deleteLater()

    def sales(self):
        self.ex = AnotherWindow()
        self.ex.show()

    def enter(self):
        if len(NAME) > 0:
            a = NAME[-1]
            self.name.setText(f'{a} ваша личная скидка:')
        else:
            self.ent = EnterWindow()
            self.ent.show()

    def get_result(self):
        con = sqlite3.connect(BASE)
        cur = con.cursor()
        cur.execute(
            """
            """)
        con.commit()
        con.close()

    def delete_all(self):
        for i in range(len(SHOP_LIST)):
            self.table.setItem(i, 1, QTableWidgetItem(''))
            self.table.setItem(i, 0, QTableWidgetItem(''))
        BASKET.clear()
        BASKET_PRICE.clear()
        self.table.setItem(0, 2, QTableWidgetItem(f'Сумма:0'))

    def order(self):
        self.ow = OrderWindow()
        self.ow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
