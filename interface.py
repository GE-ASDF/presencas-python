from presencas import *
import pyautogui as p
from connection import connection

alert = "font-size:16px;position: relative; padding: 0.75rem 1.25rem; margin-bottom: 1rem; border: 1px solid transparent;border-radius: 0.25rem;"
alertPrimary = alert+"color: #004085; background-color: #cce5ff; border-color: #b8daff;"
alertSuccess = alert+"color: #155724;background-color: #d4edda;border-color: #c3e6cb;"
alertDanger = alert+"color: #721c24; background-color: #f8d7da; border-color: #f5c6cb;"

   

def verificarUsuario(CodigoContrato):
    import requests as r
    import json
    db = connection(host='localhost', user="prepara2", password="prepara", database="ouromoderno")
    user = db.selectUserOuro(CodigoContrato)
    if user: 
        return user
    else:
        user = r.get("http://192.168.1.11/presencas/controllers/ApiController.php?CodigoContrato="+CodigoContrato)
        return json.loads(user.content)

def marcarPresenca():
    lista = [
            ui.oito.text() if ui.oito.isChecked() else None,
            ui.nove.text() if ui.nove.isChecked() else None,
            ui.dez.text() if ui.dez.isChecked() else None,
            ui.onze.text() if ui.onze.isChecked() else None,
            ui.doze.text() if ui.doze.isChecked() else None,
            ui.treze.text() if ui.treze.isChecked() else None,
            ui.catorze.text() if ui.catorze.isChecked() else None,
            ui.quinze.text() if ui.quinze.isChecked() else None,
            ui.dezesseis.text() if ui.dezesseis.isChecked() else None,
            ui.dezessete.text() if ui.dezessete.isChecked() else None,
            ui.dezoito.text() if ui.dezoito.isChecked() else None,
            ui.dezenove.text() if ui.dezenove.isChecked() else None,
        ]
    HoraPresenca = []
    for i in lista:
        if i != None:
            HoraPresenca.append(i)

    ui.fechar_alert.setStyleSheet("color: #fff; background-color: #dc3545;border-color: #dc3545;display: inline-block;font-weight: 400;text-align: center;white-space: nowrap;vertical-align: middle;border: 1px solid transparent;padding: 6px 12px;font-size: 16px;line-height: 1.5;border-radius: 4px;")
    ui.fechar_alert.raise_()
    ui.fechar_alert.setEnabled(True)
    ui.fechar_alert.setText("X")
    alert = ui.alert
    alert.setText("Aguarde...")
    alert.setStyleSheet(alertPrimary)
    alert.raise_
    i = 0
    
    CodigoContrato = ui.CodigoContrato.text()

    if CodigoContrato and len(HoraPresenca) >= 1:
        user = verificarUsuario(CodigoContrato)

        try:
            alert.setText(user['message'])
            alert.setStyleSheet(alertDanger)
        except:
            print(user)
    else:
        alert.setText("Não foi possível validar os dados, pois o usuário não foi informado.")
        alert.setStyleSheet(alertDanger)

def fecharAlert():
    ui.alert.setStyleSheet('')
    ui.fechar_alert.setStyleSheet('border:none')
    ui.fechar_alert.setEnabled(False)
    ui.alert.clear()
    ui.fechar_alert.setText('')

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_widget()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.registrar.clicked.connect(marcarPresenca)
    ui.fechar_alert.clicked.connect(fecharAlert)

    sys.exit(app.exec_())
