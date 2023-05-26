# Created by: PyQt6 UI code generator 6.5.0
# To extract .ui file to .py run this command
# python3 -m PyQt6.uic.pyuic -o output.py -x input.ui

# @author: Alperen Senyigit

from PyQt6 import QtCore, QtGui, QtWidgets
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import sys
import openpyxl
import pickle


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(900, 600)
        Widget.setMinimumSize(QtCore.QSize(900, 600))
        Widget.setMaximumSize(QtCore.QSize(900, 600))
        Widget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        Widget.setAutoFillBackground(False)
        Widget.setStyleSheet("")
        self.Header = QtWidgets.QLabel(parent=Widget)
        self.Header.setGeometry(QtCore.QRect(360, 10, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.Header.setFont(font)
        self.Header.setObjectName("Header")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 120, 191, 82))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layoutForIncome = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layoutForIncome.setContentsMargins(0, 0, 0, 0)
        self.layoutForIncome.setObjectName("layoutForIncome")
        self.Income_Label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.Income_Label.setObjectName("Income_Label")
        self.layoutForIncome.addWidget(self.Income_Label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Income_LineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.Income_LineEdit.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Income_LineEdit.setText("")
        self.Income_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Income_LineEdit.setObjectName("Income_LineEdit")
        self.layoutForIncome.addWidget(self.Income_LineEdit, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Income_Pushbutton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.Income_Pushbutton.setObjectName("Income_Pushbutton")
        self.layoutForIncome.addWidget(self.Income_Pushbutton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=Widget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(270, 120, 191, 82))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.layoutForExpense = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.layoutForExpense.setContentsMargins(0, 0, 0, 0)
        self.layoutForExpense.setObjectName("layoutForExpense")
        self.Expense_Label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.Expense_Label.setObjectName("Expense_Label")
        self.layoutForExpense.addWidget(self.Expense_Label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Expense_LineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.Expense_LineEdit.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Expense_LineEdit.setText("")
        self.Expense_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Expense_LineEdit.setObjectName("Expense_LineEdit")
        self.layoutForExpense.addWidget(self.Expense_LineEdit, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Salary_Pushbutton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.Salary_Pushbutton.setObjectName("Salary_Pushbutton")
        self.layoutForExpense.addWidget(self.Salary_Pushbutton)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=Widget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(50, 230, 191, 82))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.layoutForFindex = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.layoutForFindex.setContentsMargins(0, 0, 0, 0)
        self.layoutForFindex.setObjectName("layoutForFindex")
        self.Findex_Label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.Findex_Label.setObjectName("Findex_Label")
        self.layoutForFindex.addWidget(self.Findex_Label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Findex_LineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_3)
        self.Findex_LineEdit.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Findex_LineEdit.setText("")
        self.Findex_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Findex_LineEdit.setObjectName("Findex_LineEdit")
        self.layoutForFindex.addWidget(self.Findex_LineEdit, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Findex_PushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.Findex_PushButton.setObjectName("Findex_PushButton")
        self.layoutForFindex.addWidget(self.Findex_PushButton)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(parent=Widget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(270, 230, 191, 82))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.layoutForLoan = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.layoutForLoan.setContentsMargins(0, 0, 0, 0)
        self.layoutForLoan.setObjectName("layoutForLoan")
        self.LoanAmount_Label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_4)
        self.LoanAmount_Label.setObjectName("LoanAmount_Label")
        self.layoutForLoan.addWidget(self.LoanAmount_Label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.LoanAmount_LineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_4)
        self.LoanAmount_LineEdit.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.LoanAmount_LineEdit.setText("")
        self.LoanAmount_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LoanAmount_LineEdit.setObjectName("LoanAmount_LineEdit")
        self.layoutForLoan.addWidget(self.LoanAmount_LineEdit, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.LoanAmount_Pushbutton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_4)
        self.LoanAmount_Pushbutton.setObjectName("LoanAmount_Pushbutton")
        self.layoutForLoan.addWidget(self.LoanAmount_Pushbutton)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 380, 291, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_Result = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_Result.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_Result.setObjectName("gridLayout_Result")
        self.Result_Pushbutton_Decline = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.Result_Pushbutton_Decline.setAutoFillBackground(False)
        self.Result_Pushbutton_Decline.setStyleSheet("")
        self.Result_Pushbutton_Decline.setObjectName("Result_Pushbutton_Decline")
        self.gridLayout_Result.addWidget(self.Result_Pushbutton_Decline, 2, 1, 1, 1)
        self.Result_hesaplama_LineEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.Result_hesaplama_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Result_hesaplama_LineEdit.setReadOnly(True)
        self.Result_hesaplama_LineEdit.setObjectName("Result_hesaplama_LineEdit")
        self.gridLayout_Result.addWidget(self.Result_hesaplama_LineEdit, 1, 0, 1, 2)
        self.Result_Pushbutton_Accept = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.Result_Pushbutton_Accept.setAutoFillBackground(False)
        self.Result_Pushbutton_Accept.setStyleSheet("")
        self.Result_Pushbutton_Accept.setObjectName("Result_Pushbutton_Accept")
        self.gridLayout_Result.addWidget(self.Result_Pushbutton_Accept, 2, 0, 1, 1)
        self.Result_Label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.Result_Label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Result_Label.setObjectName("Result_Label")
        self.gridLayout_Result.addWidget(self.Result_Label, 0, 0, 1, 2)
        self.formLayoutWidget = QtWidgets.QWidget(parent=Widget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(490, 70, 369, 461))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.HowtoUseLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.HowtoUseLayout.setContentsMargins(0, 0, 0, 0)
        self.HowtoUseLayout.setObjectName("HowtoUseLayout")
        self.textEdit = QtWidgets.QTextEdit(parent=self.formLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.HowtoUseLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.textEdit)
        self.calculateCreditRisk_pushButton = QtWidgets.QPushButton(parent=Widget)
        self.calculateCreditRisk_pushButton.setGeometry(QtCore.QRect(180, 350, 151, 32))
        self.calculateCreditRisk_pushButton.setObjectName("calculateCreditRisk_pushButton")
        self.predictCreditAmount_pushButton = QtWidgets.QPushButton(parent=Widget)
        self.predictCreditAmount_pushButton.setGeometry(QtCore.QRect(180, 315, 151, 32))
        self.predictCreditAmount_pushButton.setObjectName("predictCreditAmount_pushButton")
        self.ResultBottom_lineEdit = QtWidgets.QLineEdit(parent=Widget)
        self.ResultBottom_lineEdit.setGeometry(QtCore.QRect(110, 480, 291, 51))
        self.ResultBottom_lineEdit.setReadOnly(True)
        self.ResultBottom_lineEdit.setObjectName("ResultBottom_lineEdit")

        # ---------------------------- DO NOT EDIT ----------------------
        #self.submitIncome()
        self.submitFindex()
        self.submitLoanAmount()
        self.submitExpense()
        self.Income_Pushbutton.clicked.connect(self.submitIncome)
        self.Findex_PushButton.clicked.connect(self.submitFindex)
        self.Salary_Pushbutton.clicked.connect(self.submitExpense)
        self.LoanAmount_Pushbutton.clicked.connect(self.submitLoanAmount)
        self.calculateCreditRisk_pushButton.clicked.connect(self.calculateFuzzyLogic)
        self.Result_Pushbutton_Accept.clicked.connect(self.resultingButtonForAccept)
        self.Result_Pushbutton_Decline.clicked.connect(self.resultingButtonForDecline)
        self.predictCreditAmount_pushButton.clicked.connect(self.predictLoanAmount)

        # ---------------------------- DO NOT EDIT ----------------------

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)


    # ---------------------------- BUTTONS START ----------------------
    def submitIncome(self):
        try:
            self.income_input = self.Income_LineEdit.text()
            if self.income_input:
                print("Income input: ",self.income_input)
        except ValueError as ve:
             self.textEdit.setHtml("Login information is missing. Don't forget to save the values after typing" + str(ve.args))

    def submitExpense(self):
            try:
                self.expense_input = self.Expense_LineEdit.text()
                if self.expense_input:
                    print("Expense input : ", self.expense_input)
            except ValueError as ve:
                self.textEdit.setHtml("Login information is missing. Don't forget to save the values after typing" + str(ve.args))
    def submitLoanAmount(self):
            try:
                self.LoanAmount_input = self.LoanAmount_LineEdit.text()
                if self.LoanAmount_input:
                    print("Loan Amount : ", self.LoanAmount_input)
            except ValueError as ve:
                self.textEdit.setHtml("Login information is missing. Don't forget to save the values after typing" + str(ve.args))        
    def submitFindex(self):
        try:
            self.Findex_input = self.Findex_LineEdit.text()
            if self.Findex_input:
                print("Findex Input :",  self.Findex_input)
        except ValueError as ve:
            self.textEdit.setHtml("Login information is missing. Don't forget to save the values after typing" + str(ve.args))
    
    def resultingButtonForAccept(self):
         if not (self.Result_hesaplama_LineEdit.text() is None or ''): # does not work properly.
            self.ResultBottom_lineEdit.setText("Your loan has been accepted! Amount:" + str(self.LoanAmount_input))
            self.textEdit.setHtml("HAVE A GOOD DAYS")
    def resultingButtonForDecline(self):
         self.ResultBottom_lineEdit.setText("Your loan has been declined!")
         self.textEdit.setHtml("HAVE A GOOD DAYS")

    def predictLoanAmount(self):
        try:
            with open('model-v1.pkl', 'rb') as file:
                self.model = pickle.load(file)

            self.INPUT_INCOME = int(self.income_input)
            self.INPUT_EXPENSE = int(self.expense_input)
            self.INPUT_FINDEX = int(self.Findex_input)
            input_data = [[self.INPUT_INCOME, self.INPUT_EXPENSE, self.INPUT_FINDEX]]
            loan_amount_prediction = self.model.predict(input_data)

            print("Kredi Tahmini: ", loan_amount_prediction[0])
            self.ResultBottom_lineEdit.setText("Suggested Amount: " + str(loan_amount_prediction[0]))
        except ValueError as ve:
            self.textEdit.setHtml("Your model file could not be loaded. Contact system administrator" + str(ve.args))


    # ---------------------------- BUTTONS END ---------------------- 


    ## ---------------------------- Save Excel Start ---------------------- 
    def save_to_excel(self,income, expense, findex, loan_amount):
        try:
            workbook = openpyxl.load_workbook("userDatas.xlsx")
            sheet = workbook.active
        except FileNotFoundError:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.append(["Income", "Expense", "Findex", "LoanAmount"])

        sheet.append([int(income), int(expense), int(findex), int(loan_amount)])
        workbook.save("userDatas.xlsx")
        print("Data has been saved succesfully")

    ## ---------------------------- Save Excel End ----------------------
  
    def calculateFuzzyLogic(self):
        try:
             
            self.Income = ctrl.Antecedent(np.arange(0, 10001, 1),'income')
            self.Expense = ctrl.Antecedent(np.arange(0, 5001, 1),'expense')
            self.LoanAmount = ctrl.Antecedent(np.arange(0, 1000001, 1),'loanAmount')
            self.Findex = ctrl.Antecedent(np.arange(0, 101, 1),'findex')
            
            # Definiton of output variable
            self.creditConfirmation = ctrl.Consequent(np.arange(0, 101, 1),'creditConfirmation')
            
            #Membership Functions
            self.Income['low'] = fuzz.trimf(self.Income.universe, [0, 0, 5000])
            self.Income['avarage'] = fuzz.trimf(self.Income.universe, [1500, 5000, 7000])
            self.Income['high'] = fuzz.trimf(self.Income.universe, [5000, 7000, 10000])

            self.Expense['low'] = fuzz.trimf(self.Expense.universe, [0, 0, 2500])
            self.Expense['avarage'] = fuzz.trimf(self.Expense.universe, [1500, 2500, 3500])
            self.Expense['high'] = fuzz.trimf(self.Expense.universe, [2500, 5000, 5000])

            self.LoanAmount['low'] = fuzz.trimf(self.LoanAmount.universe, [0, 0, 50000])
            self.LoanAmount['avarage'] = fuzz.trimf(self.LoanAmount.universe, [30000, 50000, 70000])
            self.LoanAmount['high'] = fuzz.trimf(self.LoanAmount.universe, [50000, 100000, 100000])

            self.Findex['low'] = fuzz.trimf(self.Findex.universe, [0, 0, 50])
            self.Findex['avarage'] = fuzz.trimf(self.Findex.universe, [30, 50, 70])
            self.Findex['high'] = fuzz.trimf(self.Findex.universe, [50, 100, 100])

            # Define membership function to output variable
            self.creditConfirmation['low'] = fuzz.trimf(self.creditConfirmation.universe, [0, 0, 50])
            self.creditConfirmation['avarage'] = fuzz.trimf(self.creditConfirmation.universe, [30, 50, 70])
            self.creditConfirmation['high'] = fuzz.trimf(self.creditConfirmation.universe, [50, 100, 100])
            
            # Rule Definition
            self.rule_1 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['high'], self.creditConfirmation['high'])  # High income, low expense, high loan amount, high financial index -> High credit confirmation
            self.rule_2 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # High income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_3 = ctrl.Rule(self.Income['high'] & self.Expense['high'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['high'])  # High income, high expense, low loan amount, high financial index -> High credit confirmation
            self.rule_4 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['low'], self.creditConfirmation['high'])  # High income, low expense, high loan amount, low financial index -> High credit confirmation
            self.rule_5 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['avarage'])  # High income, low expense, low loan amount, high financial index -> avarage credit confirmation
            self.rule_6 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # High income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_7 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['high'], self.creditConfirmation['high'])  # High income, low expense, high loan amount, high financial index -> High credit confirmation
            self.rule_8 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # High income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_9 = ctrl.Rule(self.Income['high'] & self.Expense['high'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['high'])  # High income, high expense, low loan amount, high financial index -> High credit confirmation
            self.rule_10 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['low'], self.creditConfirmation['high'])  # High income, low expense, high loan amount, low financial index -> High credit confirmation
            self.rule_11 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['avarage'])  # High income, low expense, low loan amount, high financial index -> avarage credit confirmation
            self.rule_12 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # High income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_13 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['high'], self.creditConfirmation['high'])  # High income, low expense, high loan amount, high financial index -> High credit confirmation
            self.rule_14 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # High income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_15 = ctrl.Rule(self.Income['high'] & self.Expense['high'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['high'])  # High income, high expense, low loan amount, high financial index -> High credit confirmation
            self.rule_16 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['low'], self.creditConfirmation['high'])  # High income, low expense, high loan amount, low financial index -> High credit confirmation
            self.rule_17 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['avarage'])  # High income, low expense, low loan amount, high financial index -> avarage credit confirmation
            self.rule_18 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # High income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_19 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['high'], self.creditConfirmation['high'])  # High income, low expense, high loan amount, high financial index -> High credit confirmation
            self.rule_20 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # High income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_21 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['high'], self.creditConfirmation['avarage'])  # High income, low expense, high loan amount, high financial index -> avarage credit confirmation
            self.rule_22 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # High income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_23 = ctrl.Rule(self.Income['high'] & self.Expense['high'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['high'])  # High income, high expense, low loan amount, high financial index -> High credit confirmation
            self.rule_24 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['low'], self.creditConfirmation['high'])  # High income, low expense, high loan amount, low financial index -> High credit confirmation
            self.rule_25 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['avarage'])  # High income, low expense, low loan amount, high financial index -> avarage credit confirmation
            self.rule_26 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # High income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_27 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['high'], self.creditConfirmation['high'])  # High income, low expense, high loan amount, high financial index -> High credit confirmation
            self.rule_28 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # High income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_29 = ctrl.Rule(self.Income['high'] & self.Expense['high'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['high'])  # High income, high expense, low loan amount, high financial index -> High credit confirmation
            self.rule_30 = ctrl.Rule(self.Income['high'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['low'], self.creditConfirmation['high'])  # High income, low expense, high loan amount, low financial index -> High credit confirmation
            self.rule_31 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['high'], self.creditConfirmation['high'])  # avarage income, low expense, high loan amount, high financial index -> High credit confirmation
            self.rule_32 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # avarage income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_33 = ctrl.Rule(self.Income['avarage'] & self.Expense['high'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['high'])  # avarage income, high expense, low loan amount, high financial index -> High credit confirmation
            self.rule_34 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['low'], self.creditConfirmation['high'])  # avarage income, low expense, high loan amount, low financial index -> High credit confirmation
            self.rule_35 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['avarage'])  # avarage income, low expense, low loan amount, high financial index -> avarage credit confirmation
            self.rule_36 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # avarage income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_37 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['high'], self.creditConfirmation['high'])  # avarage income, low expense, high loan amount, high financial index -> High credit confirmation
            self.rule_38 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # avarage income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_39 = ctrl.Rule(self.Income['avarage'] & self.Expense['high'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['high'])  # avarage income, high expense, low loan amount, high financial index -> High credit confirmation
            self.rule_40 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['low'], self.creditConfirmation['high'])  # avarage income, low expense, high loan amount, low financial index -> High credit confirmation
            self.rule_41 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['avarage'])  # avarage income, low expense, low loan amount, high financial index -> avarage credit confirmation
            self.rule_42 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # avarage income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_43 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['high'], self.creditConfirmation['high'])  # avarage income, low expense, high loan amount, high financial index -> High credit confirmation
            self.rule_44 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # avarage income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_45 = ctrl.Rule(self.Income['avarage'] & self.Expense['high'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['high'])  # avarage income, high expense, low loan amount, high financial index -> High credit confirmation
            self.rule_46 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['low'], self.creditConfirmation['high'])  # avarage income, low expense, high loan amount, low financial index -> High credit confirmation
            self.rule_47 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['avarage'])  # avarage income, low expense, low loan amount, high financial index -> avarage credit confirmation
            self.rule_48 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # avarage income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_49 = ctrl.Rule(self.Income['avarage'] & self.Expense['high'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['high'])  # avarage income, high expense, low loan amount, high financial index -> High credit confirmation
            self.rule_50 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['low'], self.creditConfirmation['high'])  # avarage income, low expense, high loan amount, low financial index -> High credit confirmation
            self.rule_51 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['avarage'])  # avarage income, low expense, low loan amount, high financial index -> avarage credit confirmation
            self.rule_52 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # avarage income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_53 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['high'], self.creditConfirmation['high'])  # avarage income, low expense, high loan amount, high financial index -> High credit confirmation
            self.rule_54 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # avarage income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_55 = ctrl.Rule(self.Income['avarage'] & self.Expense['high'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['high'])  # avarage income, high expense, low loan amount, high financial index -> High credit confirmation
            self.rule_56 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['low'], self.creditConfirmation['high'])  # avarage income, low expense, high loan amount, low financial index -> High credit confirmation
            self.rule_57 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['avarage'])  # avarage income, low expense, low loan amount, high financial index -> avarage credit confirmation
            self.rule_58 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # avarage income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_59 = ctrl.Rule(self.Income['avarage'] & self.Expense['high'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['high'])  # avarage income, high expense, low loan amount, high financial index -> High credit confirmation
            self.rule_60 = ctrl.Rule(self.Income['avarage'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['low'], self.creditConfirmation['high'])  # avarage income, low expense, high loan amount, low financial index -> High credit confirmation
            self.rule_61 = ctrl.Rule(self.Income['low'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['high'], self.creditConfirmation['high'])  # Low income, low expense, high loan amount, high financial index -> High credit confirmation
            self.rule_62 = ctrl.Rule(self.Income['low'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # Low income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_63 = ctrl.Rule(self.Income['low'] & self.Expense['high'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['high'])  # Low income, high expense, low loan amount, high financial index -> High credit confirmation
            self.rule_64 = ctrl.Rule(self.Income['low'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['low'], self.creditConfirmation['high'])  # Low income, low expense, high loan amount, low financial index -> High credit confirmation
            self.rule_65 = ctrl.Rule(self.Income['low'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['avarage'])  # Low income, low expense, low loan amount, high financial index -> avarage credit confirmation
            self.rule_66 = ctrl.Rule(self.Income['low'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # Low income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_67 = ctrl.Rule(self.Income['low'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['high'], self.creditConfirmation['high'])  # Low income, low expense, high loan amount, high financial index -> High credit confirmation
            self.rule_68 = ctrl.Rule(self.Income['low'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # Low income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_69 = ctrl.Rule(self.Income['low'] & self.Expense['high'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['high'])  # Low income, high expense, low loan amount, high financial index -> High credit confirmation
            self.rule_70 = ctrl.Rule(self.Income['low'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['low'], self.creditConfirmation['high'])  # Low income, low expense, high loan amount, low financial index -> High credit confirmation
            self.rule_71 = ctrl.Rule(self.Income['low'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['avarage'])  # Low income, low expense, low loan amount, high financial index -> avarage credit confirmation
            self.rule_72 = ctrl.Rule(self.Income['low'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # Low income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_73 = ctrl.Rule(self.Income['low'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['high'], self.creditConfirmation['high'])  # Low income, low expense, high loan amount, high financial index -> High credit confirmation
            self.rule_74 = ctrl.Rule(self.Income['low'] & self.Expense['low'] & self.LoanAmount['low'] & self.Findex['low'], self.creditConfirmation['avarage'])  # Low income, low expense, low loan amount, low financial index -> avarage credit confirmation
            self.rule_75 = ctrl.Rule(self.Income['low'] & self.Expense['high'] & self.LoanAmount['low'] & self.Findex['high'], self.creditConfirmation['high'])  # Low income, high expense, low loan amount, high financial index -> High credit confirmation
            self.rule_76 = ctrl.Rule(self.Income['low'] & self.Expense['low'] & self.LoanAmount['high'] & self.Findex['low'], self.creditConfirmation['low'])  # Low income, low expense, high loan amount, low financial index -> Low credit confirmation
            
            self.creditControl = ctrl.ControlSystem([
                self.rule_1,self.rule_2,self.rule_3,self.rule_4,self.rule_5,self.rule_6,self.rule_7,self.rule_8,self.rule_9,self.rule_10,
                self.rule_11,self.rule_12,self.rule_13,self.rule_14,self.rule_15,self.rule_16,self.rule_17,self.rule_18,self.rule_19,self.rule_20,
                self.rule_21,self.rule_22,self.rule_23,self.rule_24,self.rule_25,self.rule_26,self.rule_27,self.rule_28,self.rule_29,self.rule_30,
                self.rule_31,self.rule_32,self.rule_33,self.rule_34,self.rule_35,self.rule_36,self.rule_37,self.rule_38,self.rule_39,self.rule_40,
                self.rule_41,self.rule_42,self.rule_43,self.rule_44,self.rule_45,self.rule_46,self.rule_47,self.rule_48,self.rule_49,self.rule_50,
                self.rule_51,self.rule_52,self.rule_53,self.rule_54,self.rule_55,self.rule_56,self.rule_57,self.rule_58,self.rule_59,self.rule_60,
                self.rule_61,self.rule_62,self.rule_63,self.rule_64,self.rule_65,self.rule_66,self.rule_67,self.rule_68,self.rule_69,self.rule_70,
                self.rule_71,self.rule_72,self.rule_73,self.rule_74,self.rule_75,self.rule_76
            ])

            

            
            # Generate control system simulation
            self.creditSimulation = ctrl.ControlSystemSimulation(self.creditControl)
            
            # Define input variables
            self.creditSimulation.input['income'] = int(self.income_input)
            self.creditSimulation.input['expense'] = int(self.expense_input)
            self.creditSimulation.input['loanAmount'] = int(self.LoanAmount_input)
            self.creditSimulation.input['findex'] = int(self.Findex_input)

            self.creditSimulation.compute()

            # output algorithm will start here!

            self.creditApprovalValue = self.creditSimulation.output['creditConfirmation'] # <class 'numpy.float64'>
            print("creditConfirmation value : ",self.creditApprovalValue) 
            
            if self.creditApprovalValue >= 40:
                self.Result_hesaplama_LineEdit.setText("Press the Accept button to confirm the loan.")
                self.save_to_excel(self.income_input,self.expense_input,self.Findex_input,self.LoanAmount_input)
            else:
                self.Result_hesaplama_LineEdit.setText("Credit denied.")
        except ValueError as ve:
             ERROR_DESCRIPTION = "SOMETHING WENT WRONG\n Be sure the all fields are correct or full.\n The problem may caused by the rule set does not exist.\n Contact your system administrator " + str(ve.args)
             self.textEdit.setHtml(ERROR_DESCRIPTION)


    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.Header.setText(_translate("Widget", "Credit Risk Analysis"))
        self.Income_Label.setText(_translate("Widget", "Customer Income"))
        self.Income_LineEdit.setToolTip(_translate("Widget", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Income_Pushbutton.setText(_translate("Widget", "Enter"))
        self.Expense_Label.setText(_translate("Widget", "Customer Expense"))
        self.Expense_LineEdit.setToolTip(_translate("Widget", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Salary_Pushbutton.setText(_translate("Widget", "Enter"))
        self.Findex_Label.setText(_translate("Widget", "Customer Findex Score"))
        self.Findex_LineEdit.setToolTip(_translate("Widget", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Findex_PushButton.setText(_translate("Widget", "Enter"))
        self.LoanAmount_Label.setText(_translate("Widget", "Requested Loan Amount"))
        self.LoanAmount_LineEdit.setToolTip(_translate("Widget", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.LoanAmount_Pushbutton.setText(_translate("Widget", "Enter"))
        self.Result_Pushbutton_Decline.setText(_translate("Widget", "Decline"))
        self.Result_Pushbutton_Accept.setText(_translate("Widget", "Accept"))
        self.Result_Label.setText(_translate("Widget", "Credit Result "))
        self.predictCreditAmount_pushButton.setText(_translate("Widget", "Suggest Loan Amounts"))
        self.textEdit.setHtml(_translate("Widget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "hr { height: 1px; border-width: 0; }\n"
                                        "li.unchecked::marker { content: \"\\2610\"; }\n"
                                        "li.checked::marker { content: \"\\2612\"; }\n"
                                        "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Computable ranges of values</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Income : between 0 and 10000</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Expense : between 0 and 5000</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Findex : between 0 and 100</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Loan Amount : between 0 and 100000</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The user must enter his inputs in these value ranges.</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Otherwise, it will get an error because it is not in the computable range.</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">All data is stored in a database.</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In long-term use, the lower limit of the credit risk value may change positively or negatively.</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For this reason, take care to enter the correct values.</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Do not exceed the above-mentioned intervals in order to ensure the program flow.</p>\n"


                                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.calculateCreditRisk_pushButton.setText(_translate("Widget", "Calculate Credit Risk"))

    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec())
