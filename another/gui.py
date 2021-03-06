# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dwh-gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from queries_etl import *
from database import *

mysql_check_member = ('''
                    SELECT * FROM history_etl WHERE id_tabel = 5
                    ORDER BY id DESC LIMIT 1
''')
mysql_check_buku = ('''
                    SELECT * FROM history_etl WHERE id_tabel = 1
                    ORDER BY id DESC LIMIT 1
''')
mysql_check_perpustakaan = ('''
                    SELECT * FROM history_etl WHERE id_tabel = 2
                    ORDER BY id DESC LIMIT 1
''')
mysql_check_peminjaman =('''
                    SELECT * FROM history_etl WHERE id_tabel = 7
                    ORDER BY id DESC LIMIT 1
''')

show_data_tabel_etl = ('''SELECT nama_tabel, start_row, end_row, `status`, tgl_proses FROM history_etl
INNER JOIN tb_tabel ON history_etl.`id_tabel` = tb_tabel.`id`
ORDER BY history_etl.`id` ASC''')

mysql_combobox_perpus = ('''SELECT nama_perpustakaan FROM dim_perpustakaan''')

mysql_combobox_member = ('''SELECT nama_member FROM dim_member''')

mysql_combobox_tahun = ('''SELECT tahun FROM fact_peminjaman_bulan GROUP BY tahun''')


class Ui_MainWindow(object):

    def loadData(self):
        result = self.queries_etl.mysql_db_etl(show_data_tabel_etl)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.tableWidget.setHorizontalHeaderLabels(['Nama Tabel', 'Data Awal', 'Data Akhir', 'Status', 'Waktu Proses'])
                header = self.tableWidget.horizontalHeader()
                header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        # cursor2.close()
    def comboboxPerpustaka(self):
        result = self.queries_etl.mysql_db_etl(mysql_combobox_perpus)
        # print(result)
        for i in range(0, len(result)):
            # print(result[i][0])
            self.comboPerpus.addItem(result[i][0])

    def comboboxMember(self):
        result = self.queries_etl.mysql_db_etl(mysql_combobox_member)
        # print(result)
        for i in range(0, len(result)):
            self.comboMember.addItem(result[i][0])
    def comboboxTahun(self):
        result = self.queries_etl.mysql_db_etl(mysql_combobox_tahun)
        # print(result)
        for i in range(0, len(result)):
            self.comboTahun.addItem(result[i][0])

    def setupUi(self, MainWindow):
        # conect file queries_etl
        self.queries_etl = query()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1110, 777)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1101, 741))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 1081, 441))

        # self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("prbauba"))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.buttonExtract = QtWidgets.QPushButton(self.tab)
        self.buttonExtract.setGeometry(QtCore.QRect(10, 550, 93, 28))
        self.buttonExtract.setObjectName("buttonExtract")
        # definisi button
        self.buttonExtract.clicked.connect(self.extractData)
        self.loadData()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(280, 110, 811, 571))
        self.tableWidget_2.setObjectName("tableWidget_2")
        # self.tableWidget_2.setRowCount(5)
        # self.tableWidget_2.setColumnCount(5)
        self.comboPerpus = QtWidgets.QComboBox(self.tab_2)
        self.comboPerpus.setGeometry(QtCore.QRect(60, 170, 161, 31))
        self.comboPerpus.setObjectName("comboPerpus")
        self.comboboxPerpustaka()
        self.comboMember = QtWidgets.QComboBox(self.tab_2)
        self.comboMember.setGeometry(QtCore.QRect(60, 290, 161, 31))
        self.comboMember.setObjectName("comboMember")
        self.comboboxMember()
        self.comboTahun = QtWidgets.QComboBox(self.tab_2)
        self.comboTahun.setGeometry(QtCore.QRect(60, 390, 161, 31))
        self.comboTahun.setObjectName("comboTahun")
        self.comboboxTahun()
        self.buttonLoad = QtWidgets.QPushButton(self.tab_2)
        self.buttonLoad.setGeometry(QtCore.QRect(60, 640, 131, 31))
        self.buttonLoad.setObjectName("buttonLoad")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1110, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.buttonLoad.clicked.connect(self.selectData)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonExtract.setText(_translate("MainWindow", "Extract Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Database"))
        self.comboPerpus.setCurrentText(_translate("MainWindow", "Pilih Perpustakaan"))
        # self.comboPerpus.setItemText(0, _translate("MainWindow", "Perpustakaan Bersama"))
        # self.comboPerpus.setItemText(1, _translate("MainWindow", "Perpustakaan Jurusan"))
        # self.comboMember.setCurrentText(_translate("MainWindow", "Deva"))
        # self.comboMember.setItemText(0, _translate("MainWindow", "Deva"))
        # self.comboMember.setItemText(1, _translate("MainWindow", "Agung"))
        # self.comboTahun.setCurrentText(_translate("MainWindow", "2017"))
        # self.comboTahun.setItemText(0, _translate("MainWindow", "2017"))
        # self.comboTahun.setItemText(1, _translate("MainWindow", "2018"))
        # self.comboTahun.setItemText(2, _translate("MainWindow", "2019"))
        self.buttonLoad.setText(_translate("MainWindow", "Load Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Data Warehouse"))

    # def getDataSQL(self):


    def extractData(self):
        self.queries_etl.check_member(mysql_check_member)
        self.queries_etl.check_buku(mysql_check_buku)
        self.queries_etl.check_cabang_perpustakaan(mysql_check_perpustakaan)
        self.queries_etl.check_fact_peminjaman_bulan(mysql_check_peminjaman)

    def selectData(self):
        value_perpus = self.comboPerpus.currentIndex()
        value_perpus += 1
        value_member = self.comboMember.currentIndex()
        value_member += 1
        value_tahun = self.comboTahun.currentText()
        # value_tahun += 1
        # print(value_perpus,value_member,value_tahun)

        get_book_name = ("SELECT nama_buku FROM dim_member INNER JOIN fact_peminjaman_bulan ON dim_member.`id` = fact_peminjaman_bulan.`id_dimMember` INNER JOIN dim_buku ON fact_peminjaman_bulan.`id_dimBuku` = dim_buku.`id` WHERE dim_member.`id`='"+str(value_member)+"' AND tahun = '"+value_tahun+"' GROUP BY nama_buku;")
        column_name = self.queries_etl.get_row_column(get_book_name)
        # print(column_name)
        get_month = ("SELECT bulan FROM dim_member INNER JOIN fact_peminjaman_bulan ON dim_member.`id` = fact_peminjaman_bulan.`id_dimMember` INNER JOIN dim_buku ON fact_peminjaman_bulan.`id_dimBuku` = dim_buku.`id` WHERE dim_member.`id`='"+str(value_member)+"' AND tahun = '"+value_tahun+"' GROUP BY bulan;")
        row_name = self.queries_etl.get_row_column(get_month)

        # print(row_name)

        array_item_column = []
        for x , item in enumerate(column_name):
            # print(x)
            # print("ISI COLUMN : ",item[0])

            array_item_column.append(item[0])
            self.tableWidget_2.insertColumn(x)
            header = self.tableWidget.horizontalHeader()
            self.tableWidget_2.setHorizontalHeaderLabels(array_item_column)
            header.setSectionResizeMode(x, QtWidgets.QHeaderView.Stretch)

            # self.tableWidget_2.clearSpans()

            # self.tableWidget_2.insertRow(x)
            # list_book = list(item)
            # list_book.insert(0,x)
            # print("print : ",list_book[x])
            # self.m_grid3.ClearGrid()
        #     self.tableWidget_2.setHorizontalHeaderLabels(list_book[x])
        #     # self.m_grid3.SetColLabelValue(x,list_book[1])
        array_item_row = []
        for x , item in enumerate(row_name):
            array_item_row.append(item[0])
            self.tableWidget_2.insertRow(x)
            self.tableWidget_2.setVerticalHeaderLabels(array_item_row)
        #     self.m_grid3.AppendRows(x)
        #     list_item = list(item)
        #     list_item.insert(0,x)
        #     print(list_item[1])
            # self.m_grid3.ClearGrid()
            # self.m_grid3.SetRowLabelValue(x,list_item[1])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

