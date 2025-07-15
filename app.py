import sys
from PySide6.QtWidgets import QApplication
from overlay import Overlay

if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = Overlay()
    overlay.resize(400, 400)
    overlay.show()
    sys.exit(app.exec())
