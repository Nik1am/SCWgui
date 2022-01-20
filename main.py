from ctypes.wintypes import MSG
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
fname = ('','')
class SCWGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):

        mode_label = QLabel(self)
        mode_label.setText('Conversion mode:')
        mode_label.move(0,4)

        flags_label = QLabel(self)
        flags_label.setText('Flags:')
        flags_label.move(0,48)


        self.mode = QComboBox(self)
        self.mode.addItems(["scw2dae", "dae2scw"])
        self.mode.move(110,0)


        self.filename_lbl = QLabel(self)
        self.filename_lbl.move(0,24)
        self.filename_lbl.setText('(This will show the path to your model)')
        self.filename_lbl.resize(300, 20)


        convert_btn = QPushButton("Convert",self)
        convert_btn.move(0,200-24)
        convert_btn.clicked.connect(lambda: self.convert(self.mode.currentText(),fname[0]))


        file_dialog_bnt = QPushButton("Select file",self)
        file_dialog_bnt.move(185,0)
        file_dialog_bnt.clicked.connect(self.getfile)


        self.flag_M = QCheckBox('[M]aterials',self)
        self.flag_G = QCheckBox('[G]eometries',self)
        self.flag_A = QCheckBox('[A]nimations',self)
        self.flag_C = QCheckBox('[C]ameras',self)
        
        self.flag_M.move(0,64)
        self.flag_G.move(0,80)
        self.flag_A.move(0,96)
        self.flag_C.move(0,112)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('SCW.jar GUI')
        self.show()



    def getfile(self):
        global fname
        fname = QFileDialog.getOpenFileName(self, 'Open file','.\\',"Model files (*.scw *.dae)")
        self.filename_lbl.setText(fname[0])
        
    def flag_M_check(self):
        if self.flag_M.isChecked() == True:
            return 'M'
        else:
            return ''

    def flag_G_check(self):
        if self.flag_G.isChecked() == True:
            return 'G'
        else:
            return ''

    def flag_A_check(self):
        if self.flag_A.isChecked() == True:
            return 'A'
        else:
            return ''

    def flag_C_check(self):
        if self.flag_C.isChecked() == True:
            return 'C'
        else:
            return ''

    def flag_check(self):
        if self.flag_M.isChecked() or self.flag_G.isChecked() or self.flag_A.isChecked() or self.flag_C.isChecked() == True:
            return '-a'
        else:
            return ''

    def convert(self,mode,file):
        cmd = f'java -jar SCW.jar {mode} {self.flag_check()} {self.flag_M_check()+self.flag_G_check()+self.flag_A_check()+self.flag_C_check()} {file}'
        print(cmd)
        os.system(cmd)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = SCWGUI()
    sys.exit(app.exec_())