from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QDialog, QInputDialog, QLineEdit
from PyQt5.QtCore import Qt,QCoreApplication
from PyQt5.QtGui import QPdfWriter, QPagedPaintDevice, QPainter, QScreen, QPixmap, QIcon, QFont
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5 import uic
import sys
import random
import numpy as np

words = np.load('./words.npy')
form_class = uic.loadUiType("ui.ui")[0]

class word_test(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.x = 0
        self.init_table()
        self.setWindowTitle("Apple 영어 This is voca")
        self.setWindowIcon(QIcon('./icon.png'))
        
        self.btn_1.clicked.connect(self.btn1clicked)
        self.btn_2.clicked.connect(self.btn2clicked)
        self.btn_3.clicked.connect(self.btn3clicked)
        self.btn_4.clicked.connect(self.btn4clicked)
        self.btn_quit.clicked.connect(QCoreApplication.instance().quit)

    def init_table(self):
        QTableWidget.clear(self.table)
        self.table.setRowCount(19)
        self.table.setColumnCount(4)

        self.mknum = self.table.rowCount()-15
        
        row = list(map(str,list(range(1,self.table.rowCount(),1))))
        for i in range(self.mknum):
            row.insert(0,'') 
        self.table.setVerticalHeaderLabels(row)

        col=['','','','']
        self.table.setHorizontalHeaderLabels(col)

        self.table.setSpan(0,0,2,4)
        self.table.setItem(0, 0, QTableWidgetItem("this is vocabulary"))
        self.table.item(0,0).setFont(QFont('Times',24 , QFont.Bold))
        for i in [0,2]:
            self.table.setItem(self.mknum-1, i, QTableWidgetItem("영어"))
            self.table.setItem(self.mknum-1, i+1, QTableWidgetItem("뜻"))
        
        title = ['This is Voca', 'Day '+str(self.x), '애플영어','이름 : ']
        for k in range(4):
            self.table.setItem(self.mknum-2,k,QTableWidgetItem(title[k]))
        
    
    # def change_eng(self):
        
    #     a = self.set_eng.text()
    #     if(a.isdemical):
            
    #     else:
    #         self.set_kor.setText('0')
    #         self.set_eng.setText('0')
                    
    def btn1clicked(self):
        self.init_table()
        self.answer=False
        self.x = self.set_day.text()
        self.x = int(self.x)
        self.eng = self.set_eng.text()
        self.eng = int(self.eng)

        self.kor = 30 - self.eng
        self.set_kor.setText(str(self.kor))
        self.table.setItem(self.mknum-2,1,QTableWidgetItem('Day : '+str(self.x)))

        self.ran = list(range(30))
        random.shuffle(self.ran)
       
        i = self.eng
        # self.table.setItem(0,0,QTableWidgetItem('This is voca'))
        # self.table.setItem(0,1,QTableWidgetItem('Day'+str(self.x)))
        # self.table.setItem(0,2,QTableWidgetItem('애플영어'))
        # self.table.setItem(0,3,QTableWidgetItem('이름 : '))
        
        
        # for r in range(self.table.rowCount()-2):
        #     for c in range(2):#self.table.columnCount()):
        #         self.table.setItem(r+2, c, QTableWidgetItem(words[self.x][ran[r]][c]))
        #     for p in range(2):
        #             self.table.setItem(r+2, p+2, QTableWidgetItem(words[self.x][ran[r+15]][p]))
        for r in range(self.table.rowCount()-self.mknum):
            for c in range(2):
                if i>0:
                    self.table.setItem(r+self.mknum, 0+c*2, QTableWidgetItem(words[self.x-1][self.ran[r+c*15]][0]))
                    i -= 1
                else:
                    self.table.setItem(r+self.mknum, 1+c*2, QTableWidgetItem(words[self.x-1][self.ran[r+c*15]][1]))

        for r in range(self.table.rowCount()-2):
            self.table.resizeRowToContents(r+2)
        
    # def btn2clicked(self):
    #     # pdf 생성
    #     pdf = QPdfWriter('.pdf')
    #     pdf.setPageSize(QPagedPaintDevice.A4)
 
    #     # 화면 캡쳐        
    #     screen = QApplication.primaryScreen()
    #     img = screen.grabWindow(self.winId(), 0,0, self.rect().width(),self.rect().height())
 
    #     # 3항 연산자 (a if test else b, 만약 test가 참이면 a, 아니면 b)
    #     # 이미지 크기는 큰 값 기준, PDF 크기는 작은값 기준(화면 초과 방지)
    #     img_size = img.width() if img.width()-img.height() > 0 else img.height()
    #     pdf_size = pdf.width() if pdf.width()-pdf.height() < 0 else pdf.height()
 
    #     # 최적 비율 얻기
    #     ratio = pdf_size / img_size
         
    #     # pdf에 쓰기
    #     qp = QPainter()
    #     qp.begin(pdf)
    #     qp.drawPixmap(0, 0, img.width()*ratio, img.height()*ratio, img)
    #     qp.end()

    def btn3clicked(self):
        # 프린터 생성, 실행
        printer = QPrinter()
        dlg = QPrintDialog(printer, self)
        if dlg.exec() == QDialog.Accepted:
            # Painter 생성
            qp = QPainter()
            qp.begin(printer)        
 
            # 여백 비율
            wgap = printer.pageRect().width()*0.1
            hgap = printer.pageRect().height()*0.1
 
            # 화면 중앙에 위젯 배치
            xscale = (printer.pageRect().width()-wgap)/self.table.width()
            yscale = (printer.pageRect().height()-hgap)/self.table.height()
            scale = xscale if xscale < yscale else yscale        
            qp.translate(printer.paperRect().x() + printer.pageRect().width()/2, printer.paperRect().y() + printer.pageRect().height()/2)
            qp.scale(scale, scale);
            qp.translate(-self.table.width()/2, -self.table.height()/2);
 
            # 인쇄
            self.table.render(qp)
 
            qp.end()

    def btn4clicked(self):
        if self.answer == False:
            for r in range(self.table.rowCount()-self.mknum):
                for c in range(2):
                    self.table.setItem(r+self.mknum, c, QTableWidgetItem(words[self.x-1][self.ran[r]][c]))
                for p in range(2):
                        self.table.setItem(r+self.mknum, p+2, QTableWidgetItem(words[self.x-1][self.ran[r+15]][p]))
            self.answer = True

        else :
            self.init_table()
            i = self.eng
            for r in range(self.table.rowCount()-self.mknum):
                for c in range(2):
                    if i>0:
                        self.table.setItem(r+self.mknum, 0+c*2, QTableWidgetItem(words[self.x-1][self.ran[r+c*15]][0]))
                        i -= 1
                    else:
                        self.table.setItem(r+self.mknum, 1+c*2, QTableWidgetItem(words[self.x-1][self.ran[r+c*15]][1]))
            self.answer = False
 
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = word_test()
    myWindow.show()
    app.exec_()