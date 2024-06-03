from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RemoveWindow():
    def setupUi(self, MainWindow, list_of_trains):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1160, 540)
        MainWindow.setMaximumSize(QtCore.QSize(1160, 540))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setGeometry(QtCore.QRect(10, 20, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.mainLabel.setFont(font)
        self.mainLabel.setObjectName("mainLabel")
        self.labelFind = QtWidgets.QLabel(self.centralwidget)
        self.labelFind.setGeometry(QtCore.QRect(10, 80, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelFind.setFont(font)
        self.labelFind.setObjectName("labelFind")

        self.labelCode = QtWidgets.QLabel(self.centralwidget)
        self.labelCode.setGeometry(QtCore.QRect(10, 170, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCode.setFont(font)
        self.labelCode.setObjectName("labelCode")
        self.inputCodeOfTrain = QtWidgets.QLineEdit(self.centralwidget)
        self.inputCodeOfTrain.setGeometry(QtCore.QRect(140, 160, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inputCodeOfTrain.setFont(font)
        self.inputCodeOfTrain.setMouseTracking(True)
        self.inputCodeOfTrain.setTabletTracking(False)
        self.inputCodeOfTrain.setAutoFillBackground(False)
        self.inputCodeOfTrain.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.inputCodeOfTrain.setMaxLength(3)
        self.inputCodeOfTrain.setDragEnabled(False)
        self.inputCodeOfTrain.setReadOnly(False)
        self.inputCodeOfTrain.setClearButtonEnabled(True)
        self.inputCodeOfTrain.setObjectName("inputCodeOfTrain")

        self.labelDeparturePoint = QtWidgets.QLabel(self.centralwidget)
        self.labelDeparturePoint.setGeometry(QtCore.QRect(10, 170, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDeparturePoint.setFont(font)
        self.labelDeparturePoint.setObjectName("labelDeparturePoint")
        self.departurePoint = QtWidgets.QComboBox(self.centralwidget)
        self.departurePoint.setGeometry(QtCore.QRect(170, 170, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.departurePoint.setFont(font)
        self.departurePoint.setObjectName("departurePoint")
        self.departurePoint.addItem("")
        self.departurePoint.addItem("")
        self.departurePoint.addItem("")
        self.departurePoint.addItem("")
        self.departurePoint.addItem("")
        self.departurePoint.addItem("")
        self.departurePoint.addItem("")
        self.departurePoint.addItem("")
        self.departurePoint.addItem("")
        self.departurePoint.addItem("")
        self.departurePoint.addItem("")
        self.departurePoint.addItem("")
        self.departurePoint.addItem("")
        self.departurePoint.addItem("")
        self.departurePoint.addItem("")
        self.departurePoint.addItem("")
        self.labelArrivalPoint = QtWidgets.QLabel(self.centralwidget)
        self.labelArrivalPoint.setGeometry(QtCore.QRect(10, 170, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelArrivalPoint.setFont(font)
        self.labelArrivalPoint.setObjectName("labelArrivalPoint")
        self.arrivalPoint = QtWidgets.QComboBox(self.centralwidget)
        self.arrivalPoint.setGeometry(QtCore.QRect(160, 170, 151, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.arrivalPoint.setFont(font)
        self.arrivalPoint.setObjectName("arrivalPoint")
        self.arrivalPoint.addItem("")
        self.arrivalPoint.addItem("")
        self.arrivalPoint.addItem("")
        self.arrivalPoint.addItem("")
        self.arrivalPoint.addItem("")
        self.arrivalPoint.addItem("")
        self.arrivalPoint.addItem("")
        self.arrivalPoint.addItem("")
        self.arrivalPoint.addItem("")
        self.arrivalPoint.addItem("")
        self.arrivalPoint.addItem("")
        self.arrivalPoint.addItem("")
        self.arrivalPoint.addItem("")
        self.arrivalPoint.addItem("")
        self.arrivalPoint.addItem("")
        self.arrivalPoint.addItem("")

        self.labelDepartureDate = QtWidgets.QLabel(self.centralwidget)
        self.labelDepartureDate.setGeometry(QtCore.QRect(10, 170, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDepartureDate.setFont(font)
        self.labelDepartureDate.setObjectName("labelDepartureDate")
        self.departureDate = QtWidgets.QDateEdit(self.centralwidget)
        self.departureDate.setGeometry(QtCore.QRect(170, 170, 110, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.departureDate.setFont(font)
        self.departureDate.setInputMethodHints(QtCore.Qt.ImhDate | QtCore.Qt.ImhPreferNumbers)
        self.departureDate.setObjectName("departureDate")

        self.labelDepartureTime = QtWidgets.QLabel(self.centralwidget)
        self.labelDepartureTime.setGeometry(QtCore.QRect(10, 170, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDepartureTime.setFont(font)
        self.labelDepartureTime.setObjectName("labelDepartureTime")
        self.departureTimeLowLimit = QtWidgets.QTimeEdit(self.centralwidget)
        self.departureTimeLowLimit.setGeometry(QtCore.QRect(320, 170, 118, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.departureTimeLowLimit.setFont(font)
        self.departureTimeLowLimit.setInputMethodHints(QtCore.Qt.ImhPreferNumbers | QtCore.Qt.ImhTime)
        self.departureTimeLowLimit.setObjectName("departureTimeLowLimit")

        self.labelArrivalTime = QtWidgets.QLabel(self.centralwidget)
        self.labelArrivalTime.setGeometry(QtCore.QRect(10, 170, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelArrivalTime.setFont(font)
        self.labelArrivalTime.setObjectName("labelArrivalTime")
        self.arrivalTimeLowLimit = QtWidgets.QTimeEdit(self.centralwidget)
        self.arrivalTimeLowLimit.setGeometry(QtCore.QRect(300, 170, 118, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.arrivalTimeLowLimit.setFont(font)
        self.arrivalTimeLowLimit.setInputMethodHints(QtCore.Qt.ImhPreferNumbers | QtCore.Qt.ImhTime)
        self.arrivalTimeLowLimit.setObjectName("arrivalTimeLowLimit")

        self.labelDepartureTime2 = QtWidgets.QLabel(self.centralwidget)
        self.labelDepartureTime2.setGeometry(QtCore.QRect(460, 170, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDepartureTime2.setFont(font)
        self.labelDepartureTime2.setObjectName("labelDepartureTime2")
        self.departureTimeHighLimit = QtWidgets.QTimeEdit(self.centralwidget)
        self.departureTimeHighLimit.setGeometry(QtCore.QRect(500, 170, 118, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.departureTimeHighLimit.setFont(font)
        self.departureTimeHighLimit.setInputMethodHints(QtCore.Qt.ImhPreferNumbers | QtCore.Qt.ImhTime)
        self.departureTimeHighLimit.setObjectName("departureTimeHighLimit")

        self.arrivalTimeHighLimit = QtWidgets.QTimeEdit(self.centralwidget)
        self.arrivalTimeHighLimit.setGeometry(QtCore.QRect(480, 170, 118, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.arrivalTimeHighLimit.setFont(font)
        self.arrivalTimeHighLimit.setInputMethodHints(QtCore.Qt.ImhPreferNumbers | QtCore.Qt.ImhTime)
        self.arrivalTimeHighLimit.setObjectName("arrivalTimeHighLimit")
        self.labelArrivalTime2 = QtWidgets.QLabel(self.centralwidget)
        self.labelArrivalTime2.setGeometry(QtCore.QRect(440, 170, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelArrivalTime2.setFont(font)
        self.labelArrivalTime2.setObjectName("labelArrivalTime2")

        self.labelTravelTime = QtWidgets.QLabel(self.centralwidget)
        self.labelTravelTime.setGeometry(QtCore.QRect(10, 170, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelTravelTime.setFont(font)
        self.labelTravelTime.setObjectName("labelTravelTime")
        self.travelTimeLowLimit = QtWidgets.QTimeEdit(self.centralwidget)
        self.travelTimeLowLimit.setGeometry(QtCore.QRect(370, 170, 118, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.travelTimeLowLimit.setFont(font)
        self.travelTimeLowLimit.setInputMethodHints(QtCore.Qt.ImhPreferNumbers | QtCore.Qt.ImhTime)
        self.travelTimeLowLimit.setObjectName("travelTimeLowLimit")
        self.travelTimeHighLimit = QtWidgets.QTimeEdit(self.centralwidget)
        self.travelTimeHighLimit.setGeometry(QtCore.QRect(670, 170, 118, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.travelTimeHighLimit.setFont(font)
        self.travelTimeHighLimit.setInputMethodHints(QtCore.Qt.ImhPreferNumbers | QtCore.Qt.ImhTime)
        self.travelTimeHighLimit.setObjectName("travelTimeHighLimit")
        self.labelTravelTime2 = QtWidgets.QLabel(self.centralwidget)
        self.labelTravelTime2.setGeometry(QtCore.QRect(510, 170, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelTravelTime2.setFont(font)
        self.labelTravelTime2.setObjectName("labelTravelTime2")

        self.labelCountOfDatsLowLimit = QtWidgets.QLabel(self.centralwidget)
        self.labelCountOfDatsLowLimit.setGeometry(QtCore.QRect(315, 165, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCountOfDatsLowLimit.setFont(font)
        self.labelCountOfDatsLowLimit.setObjectName("labelCountOfDatsLowLimit")

        self.labelCountOfDatsHighLimit = QtWidgets.QLabel(self.centralwidget)
        self.labelCountOfDatsHighLimit.setGeometry(QtCore.QRect(610, 165, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCountOfDatsHighLimit.setFont(font)
        self.labelCountOfDatsHighLimit.setObjectName("labelCountOfDatsLowLimit")

        self.countOfDaysLowLimit = QtWidgets.QComboBox(self.centralwidget)
        self.countOfDaysLowLimit.setGeometry(QtCore.QRect(260, 170, 35, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.countOfDaysLowLimit.setFont(font)
        self.countOfDaysLowLimit.setObjectName("countOfDaysLowLimit")
        self.countOfDaysLowLimit.addItem("")
        self.countOfDaysLowLimit.addItem("")
        self.countOfDaysLowLimit.addItem("")
        self.countOfDaysLowLimit.addItem("")
        self.countOfDaysLowLimit.addItem("")
        self.countOfDaysLowLimit.addItem("")
        self.countOfDaysLowLimit.addItem("")
        self.countOfDaysLowLimit.addItem("")

        self.countOfDaysHighLimit = QtWidgets.QComboBox(self.centralwidget)
        self.countOfDaysHighLimit.setGeometry(QtCore.QRect(550, 170, 35, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.countOfDaysHighLimit.setFont(font)
        self.countOfDaysHighLimit.setObjectName("countOfDaysHighLimit")
        self.countOfDaysHighLimit.addItem("")
        self.countOfDaysHighLimit.addItem("")
        self.countOfDaysHighLimit.addItem("")
        self.countOfDaysHighLimit.addItem("")
        self.countOfDaysHighLimit.addItem("")
        self.countOfDaysHighLimit.addItem("")
        self.countOfDaysHighLimit.addItem("")
        self.countOfDaysHighLimit.addItem("")

        self.labelCode.hide()
        self.inputCodeOfTrain.hide()
        self.labelDeparturePoint.hide()
        self.departurePoint.hide()
        self.labelArrivalPoint.hide()
        self.arrivalPoint.hide()
        self.labelDepartureDate.hide()
        self.departureDate.hide()
        self.labelDepartureTime.hide()
        self.departureTimeLowLimit.hide()
        self.labelArrivalTime.hide()
        self.arrivalTimeLowLimit.hide()
        self.labelDepartureTime2.hide()
        self.departureTimeHighLimit.hide()
        self.arrivalTimeHighLimit.hide()
        self.labelArrivalTime2.hide()
        self.labelTravelTime.hide()
        self.travelTimeLowLimit.hide()
        self.travelTimeHighLimit.hide()
        self.labelTravelTime2.hide()
        self.labelCountOfDatsLowLimit.hide()
        self.labelCountOfDatsHighLimit.hide()
        self.countOfDaysLowLimit.hide()
        self.countOfDaysHighLimit.hide()

        self.selectionOfSearchParameter = QtWidgets.QComboBox(self.centralwidget)
        self.selectionOfSearchParameter.setGeometry(QtCore.QRect(10, 110, 1140, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectionOfSearchParameter.setFont(font)
        self.selectionOfSearchParameter.setObjectName("selectionOfSearchParameter")
        self.selectionOfSearchParameter.addItem("")
        self.selectionOfSearchParameter.addItem("")
        self.selectionOfSearchParameter.addItem("")
        self.selectionOfSearchParameter.addItem("")
        self.selectionOfSearchParameter.addItem("")
        self.selectionOfSearchParameter.addItem("")
        self.selectionOfSearchParameter.addItem("")
        self.selectionOfSearchParameter.addItem("")
        self.btnDel = QtWidgets.QPushButton(self.centralwidget)
        self.btnDel.setGeometry(QtCore.QRect(1050, 490, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnDel.setFont(font)
        self.btnDel.setStyleSheet("background-color: rgb(187, 73, 51);\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0.881, x2:0.494, y2:0.159, stop:0.210227 rgba(187, 73, 51, 255), stop:1 rgba(224, 149, 135, 255));\n"
"color: rgb(255, 255, 255);")
        self.btnDel.setObjectName("btnDel")
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(940, 490, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName("btnCancel")
        self.Table = QtWidgets.QTableWidget(self.centralwidget)
        self.Table.setGeometry(QtCore.QRect(10, 260, 1140, 210))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Table.setFont(font)
        self.Table.setMouseTracking(False)
        self.Table.setTabletTracking(False)
        self.Table.setToolTip("")
        self.Table.setStatusTip("")
        self.Table.setWhatsThis("")
        self.Table.setAccessibleName("")
        self.Table.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Table.setAutoScroll(False)
        self.Table.setAutoScrollMargin(10)
        self.Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Table.setTabKeyNavigation(True)
        self.Table.setProperty("showDropIndicator", True)
        self.Table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.Table.setObjectName("Table")
        self.Table.setColumnCount(8)
        self.Table.setRowCount(len(list_of_trains))
        for i in range(0, len(list_of_trains)):
            item = QtWidgets.QTableWidgetItem()
            self.Table.setVerticalHeaderItem(i, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(7, item)

        for j in range(0, 8):
            for i in range(0, len(list_of_trains)):
                item = QtWidgets.QTableWidgetItem()
                self.Table.setItem(i, j, item)

        self.Table.horizontalHeader().setVisible(True)
        self.Table.horizontalHeader().setCascadingSectionResizes(True)
        self.Table.horizontalHeader().setDefaultSectionSize(140)
        self.Table.horizontalHeader().setHighlightSections(True)
        self.Table.horizontalHeader().setMinimumSectionSize(49)
        self.Table.horizontalHeader().setSortIndicatorShown(False)
        self.Table.horizontalHeader().setStretchLastSection(False)
        self.Table.verticalHeader().setVisible(False)
        self.Table.verticalHeader().setCascadingSectionResizes(False)
        self.Table.verticalHeader().setDefaultSectionSize(22)
        self.Table.verticalHeader().setMinimumSectionSize(20)
        self.Table.verticalHeader().setSortIndicatorShown(False)
        self.Table.verticalHeader().setStretchLastSection(False)
        self.btnFind = QtWidgets.QPushButton(self.centralwidget)
        self.btnFind.setGeometry(QtCore.QRect(1050, 220, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnFind.setFont(font)
        self.btnFind.setObjectName("btnFind")
        self.labelCountOfFind = QtWidgets.QLabel(self.centralwidget)
        self.labelCountOfFind.setGeometry(QtCore.QRect(10, 480, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelCountOfFind.setFont(font)
        self.labelCountOfFind.setObjectName("labelCountOfFind")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow, list_of_trains)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.selectionOfSearchParameter.currentIndexChanged.connect(self.add_search_parameters)

    def retranslateUi(self, MainWindow, list_of_trains):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Удаление"))
        self.mainLabel.setText(_translate("MainWindow", "Удаление маршрута"))
        self.labelFind.setText(_translate("MainWindow", "Параметр выборки"))
        self.selectionOfSearchParameter.setItemText(0, _translate("MainWindow", "Выбрать"))
        self.selectionOfSearchParameter.setItemText(1, _translate("MainWindow", "По номеру поезда"))
        self.selectionOfSearchParameter.setItemText(2, _translate("MainWindow", "По станции отправления"))
        self.selectionOfSearchParameter.setItemText(3, _translate("MainWindow", "По станции прибытия"))
        self.selectionOfSearchParameter.setItemText(4, _translate("MainWindow", "По дате отправления"))
        self.selectionOfSearchParameter.setItemText(5, _translate("MainWindow", "По времени отправления"))
        self.selectionOfSearchParameter.setItemText(6, _translate("MainWindow", "По времени прибытия"))
        self.selectionOfSearchParameter.setItemText(7, _translate("MainWindow", "По времени в пути"))
        self.btnDel.setText(_translate("MainWindow", "Удалить"))
        self.btnCancel.setText(_translate("MainWindow", "Отмена"))
        item = self.Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Номер поезда"))
        item = self.Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ст. отправления"))
        item = self.Table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ст. прибытия"))
        item = self.Table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата оправления"))
        item = self.Table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Время оправления"))
        item = self.Table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Дата прибытия"))
        item = self.Table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Время прибытия"))
        item = self.Table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Время в пути"))
        __sortingEnabled = self.Table.isSortingEnabled()
        self.Table.setSortingEnabled(False)
        for index in range(0, len(list_of_trains)):
            item = self.Table.item(index, 0)
            item.setText(_translate("MainWindow", list_of_trains[index].number_of_train))
            item = self.Table.item(index, 1)
            item.setText(_translate("MainWindow", list_of_trains[index].first_station))
            item = self.Table.item(index, 2)
            item.setText(_translate("MainWindow", list_of_trains[index].last_station))
            item = self.Table.item(index, 3)
            item.setText(_translate("MainWindow", list_of_trains[index].departure_date))
            item = self.Table.item(index, 4)
            item.setText(_translate("MainWindow", list_of_trains[index].departure_time))
            item = self.Table.item(index, 5)
            item.setText(_translate("MainWindow", list_of_trains[index].arrival_date))
            item = self.Table.item(index, 6)
            item.setText(_translate("MainWindow", list_of_trains[index].arrival_time))
            item = self.Table.item(index, 7)
            item.setText(_translate("MainWindow", str(list_of_trains[index].travel_time)))
        self.Table.setSortingEnabled(__sortingEnabled)
        self.btnFind.setText(_translate("MainWindow", "Найти"))
        self.labelCode.setText(_translate("MainWindow", "Номер поезда"))
        self.inputCodeOfTrain.setText(_translate("MainWindow", "000"))
        self.labelDeparturePoint.setText(_translate("MainWindow", "Пункт отправления"))
        self.departurePoint.setItemText(0, _translate("MainWindow", "Выбрать пункт"))
        self.departurePoint.setItemText(1, _translate("MainWindow", "Минск"))
        self.departurePoint.setItemText(2, _translate("MainWindow", "Брест"))
        self.departurePoint.setItemText(3, _translate("MainWindow", "Витебск"))
        self.departurePoint.setItemText(4, _translate("MainWindow", "Гомель"))
        self.departurePoint.setItemText(5, _translate("MainWindow", "Гродно"))
        self.departurePoint.setItemText(6, _translate("MainWindow", "Могилев"))
        self.departurePoint.setItemText(7, _translate("MainWindow", "Жлобин"))
        self.departurePoint.setItemText(8, _translate("MainWindow", "Калинковичи"))
        self.departurePoint.setItemText(9, _translate("MainWindow", "Лида"))
        self.departurePoint.setItemText(10, _translate("MainWindow", "Орша"))
        self.departurePoint.setItemText(11, _translate("MainWindow", "Пинск"))
        self.departurePoint.setItemText(12, _translate("MainWindow", "Полоцк"))
        self.departurePoint.setItemText(13, _translate("MainWindow", "Адлер"))
        self.departurePoint.setItemText(14, _translate("MainWindow", "Москва"))
        self.departurePoint.setItemText(15, _translate("MainWindow", "С.Петербург"))
        self.labelArrivalPoint.setText(_translate("MainWindow", "Пункт прибытия"))
        self.arrivalPoint.setItemText(0, _translate("MainWindow", "Выбрать пункт"))
        self.arrivalPoint.setItemText(1, _translate("MainWindow", "Минск"))
        self.arrivalPoint.setItemText(2, _translate("MainWindow", "Брест"))
        self.arrivalPoint.setItemText(3, _translate("MainWindow", "Витебск"))
        self.arrivalPoint.setItemText(4, _translate("MainWindow", "Гомель"))
        self.arrivalPoint.setItemText(5, _translate("MainWindow", "Гродно"))
        self.arrivalPoint.setItemText(6, _translate("MainWindow", "Могилев"))
        self.arrivalPoint.setItemText(7, _translate("MainWindow", "Жлобин"))
        self.arrivalPoint.setItemText(8, _translate("MainWindow", "Калинковичи"))
        self.arrivalPoint.setItemText(9, _translate("MainWindow", "Лида"))
        self.arrivalPoint.setItemText(10, _translate("MainWindow", "Орша"))
        self.arrivalPoint.setItemText(11, _translate("MainWindow", "Пинск"))
        self.arrivalPoint.setItemText(12, _translate("MainWindow", "Полоцк"))
        self.arrivalPoint.setItemText(13, _translate("MainWindow", "Адлер"))
        self.arrivalPoint.setItemText(14, _translate("MainWindow", "Москва"))
        self.arrivalPoint.setItemText(15, _translate("MainWindow", "С.Петербург"))
        self.labelDepartureDate.setText(_translate("MainWindow", "Дата отправления"))
        self.labelDepartureTime.setText(_translate("MainWindow", "Время отправления в промежутке    от "))
        self.labelArrivalTime.setText(_translate("MainWindow", "Время прибытия в промежутке    от"))
        self.labelDepartureTime2.setText(_translate("MainWindow", "до"))
        self.labelArrivalTime2.setText(_translate("MainWindow", "до"))
        self.labelTravelTime.setText(_translate("MainWindow", "Время в пути промежутке    от"))
        self.labelTravelTime2.setText(_translate("MainWindow", "до"))
        self.labelCountOfFind.setText(_translate("MainWindow", f"Найдено {len(list_of_trains)} маршрутов"))
        self.labelCountOfDatsLowLimit.setText(_translate("MainWindow", 'дней'))
        self.labelCountOfDatsHighLimit.setText(_translate("MainWindow", 'дней'))
        self.countOfDaysLowLimit.currentIndexChanged.connect(self.add_label_low_parameter)
        self.countOfDaysHighLimit.currentIndexChanged.connect(self.add_label_high_parameter)
        self.countOfDaysLowLimit.setItemText(0, _translate("MainWindow", "0"))
        self.countOfDaysLowLimit.setItemText(1, _translate("MainWindow", "1"))
        self.countOfDaysLowLimit.setItemText(2, _translate("MainWindow", "2"))
        self.countOfDaysLowLimit.setItemText(3, _translate("MainWindow", "3"))
        self.countOfDaysLowLimit.setItemText(4, _translate("MainWindow", "4"))
        self.countOfDaysLowLimit.setItemText(5, _translate("MainWindow", "5"))
        self.countOfDaysLowLimit.setItemText(6, _translate("MainWindow", "6"))
        self.countOfDaysLowLimit.setItemText(7, _translate("MainWindow", "7"))
        self.countOfDaysHighLimit.setItemText(0, _translate("MainWindow", "0"))
        self.countOfDaysHighLimit.setItemText(1, _translate("MainWindow", "1"))
        self.countOfDaysHighLimit.setItemText(2, _translate("MainWindow", "2"))
        self.countOfDaysHighLimit.setItemText(3, _translate("MainWindow", "3"))
        self.countOfDaysHighLimit.setItemText(4, _translate("MainWindow", "4"))
        self.countOfDaysHighLimit.setItemText(5, _translate("MainWindow", "5"))
        self.countOfDaysHighLimit.setItemText(6, _translate("MainWindow", "6"))
        self.countOfDaysHighLimit.setItemText(7, _translate("MainWindow", "7"))

    def add_label_low_parameter(self, index):
        _translate = QtCore.QCoreApplication.translate
        if index == 1:
            self.labelCountOfDatsLowLimit.setText(_translate("MainWindow", 'дня'))
        else:
            self.labelCountOfDatsLowLimit.setText(_translate("MainWindow", 'дней'))

    def add_label_high_parameter(self, index):
        _translate = QtCore.QCoreApplication.translate
        if index == 1:
            self.labelCountOfDatsHighLimit.setText(_translate("MainWindow", 'дня'))
        else:
            self.labelCountOfDatsHighLimit.setText(_translate("MainWindow", 'дней'))

    def add_search_parameters(self, index):
        if index == 1:
            self.labelCode.show()
            self.inputCodeOfTrain.show()
            self.labelDeparturePoint.hide()
            self.departurePoint.hide()
            self.labelArrivalPoint.hide()
            self.arrivalPoint.hide()
            self.labelDepartureDate.hide()
            self.departureDate.hide()
            self.labelDepartureTime.hide()
            self.departureTimeLowLimit.hide()
            self.labelArrivalTime.hide()
            self.arrivalTimeLowLimit.hide()
            self.labelDepartureTime2.hide()
            self.departureTimeHighLimit.hide()
            self.arrivalTimeHighLimit.hide()
            self.labelArrivalTime2.hide()
            self.labelTravelTime.hide()
            self.travelTimeLowLimit.hide()
            self.travelTimeHighLimit.hide()
            self.labelTravelTime2.hide()
            self.labelCountOfDatsLowLimit.hide()
            self.labelCountOfDatsHighLimit.hide()
            self.countOfDaysLowLimit.hide()
            self.countOfDaysHighLimit.hide()
        elif index == 2:
            self.labelCode.hide()
            self.inputCodeOfTrain.hide()
            self.labelDeparturePoint.show()
            self.departurePoint.show()
            self.labelArrivalPoint.hide()
            self.arrivalPoint.hide()
            self.labelDepartureDate.hide()
            self.departureDate.hide()
            self.labelDepartureTime.hide()
            self.departureTimeLowLimit.hide()
            self.labelArrivalTime.hide()
            self.arrivalTimeLowLimit.hide()
            self.labelDepartureTime2.hide()
            self.departureTimeHighLimit.hide()
            self.arrivalTimeHighLimit.hide()
            self.labelArrivalTime2.hide()
            self.labelTravelTime.hide()
            self.travelTimeLowLimit.hide()
            self.travelTimeHighLimit.hide()
            self.labelTravelTime2.hide()
            self.labelCountOfDatsLowLimit.hide()
            self.labelCountOfDatsHighLimit.hide()
            self.countOfDaysLowLimit.hide()
            self.countOfDaysHighLimit.hide()
        elif index == 3:
            self.labelCode.hide()
            self.inputCodeOfTrain.hide()
            self.labelDeparturePoint.hide()
            self.departurePoint.hide()
            self.labelArrivalPoint.show()
            self.arrivalPoint.show()
            self.labelDepartureDate.hide()
            self.departureDate.hide()
            self.labelDepartureTime.hide()
            self.departureTimeLowLimit.hide()
            self.labelArrivalTime.hide()
            self.arrivalTimeLowLimit.hide()
            self.labelDepartureTime2.hide()
            self.departureTimeHighLimit.hide()
            self.arrivalTimeHighLimit.hide()
            self.labelArrivalTime2.hide()
            self.labelTravelTime.hide()
            self.travelTimeLowLimit.hide()
            self.travelTimeHighLimit.hide()
            self.labelTravelTime2.hide()
            self.labelCountOfDatsLowLimit.hide()
            self.labelCountOfDatsHighLimit.hide()
            self.countOfDaysLowLimit.hide()
            self.countOfDaysHighLimit.hide()
        elif index == 4:
            self.labelCode.hide()
            self.inputCodeOfTrain.hide()
            self.labelDeparturePoint.hide()
            self.departurePoint.hide()
            self.labelArrivalPoint.hide()
            self.arrivalPoint.hide()
            self.labelDepartureDate.show()
            self.departureDate.show()
            self.labelDepartureTime.hide()
            self.departureTimeLowLimit.hide()
            self.labelArrivalTime.hide()
            self.arrivalTimeLowLimit.hide()
            self.labelDepartureTime2.hide()
            self.departureTimeHighLimit.hide()
            self.arrivalTimeHighLimit.hide()
            self.labelArrivalTime2.hide()
            self.labelTravelTime.hide()
            self.travelTimeLowLimit.hide()
            self.travelTimeHighLimit.hide()
            self.labelTravelTime2.hide()
            self.labelCountOfDatsLowLimit.hide()
            self.labelCountOfDatsHighLimit.hide()
            self.countOfDaysLowLimit.hide()
            self.countOfDaysHighLimit.hide()
        elif index == 5:
            self.labelCode.hide()
            self.inputCodeOfTrain.hide()
            self.labelDeparturePoint.hide()
            self.departurePoint.hide()
            self.labelArrivalPoint.hide()
            self.arrivalPoint.hide()
            self.labelDepartureDate.hide()
            self.departureDate.hide()
            self.labelDepartureTime.show()
            self.departureTimeLowLimit.show()
            self.labelArrivalTime.hide()
            self.arrivalTimeLowLimit.hide()
            self.labelDepartureTime2.show()
            self.departureTimeHighLimit.show()
            self.arrivalTimeHighLimit.hide()
            self.labelArrivalTime2.hide()
            self.labelTravelTime.hide()
            self.travelTimeLowLimit.hide()
            self.travelTimeHighLimit.hide()
            self.labelTravelTime2.hide()
            self.labelCountOfDatsLowLimit.hide()
            self.labelCountOfDatsHighLimit.hide()
            self.countOfDaysLowLimit.hide()
            self.countOfDaysHighLimit.hide()
        elif index == 6:
            self.labelCode.hide()
            self.inputCodeOfTrain.hide()
            self.labelDeparturePoint.hide()
            self.departurePoint.hide()
            self.labelArrivalPoint.hide()
            self.arrivalPoint.hide()
            self.labelDepartureDate.hide()
            self.departureDate.hide()
            self.labelDepartureTime.hide()
            self.departureTimeLowLimit.hide()
            self.labelArrivalTime.show()
            self.arrivalTimeLowLimit.show()
            self.labelDepartureTime2.hide()
            self.departureTimeHighLimit.hide()
            self.arrivalTimeHighLimit.show()
            self.labelArrivalTime2.show()
            self.labelTravelTime.hide()
            self.travelTimeLowLimit.hide()
            self.travelTimeHighLimit.hide()
            self.labelTravelTime2.hide()
            self.labelCountOfDatsLowLimit.hide()
            self.labelCountOfDatsHighLimit.hide()
            self.countOfDaysLowLimit.hide()
            self.countOfDaysHighLimit.hide()
        elif index == 7:
            self.labelCode.hide()
            self.inputCodeOfTrain.hide()
            self.labelDeparturePoint.hide()
            self.departurePoint.hide()
            self.labelArrivalPoint.hide()
            self.arrivalPoint.hide()
            self.labelDepartureDate.hide()
            self.departureDate.hide()
            self.labelDepartureTime.hide()
            self.departureTimeLowLimit.hide()
            self.labelArrivalTime.hide()
            self.arrivalTimeLowLimit.hide()
            self.labelDepartureTime2.hide()
            self.departureTimeHighLimit.hide()
            self.arrivalTimeHighLimit.hide()
            self.labelArrivalTime2.hide()
            self.labelTravelTime.show()
            self.travelTimeLowLimit.show()
            self.travelTimeHighLimit.show()
            self.labelTravelTime2.show()
            self.labelCountOfDatsLowLimit.show()
            self.labelCountOfDatsHighLimit.show()
            self.countOfDaysLowLimit.show()
            self.countOfDaysHighLimit.show()
        else:
            self.labelCode.hide()
            self.inputCodeOfTrain.hide()
            self.labelDeparturePoint.hide()
            self.departurePoint.hide()
            self.labelArrivalPoint.hide()
            self.arrivalPoint.hide()
            self.labelDepartureDate.hide()
            self.departureDate.hide()
            self.labelDepartureTime.hide()
            self.departureTimeLowLimit.hide()
            self.labelArrivalTime.hide()
            self.arrivalTimeLowLimit.hide()
            self.labelDepartureTime2.hide()
            self.departureTimeHighLimit.hide()
            self.arrivalTimeHighLimit.hide()
            self.labelArrivalTime2.hide()
            self.labelTravelTime.hide()
            self.travelTimeLowLimit.hide()
            self.travelTimeHighLimit.hide()
            self.labelTravelTime2.hide()
            self.labelCountOfDatsLowLimit.hide()
            self.labelCountOfDatsHighLimit.hide()
            self.countOfDaysLowLimit.hide()
            self.countOfDaysHighLimit.hide()
