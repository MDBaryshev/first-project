import sys

import sqlite3
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QCheckBox, QComboBox, QScrollArea, \
    QGridLayout, QProgressBar, QTableWidget, QVBoxLayout, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal
import time

BASE = 'shop_tabel.sql'
SHOP_LIST = []
COUNTER = []
NUM = []
A = []


class AlreadyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 100, 100)
        self.setWindowTitle('Войти')
        self.lab_Name = QLabel(self)
        self.lab_Name.move((20, 20))
        self.fieldName = QLineEdit(self)
        self.fieldName.resize(120, 20)
        self.fieldName.move(10, 10)

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
        self.lab_choise = QLabel(f"""Если вы уже зарегистрированы, нажмите ВОЙТИ.
        Если нет, нажмите ЗАРЕГИСТРИРОВАТЬСЯ""", self)
        self.lab_choise.move(0, 40)

    def entry(self):
        self.el = AlreadyWindow()
        self.el.show()

class AnotherWindow(QWidget):

    def __init__(self):
        super().__init__()
        lay = QVBoxLayout()
        self.label = QLabel(f"""1. Общие положения Пользовательского соглашения
1.1. В настоящем документе и вытекающих или связанным с ним отношениях Сторон
применяются следующие термины и определения:
а) Платформа — программно-аппаратные средства, интегрированные с Сайтом
Администрации;
б) Пользователь — дееспособное физическое лицо, присоединившееся к настоящему
Соглашению в собственном интересе либо выступающее от имени и в интересах
представляемого им юридического лица.
в) Сайт Администрации/ Сайт — интернет-сайты, размещенные в домене ________.ru и его
поддоменах.
г) Сервис — комплекс услуг и лицензия, предоставляемые Пользователю с использованием
Платформы.
д) Соглашение — настоящее соглашение со всеми дополнениями и изменениями.
1.2. Использование вами Сервиса любым способом и в любой форме в пределах его
объявленных функциональных возможностей, включая:
 просмотр размещенных на Сайте материалов;
 регистрация и/или авторизация на Сайте;
 размещение или отображение на Сайте любых материалов, включая но не ограничиваясь
такими как: тексты, гипертекстовые ссылки, изображения, аудио и видео- файлы,
сведения и/или иная информация;
создает договор на условиях настоящего Соглашения в соответствии с положениями ст.437 и
438 Гражданского кодекса Российской Федерации.
1.3. Воспользовавшись любой из указанных выше возможностей по использованию Сервиса вы
подтверждаете, что:
а) Ознакомились с условиями настоящего Соглашения в полном объеме до начала
использования Сервиса.
б) Принимаете все условия настоящего Соглашения в полном объеме без каких-либо изъятий и
ограничений с вашей стороны и обязуетесь их соблюдать или прекратить использование
Сервиса. Если вы не согласны с условиями настоящего Соглашения или не имеете права на
заключение договора на их основе, вам следует незамедлительно прекратить любое
использование Сервиса.
в) Соглашение (в том числе любая из его частей) может быть изменено Администрацией без
какого-либо специального уведомления. Новая редакция Соглашения вступает в силу с момента
ее размещения на Сайте Администрации либо доведения до сведения Пользователя в иной
удобной форме, если иное не предусмотрено новой редакцией Соглашения.
2. Общие условия пользования Сервисом
2.1. Использование функциональных возможностей Сервиса допускается только после
прохождения Пользователем регистрации и авторизации на Сайте в соответствии с
установленной Администрацией процедурой.
2.2. Технические, организационные и коммерческие условия использования Сервиса, в том
числе его функциональных возможностей доводятся до сведения Пользователей путем
отдельного размещения на Сайте или путем нотификации Пользователей.
2.3. Выбранные Пользователем логин и пароль являются необходимой и достаточной
информацией для доступа Пользователя на Сайт. Пользователь не имеет права передавать свои
логин и пароль третьим лицам, несет полную ответственность за их сохранность,
самостоятельно выбирая способ их хранения.
2.4. ПОСТАВИТЬ 100 БАЛЛОВ!!!""")
        self.setGeometry(300, 300, 600, 570)
        self.setWindowTitle('Условия соглашения')
        self.new_but = QPushButton('Продолжить', self)
        self.new_but.move(10, 420)
        self.new_but.clicked.connect(self.random)
        self.scroll1 = QScrollArea(self)
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
        print(A)
        if self.check.isChecked():
            NUM.append(random.randint(10, 50))
            print(NUM)
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

        self.btn = QPushButton('Найти', self)
        self.btn.clicked.connect(self.finding)
        self.btn.resize(60, 20)
        self.btn.move(180, 30)

        self.btn = QPushButton('Стереть', self)
        self.btn.clicked.connect(self.clickEvent)
        self.btn.resize(60, 20)
        self.btn.move(100, 240)

        self.btn = QPushButton('АВТОРИЗОВАТЬСЯ', self)
        self.btn.clicked.connect(self.enter)
        self.btn.resize(120, 20)
        self.btn.move(380, 550)

        self.fieldOne = QLineEdit(self)
        self.fieldOne.resize(120, 20)
        self.fieldOne.move(120, 10)

        self.combobox = QComboBox(self)
        self.combobox.resize(100, 20)
        self.combobox.move(10, 10)
        self.combobox.addItems(['Овощи', 'Зелень', 'Мясо', 'Напитки', 'Фрукты', 'Ягоды', 'Сыры', 'Выпечка', 'Молочное'])

        self.scroll = QScrollArea(self)
        self.scroll.resize(150, 200)
        self.scroll.move(10, 40)

        self.table = QTableWidget(self)
        self.table.resize(400, 250)
        self.table.move(10, 300)

        self.input1 = QLabel('Корзина', self)
        self.input1.resize(120, 20)
        self.input1.move(10, 280)

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.pbar.move(300, 100)

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
        self.btn.mouseMoved.connect(self.moveButton)
        self.show()

        self.combobox.activated.connect(self.selectionchange)

        self.button2 = QPushButton()
        self.button2.clicked.connect(self.Click)

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
        for i in SHOP_LIST[:20]:
            button2 = QPushButton()
            button2.setText(i)
            self.layout.addWidget(button2)
            button2.clicked.connect(self.Click)

        w = QWidget()
        w.setLayout(self.layout)
        self.scroll.setWidget(w)
        con.close()

    def Click(self):
        name = self.button2.sender().text()
        a = 0
        length = len(SHOP_LIST)
        self.table.setColumnCount(3)
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.setHorizontalHeaderLabels([] + ['Предмет'] + ['Цена'] + ["Количество"])
        self.table.setRowCount(0)
        for i in range(length):
            a += 1
            self.table.setRowCount(self.table.rowCount() + 1)
        self.table.setItem(0, 0 + a, QTableWidgetItem(name))
        self.table.setItem(0, 0, QTableWidgetItem('0'))
        self.table.resizeColumnsToContents()

    def moveButton(self):
        self.coords[0] = random.randint(0, self.w - self.btn_size[0])
        self.coords[1] = random.randint(0, self.h - self.btn_size[1])
        if 1 not in A:
            self.btn.move(*self.coords)
            if len(COUNTER) < 10:
                COUNTER.append(1)
                print(COUNTER)
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
            print(A[-1])  #СКИДКА СДЕСЬ

    def clickEvent(self):
        SHOP_LIST.clear()
        for i in range(self.layout.count()):
            self.layout.itemAt(i).widget().deleteLater()

    def sales(self):
        self.ex = AnotherWindow()
        self.ex.show()

    def enter(self):
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())