import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
                             QFileDialog, QListWidget, QComboBox, QProgressBar, QMessageBox, QMainWindow, 
                             QAction, QTextEdit, QFrame, QStackedWidget, QTabWidget)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import subprocess
import os

class PDFCompressorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.selected_files = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle("LCL PDF Compressor")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('icon.png'))

        # Créer la barre de menu
        self.menuBar = self.menuBar()
        helpMenu = self.menuBar.addMenu('&Aide')
        aboutAction = QAction('À propos', self)
        aboutAction.triggered.connect(self.show_help)
        helpMenu.addAction(aboutAction)

        # Ajouter une barre d'outils
        toolbar = self.addToolBar('MainToolbar')
        toolbar.setMovable(False)

        # Icône et titre
        self.logoLabel = QLabel(self)
        logo = QPixmap("logo_lcl.png")  # Remplacer par le chemin correct
        self.logoLabel.setPixmap(logo.scaled(50, 50, Qt.KeepAspectRatio))
        toolbar.addWidget(self.logoLabel)
        
        self.titleLabel = QLabel("LCL PDF Compressor", self)
        self.titleLabel.setStyleSheet("font-size: 24px; font-weight: bold; margin-left: 20px;")
        toolbar.addWidget(self.titleLabel)

        # Panneau principal
        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)
        mainLayout = QVBoxLayout(mainWidget)

        # Onglets
        tabWidget = QTabWidget()
        mainLayout.addWidget(tabWidget)

        # Onglet Principal
        mainTab = QWidget()
        tabWidget.addTab(mainTab, "Principal")
        mainTabLayout = QVBoxLayout(mainTab)

        # Section de sélection des fichiers
        fileSection = QFrame()
        fileSection.setFrameShape(QFrame.Box)
        fileSection.setFrameShadow(QFrame.Raised)
        fileSectionLayout = QVBoxLayout(fileSection)
        mainTabLayout.addWidget(fileSection)

        fileSelectLayout = QHBoxLayout()
        fileSectionLayout.addLayout(fileSelectLayout)

        self.selectButton = QPushButton("Choisir des PDFs")
        self.selectButton.setIcon(QIcon("select_icon.png"))  # Remplacer par le chemin correct
        self.selectButton.clicked.connect(self.select_files)
        fileSelectLayout.addWidget(self.selectButton)

        self.previewButton = QPushButton("Aperçu des PDFs")
        self.previewButton.setIcon(QIcon("preview_icon.png"))  # Remplacer par le chemin correct
        self.previewButton.clicked.connect(self.preview_files)
        fileSelectLayout.addWidget(self.previewButton)

        self.fileList = QListWidget()
        fileSectionLayout.addWidget(self.fileList)

        # Section des paramètres de compression
        compressSection = QFrame()
        compressSection.setFrameShape(QFrame.Box)
        compressSection.setFrameShadow(QFrame.Raised)
        compressSectionLayout = QVBoxLayout(compressSection)
        mainTabLayout.addWidget(compressSection)

        compressLevelLayout = QHBoxLayout()
        compressSectionLayout.addLayout(compressLevelLayout)

        compressLevelLabel = QLabel("Niveau de Compression:")
        compressLevelLabel.setStyleSheet("font-size: 16px;")
        compressLevelLayout.addWidget(compressLevelLabel)

        self.compressComboBox = QComboBox()
        self.compressComboBox.addItems(['screen', 'ebook', 'printer', 'prepress', 'default'])
        compressLevelLayout.addWidget(self.compressComboBox)

        # Section des options avancées
        advancedSection = QFrame()
        advancedSection.setFrameShape(QFrame.Box)
        advancedSection.setFrameShadow(QFrame.Raised)
        advancedSectionLayout = QHBoxLayout(advancedSection)
        mainTabLayout.addWidget(advancedSection)

        self.splitButton = QPushButton("Diviser PDF")
        self.splitButton.setIcon(QIcon("split_icon.png"))  # Remplacer par le chemin correct
        self.splitButton.clicked.connect(self.split_pdf)
        advancedSectionLayout.addWidget(self.splitButton)

        self.mergeButton = QPushButton("Fusionner PDFs")
        self.mergeButton.setIcon(QIcon("merge_icon.png"))  # Remplacer par le chemin correct
        self.mergeButton.clicked.connect(self.merge_pdfs)
        advancedSectionLayout.addWidget(self.mergeButton)

        # Section de suivi de processus
        processSection = QFrame()
        processSection.setFrameShape(QFrame.Box)
        processSection.setFrameShadow(QFrame.Raised)
        processSectionLayout = QVBoxLayout(processSection)
        mainTabLayout.addWidget(processSection)

        self.progressBar = QProgressBar()
        self.progressBar.setMaximum(100)
        processSectionLayout.addWidget(self.progressBar)

        self.statusLabel = QLabel("Aucune tâche en cours...")
        self.statusLabel.setStyleSheet("font-size: 16px;")
        processSectionLayout.addWidget(self.statusLabel)

        # Section des actions
        actionSection = QFrame()
        actionSection.setFrameShape(QFrame.Box)
        actionSection.setFrameShadow(QFrame.Raised)
        actionSectionLayout = QHBoxLayout(actionSection)
        mainTabLayout.addWidget(actionSection)

        self.resetButton = QPushButton("Réinitialiser")
        self.resetButton.setIcon(QIcon("reset_icon.png"))  # Remplacer par le chemin correct
        self.resetButton.clicked.connect(self.reset_files)
        actionSectionLayout.addWidget(self.resetButton)

        self.compressButton = QPushButton("Compresser")
        self.compressButton.setIcon(QIcon("compress_icon.png"))  # Remplacer par le chemin correct
        self.compressButton.clicked.connect(self.start_compression)
        actionSectionLayout.addWidget(self.compressButton)

        # Onglet d'Aide
        helpTab = QTextEdit()
        helpTab.setReadOnly(True)
        helpTab.setHtml(
            "<h1>Comment Utiliser LCL PDF Compressor</h1>"
            "<ol>"
            "<li>Cliquez sur 'Choisir des PDFs' pour sélectionner les fichiers PDF que vous souhaitez compresser.</li>"
            "<li>Utilisez l'option 'Aperçu des PDFs' pour vérifier les fichiers sélectionnés.</li>"
            "<li>Choisissez le niveau de compression souhaité dans le menu déroulant.</li>"
            "<li>Cliquez sur 'Compresser' pour compresser les fichiers PDF sélectionnés.</li>"
            "<li>Utilisez les options avancées pour diviser ou fusionner des PDF.</li>"
            "<li>Cliquez sur 'Réinitialiser' pour effacer la liste des fichiers sélectionnés.</li>"
            "</ol>"
        )
        tabWidget.addTab(helpTab, "Aide")

    def select_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Choisir des PDFs", "", "PDF Files (*.pdf)")
        if files:
            self.selected_files = files
            self.update_file_list()

    def preview_files(self):
        if not self.selected_files:
            QMessageBox.warning(self, "Warning", "Aucun fichier sélectionné !")
            return
        previewWindow = QMainWindow(self)
        previewWindow.setWindowTitle("Aperçu des PDFs Sélectionnés")
        previewWindow.setGeometry(100, 100, 600, 400)
        fileListWidget = QListWidget(previewWindow)
        fileListWidget.setGeometry(10, 10, 580, 380)
        for file in self.selected_files:
            fileListWidget.addItem(file)
        previewWindow.show()

    def update_file_list(self):
        self.fileList.clear()
        for file in self.selected_files:
            self.fileList.addItem(file)

    def reset_files(self):
        self.selected_files = []
        self.update_file_list()
        self.progressBar.setValue(0)
        self.statusLabel.setText("Aucune tâche en cours...")

    def start_compression(self):
        if not self.selected_files:
            QMessageBox.warning(self, "Warning", "Aucun fichier sélectionné !")
            return
        self.statusLabel.setText("Compression en cours...")
        self.compressThread = CompressThread(self.selected_files, self.compressComboBox.currentText(), self)
        self.compressThread.progress.connect(self.progressBar.setValue)
        self.compressThread.finished.connect(self.compression_finished)
        self.compressThread.start()

    def compression_finished(self, success, output_file):
        if success:
            self.statusLabel.setText(f"Compression terminée avec succès: {output_file}")
            QMessageBox.information(self, "Success", f"Les fichiers ont été compressés avec succès sous {output_file}")
        else:
            self.statusLabel.setText("Erreur lors de la compression")
            QMessageBox.critical(self, "Error", "Une erreur est survenue lors de la compression")

    def split_pdf(self):
        QMessageBox.information(self, "Fonctionnalité à venir", "Cette fonctionnalité n'est pas encore implémentée.")

    def merge_pdfs(self):
        QMessageBox.information(self, "Fonctionnalité à venir", "Cette fonctionnalité n'est pas encore implémentée.")

    def show_help(self):
        helpWindow = QMainWindow(self)
        helpWindow.setWindowTitle("À propos de LCL PDF Compressor")
        helpWindow.setGeometry(100, 100, 600, 400)
        helpTextEdit = QTextEdit(helpWindow)
        helpTextEdit.setReadOnly(True)
        helpTextEdit.setHtml(
            "<h1>Comment Utiliser LCL PDF Compressor</h1>"
            "<ol>"
            "<li>Cliquez sur 'Choisir des PDFs' pour sélectionner les fichiers PDF que vous souhaitez compresser.</li>"
            "<li>Utilisez l'option 'Aperçu des PDFs' pour vérifier les fichiers sélectionnés.</li>"
            "<li>Choisissez le niveau de compression souhaité dans le menu déroulant.</li>"
            "<li>Cliquez sur 'Compresser' pour compresser les fichiers PDF sélectionnés.</li>"
            "<li>Utilisez les options avancées pour diviser ou fusionner des PDF.</li>"
            "<li>Cliquez sur 'Réinitialiser' pour effacer la liste des fichiers sélectionnés.</li>"
            "</ol>"
        )
        helpTextEdit.setGeometry(10, 10, 580, 380)
        helpWindow.show()

class CompressThread(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(bool, str)

    def __init__(self, files, compression_level, parent=None):
        super().__init__(parent)
        self.files = files
        self.compression_level = compression_level

    def run(self):
        output_file_path, _ = QFileDialog.getSaveFileName(None, "Enregistrer le PDF Comprimé sous", "", "PDF Files (*.pdf)")
        if not output_file_path:
            self.finished.emit(False, "")
            return

        gs_path = 'C:\\pypdfcompiler\\ghostscript\\gs\\bin\\gswin64c.exe'
        gs_command = [
            gs_path, '-sDEVICE=pdfwrite', f'-dPDFSETTINGS=/{self.compression_level}', '-dNOPAUSE', '-dBATCH',
            '-sOutputFile=' + output_file_path
        ]
        gs_command.extend(self.files)

        try:
            subprocess.run(gs_command, check=True)
            self.finished.emit(True, output_file_path)
        except subprocess.CalledProcessError as e:
            self.finished.emit(False, "")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFCompressorApp()
    window.show()
    sys.exit(app.exec_())
