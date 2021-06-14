import sys
from PyQt5.QtWidgets import QGridLayout, QGroupBox, QLabel, QSlider, QPushButton, QHBoxLayout, QApplication, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Figurecanvas

class Window(QWidget):
    def __init__(self):
        super().__init__()

    def init_ui(self):
        #visual box for the buttons and the graph
        grid_box = QGridLayout()
        grid_box.addWidget(self.create_grp_coeff())
        self.canvas = Figurecanvas(plt.Figure(figsize = (15,6)))
        grid_box.addWidget(self.canvas)
        self.insert_plot()
        
        self.setLayout(grid_box)
        self.setWindowTitle("Hermite Curve")
        self.show()

        #defining all the sliders and their properties
    def grp_1(self):
        #slider 1 --->
        self.s1 = QSlider(Qt.Horizontal)
        self.s1.setMinimum(-250)
        self.s1.setMaximum(250)
        self.s1.setValue(0)
        self.s1.setTickInterval(25)
        self.s1.setTickPosition(QSlider.TicksBelow)
        self.s1.valueChanged.connect(self.update_label_1)

        self.label1 = QLabel('0', self)
        self.label1.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label1.setMinimumWidth(80)

        self.s1.valueChanged.connect(self.update_plot)

        grp_box_1 =QGroupBox("&Point 1 (P1)")
        grp_box_1.setAlignment(Qt.AlignHCenter)
        h_box_1 = QVBoxLayout()
        h_box_1.addWidget(self.s1)

        grp_label_1 = QGroupBox()
        H_box_label_1 = QVBoxLayout()
        H_box_label_1.addWidget(self.label1)

        grp_label_1.setLayout(H_box_label_1)
        grp_box_1.setLayout(h_box_1)
        h_box_1.addWidget(grp_label_1)
        return grp_box_1


    def grp_2(self):
        #slider 2
        self.s2 = QSlider(Qt.Horizontal)
        self.s2.setMinimum(-250)
        self.s2.setMaximum(250)
        self.s2.setValue(0)
        self.s2.setTickInterval(25)
        self.s2.setTickPosition(QSlider.TicksBelow)
        self.s2.valueChanged.connect(self.update_label_2)

        self.label2 = QLabel('0', self)
        self.label2.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label2.setMinimumWidth(80)

        self.s2.valueChanged.connect(self.update_plot)

        grp_box_2 = QGroupBox("&Point 2 (P2)")
        grp_box_2.setAlignment(Qt.AlignHCenter)
        h_box_2 = QVBoxLayout()
        h_box_2.addWidget(self.s2)

        grp_label_2 = QGroupBox()
        H_box_label_2 = QVBoxLayout()
        H_box_label_2.addWidget(self.label2)

        grp_label_2.setLayout(H_box_label_2)
        grp_box_2.setLayout(h_box_2)
        h_box_2.addWidget(grp_label_2)
        return grp_box_2

    def grp_3(self):
        #slider 3
        self.s3 = QSlider(Qt.Horizontal)
        self.s3.setMinimum(-2000)
        self.s3.setMaximum(2000)
        self.s3.setValue(0)
        self.s3.setTickInterval(200)
        self.s3.setTickPosition(QSlider.TicksBelow)
        self.s3.valueChanged.connect(self.update_label_3)

        self.label3 = QLabel('0', self)
        self.label3.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label3.setMinimumWidth(80)

        self.s3.valueChanged.connect(self.update_plot)

        grp_box_3 = QGroupBox("&Tanget 1 (R1)")
        grp_box_3.setAlignment(Qt.AlignHCenter)
        h_box_3 = QVBoxLayout()
        h_box_3.addWidget(self.s3)

        grp_label_3 = QGroupBox()
        H_box_label_3 = QVBoxLayout()
        H_box_label_3.addWidget(self.label3)

        grp_label_3.setLayout(H_box_label_3)
        grp_box_3.setLayout(h_box_3)
        h_box_3.addWidget(grp_label_3)
        return grp_box_3

    def grp_4(self):
        #slider 4
        self.s4 = QSlider(Qt.Horizontal)
        self.s4.setMinimum(-2000)
        self.s4.setMaximum(2000)
        self.s4.setValue(0)
        self.s4.setTickInterval(200)
        self.s4.setTickPosition(QSlider.TicksBelow)
        self.s4.valueChanged.connect(self.update_label_4)

        self.label4 = QLabel('0', self)
        self.label4.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label4.setMinimumWidth(80)

        self.s4.valueChanged.connect(self.update_plot)

        grp_box_4 = QGroupBox('&Tanget 2 (R2)')
        grp_box_4.setAlignment(Qt.AlignHCenter)
        h_box_4 = QVBoxLayout()
        h_box_4.addWidget(self.s4)

        grp_label_4 = QGroupBox()
        H_box_label_4 = QVBoxLayout()
        H_box_label_4.addWidget(self.label4)

        grp_label_4.setLayout(H_box_label_4)
        grp_box_4.setLayout(h_box_4)
        h_box_4.addWidget(grp_label_4)
        return grp_box_4

    #updating values for the text
    def update_label_1(self, value):
        self.label1.setText(str(value))

    def update_label_2(self, value):
        self.label2.setText(str(value))

    def update_label_3(self, value):
        self.label3.setText(str(value))

    def update_label_4(self, value):
        self.label4.setText(str(value))

    def create_grp_coeff(self):
        group_box = QGroupBox("&Parameters of the Curve")
        group_box.setAlignment(Qt.AlignHCenter)
        H_box = QHBoxLayout()
        H_box.setAlignment(Qt.AlignCenter)
        H_box.addWidget(self.grp_1())
        H_box.addWidget(self.grp_2())
        H_box.addWidget(self.grp_3())
        H_box.addWidget(self.grp_4())
        H_box.addStretch()
        group_box.setLayout(H_box)
        return group_box 

    def insert_plot(self):
        self.ax = self.canvas.figure.subplots()
        self.ax.set_xlim([0,1])
        self.ax.set_ylim([-500,500])
        self.ax.set_title("Hermite Curve")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("H(t)")
        self.graph = None

    def update_plot(self):
        
        p1 = self.s1.value()
        p2 = self.s2.value()
        t = np.loadtxt('data.csv', delimiter=',')
        r1 = self.s3.value()
        r2 = self.s4.value()

        s = (2*(t**3) - 3*(t**2) + 1)*p1 + (-2*(t**3) + 3*(t**2))*p2 + (t**3 - 2*(t**2) + t)*r1 + (t**3 - t**2)*r2

        try:
            p1 = int(p1)
        except ValueError:
            p1 = 0

        try:
            p2 = int(p2)
        except ValueError:
            p2 = 0

        try:
            r1 = int(r1)
        except ValueError:
            r1 = 0

        try:
            r2 = int(r2)
        except ValueError:
            r2 = 0

        if self.graph:
           self.graph.remove()

        self.graph = self.ax.scatter(t,s)
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    a_window = Window()
    a_window.init_ui()
    sys.exit(app.exec_())
