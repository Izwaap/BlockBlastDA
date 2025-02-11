from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Block Blast")
        self.setGeometry(100, 100, 1024, 768)

        # Создание экземпляра QWebEngineView
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://block-blast-three.vercel.app/"))
        self.setCentralWidget(self.browser)

        # Настройка профиля для браузера
        profile = QWebEngineProfile.defaultProfile()
        profile.setRequestInterceptor(None)  # Отключение перехватчика запросов

        self.browser.show()

if __name__ == "__main__":
    app = QApplication([])
    window = Browser()
    window.show()
    app.exec_()