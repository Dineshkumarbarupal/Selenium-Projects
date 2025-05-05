import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QFrame
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from qfluentwidgets import PrimaryPushButton
from automate1.automate import WaAutomate

class WorkerThread(QThread):
    finished_signal = pyqtSignal()  # Signal to notify when work is done

    def run(self):
        WaAutomate()  # Background automation
        self.finished_signal.emit()  # Emit signal when done

class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(900, 600)
        self.initui()
        # layout = QVBoxLayout(self)
    def initui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 32, 32, 32)
     
        central_frame = QFrame(self)
        central_frame.setStyleSheet("background-color: white; border-radius: 10px")
        central_frame.setMinimumSize(500, 300)
        central_frame.setMaximumWidth(500)
        
        central_layout = QVBoxLayout(central_frame)

        button = PrimaryPushButton('Start')
        central_layout.addWidget(button, alignment=Qt.AlignCenter)
        layout.addWidget(central_frame, alignment=Qt.AlignCenter)

        button.clicked.connect(self.start_automation)

    def start_automation(self):
        self.thread = WorkerThread()
        self.thread.finished_signal.connect(self.on_finished)
        self.thread.start()  

    def on_finished(self):
        print("Automation complete!")

if __name__ == "__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    
    app = QApplication(sys.argv)
    w = Mainwindow()
    w.show()
    sys.exit(app.exec_())  
