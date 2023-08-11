# -> QApplication (app)
#   -> QMainWindow (TaskApp)
#       -> CentralWidget (central_widget)
#           -> Layout (QVBoxLayout)
#               -> Widget 1 (Lista de tarefas)
#               -> Widget 2 (Campo para adicionar novas tarefas)
#               -> Widget 3 (Botão para adicionar tarefas)
#               -> Widget 4 (Botão para remover tarefas selecionadas)
#   -> show
# -> exec

import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QListWidget, QLineEdit, QPushButton, QHBoxLayout, QMessageBox


class TaskApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuração da janela principal
        self.setWindowTitle("Lista de Tarefas")
        # setGeometry(left, top, width, height)
        self.setGeometry(100, 100, 400, 400)

        # Layout principal
        layout = QVBoxLayout()

        # Lista de tarefas
        self.task_list = QListWidget()
        layout.addWidget(self.task_list)

        # Campo para adicionar novas tarefas
        self.new_task_input = QLineEdit()
        layout.addWidget(self.new_task_input)

        # Botão para adicionar tarefas
        add_button = QPushButton("Adicionar Tarefa")
        add_button.clicked.connect(self.add_task)
        layout.addWidget(add_button)

        # Botão para remover tarefas selecionadas
        remove_button = QPushButton("Remover Tarefa")
        remove_button.clicked.connect(self.remove_task)
        layout.addWidget(remove_button)

        # Widget central
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    # Método para adicionar uma nova tarefa à lista
    def add_task(self):
        task_text = self.new_task_input.text()
        if task_text:
            self.task_list.addItem(task_text)
            self.new_task_input.clear()

    # Método para remover a tarefa selecionada da lista
    def remove_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            confirm = QMessageBox.question(self, "Confirmar", "Tem certeza que deseja remover esta tarefa?",
                                           QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                self.task_list.takeItem(self.task_list.row(selected_item))


def main():
    app = QApplication(sys.argv)
    window = TaskApp()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
