#Contains 2 main tabs, Tool Combinations, List of applications
#List of applications tab: Lists directories and files of the system, Search functionality for searching specific applications, 
#Tool Combinations tab: Holds of selected tools and settings of them
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QListWidget, QFileDialog, QPushButton

class DesktopApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desktop Application")

        layout = QVBoxLayout()

        # Left Panel with Tabs
        left_panel = QWidget()

        tab_widget = QTabWidget()

        # First Tab - List of Applications
        tab1 = QWidget()
        tab1_layout = QVBoxLayout()

        app_list_label = QListWidget()  # Use QListWidget for listing directories and files

        def populate_files_and_folders():
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            selected_files = QFileDialog.getOpenFileNames(None, 'Select Files and Folders', '', 'All Files (*)')[0]
            if selected_files:
                app_list_label.addItems(selected_files)

        list_button = QPushButton("Select Files and Folders")
        list_button.clicked.connect(populate_files_and_folders)

        tab1_layout.addWidget(list_button)
        tab1_layout.addWidget(app_list_label)
        tab1.setLayout(tab1_layout)
        tab_widget.addTab(tab1, "List of Applications")

        left_panel.setLayout(layout)
        layout.addWidget(tab_widget)

        self.setCentralWidget(left_panel)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = DesktopApp()
    myApp.show()
    sys.exit(app.exec_())
