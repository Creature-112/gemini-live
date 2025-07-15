import sys
import asyncio
import threading
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, Slot, QTimer
from PySide6.QtGui import QColor

from gemini import AudioLoop

class Overlay(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.button = QPushButton(self)
        self.button.setText("...")
        self.button.setFixedSize(100, 100)
        self.button.setStyleSheet("""
            QPushButton {
                border: 2px solid #555;
                border-radius: 50px;
                background-color: #333;
                color: white;
                font-size: 24px;
            }
            QPushButton:hover {
                background-color: #444;
            }
            QPushButton:pressed {
                background-color: #555;
            }
        """)
        self.button.setCheckable(True)

        self.label = QLabel(self)
        self.label.setText("Hello, I'm Gemini!")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("""
            QLabel {
                background-color: rgba(0, 0, 0, 0.7);
                color: white;
                font-size: 18px;
                padding: 10px;
                border-radius: 5px;
            }
        """)
        self.label.adjustSize()
        self.label.hide()

        self.animation = QPropertyAnimation(self.label, b"opacity")
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)

        self.button.clicked.connect(self.toggle_streaming)

        self.streaming = False
        self.audio_loop = None
        self.asyncio_thread = None

        self.hide_timer = QTimer(self)
        self.hide_timer.setSingleShot(True)
        self.hide_timer.timeout.connect(self.hide_label)

    def toggle_streaming(self):
        if not self.streaming:
            self.start_streaming()
        else:
            self.stop_streaming()

    def start_streaming(self):
        self.streaming = True
        self.button.setChecked(True)
        self.button.setStyleSheet("""
            QPushButton {
                border: 2px solid #0f0;
                border-radius: 50px;
                background-color: #333;
                color: white;
                font-size: 24px;
            }
            QPushButton:hover {
                background-color: #444;
            }
            QPushButton:pressed {
                background-color: #555;
            }
        """)
        self.audio_loop = AudioLoop()
        self.audio_loop.new_text.connect(self.update_label)
        self.asyncio_thread = threading.Thread(target=self.run_asyncio_loop)
        self.asyncio_thread.start()

    def stop_streaming(self):
        self.streaming = False
        self.button.setChecked(False)
        self.button.setStyleSheet("""
            QPushButton {
                border: 2px solid #555;
                border-radius: 50px;
                background-color: #333;
                color: white;
                font-size: 24px;
            }
            QPushButton:hover {
                background-color: #444;
            }
            QPushButton:pressed {
                background-color: #555;
            }
        """)
        if self.asyncio_thread:
            asyncio.run_coroutine_threadsafe(self.audio_loop.session.close(), self.loop)
            self.asyncio_thread.join()
            self.asyncio_thread = None

    def run_asyncio_loop(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self.audio_loop.run())

    @Slot(str)
    def update_label(self, text):
        self.label.setText(text)
        self.label.adjustSize()
        self.show_label()
        self.hide_timer.start(5000)  # Hide after 5 seconds

    def show_label(self):
        self.label.show()
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.start()

    def hide_label(self):
        self.animation.setStartValue(1.0)
        self.animation.setEndValue(0.0)
        self.animation.finished.connect(self.label.hide)
        self.animation.start()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            delta = event.globalPos() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.button.move(
            (self.width() - self.button.width()) // 2,
            (self.height() - self.button.height()) // 2
        )
        self.label.move(
            (self.width() - self.label.width()) // 2,
            self.button.y() - self.label.height() - 10
        )
