# 套件匯入
from PyQt6 import QtWidgets
import sys
import bs4
import requests
# 網頁資料讀取設定
def fetch_rates():
    url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
    res = requests.get(url)
    result = res.text
    htmlfile = bs4.BeautifulSoup(result, 'html.parser')

    # 現金匯率/本行買入
    rates01 = {
        '新台幣(TWD)' : 1,
        '美金(USD)' : float(htmlfile.select_one('tbody tr:nth-of-type(1) td:nth-of-type(2)').text),
        '港幣(HKD)' : float(htmlfile.select_one('tbody tr:nth-of-type(2) td:nth-of-type(2)').text),
        '英鎊(GBP)' : float(htmlfile.select_one('tbody tr:nth-of-type(3) td:nth-of-type(2)').text),
        '澳幣(AUD)' : float(htmlfile.select_one('tbody tr:nth-of-type(4) td:nth-of-type(2)').text),
        '加拿大幣(CAD)':float(htmlfile.select_one('tbody tr:nth-of-type(5) td:nth-of-type(2)').text),
        '新加坡幣(SGD)':float(htmlfile.select_one('tbody tr:nth-of-type(6) td:nth-of-type(2)').text),
        '瑞士法郎(CHF)':float(htmlfile.select_one('tbody tr:nth-of-type(7) td:nth-of-type(2)').text),
        '日圓(JPY)':float(htmlfile.select_one('tbody tr:nth-of-type(8) td:nth-of-type(2)').text),
        '紐元(NZD)':float(htmlfile.select_one('tbody tr:nth-of-type(11) td:nth-of-type(2)').text),
        '泰幣(THB)':float(htmlfile.select_one('tbody tr:nth-of-type(12) td:nth-of-type(2)').text),
        '菲國比索(PHP)':float(htmlfile.select_one('tbody tr:nth-of-type(13) td:nth-of-type(2)').text),
        '印尼幣(IDR)':float(htmlfile.select_one('tbody tr:nth-of-type(14) td:nth-of-type(2)').text),
        '歐元(EUR)':float(htmlfile.select_one('tbody tr:nth-of-type(15) td:nth-of-type(2)').text),
        '韓元(KRW)':float(htmlfile.select_one('tbody tr:nth-of-type(16) td:nth-of-type(2)').text),
        '越南盾(VND)':float(htmlfile.select_one('tbody tr:nth-of-type(17) td:nth-of-type(2)').text),
        '馬來幣(MYR)':float(htmlfile.select_one('tbody tr:nth-of-type(18) td:nth-of-type(2)').text),
        '人民幣(CNY)':float(htmlfile.select_one('tbody tr:nth-of-type(19) td:nth-of-type(2)').text),
    }
    # 現金匯率/本行賣出
    rates02 = {
        '新台幣(TWD)' : 1,
        '美金(USD)' : float(htmlfile.select_one('tbody tr:nth-of-type(1) td:nth-of-type(3)').text),
        '港幣(HKD)' : float(htmlfile.select_one('tbody tr:nth-of-type(2) td:nth-of-type(3)').text),
        '英鎊(GBP)' : float(htmlfile.select_one('tbody tr:nth-of-type(3) td:nth-of-type(3)').text),
        '澳幣(AUD)' : float(htmlfile.select_one('tbody tr:nth-of-type(4) td:nth-of-type(3)').text),
        '加拿大幣(CAD)':float(htmlfile.select_one('tbody tr:nth-of-type(5) td:nth-of-type(3)').text),
        '新加坡幣(SGD)':float(htmlfile.select_one('tbody tr:nth-of-type(6) td:nth-of-type(3)').text),
        '瑞士法郎(CHF)':float(htmlfile.select_one('tbody tr:nth-of-type(7) td:nth-of-type(3)').text),
        '日圓(JPY)':float(htmlfile.select_one('tbody tr:nth-of-type(8) td:nth-of-type(3)').text),
        '紐元(NZD)':float(htmlfile.select_one('tbody tr:nth-of-type(11) td:nth-of-type(3)').text),
        '泰幣(THB)':float(htmlfile.select_one('tbody tr:nth-of-type(12) td:nth-of-type(3)').text),
        '菲國比索(PHP)':float(htmlfile.select_one('tbody tr:nth-of-type(13) td:nth-of-type(3)').text),
        '印尼幣(IDR)':float(htmlfile.select_one('tbody tr:nth-of-type(14) td:nth-of-type(3)').text),
        '歐元(EUR)':float(htmlfile.select_one('tbody tr:nth-of-type(15) td:nth-of-type(3)').text),
        '韓元(KRW)':float(htmlfile.select_one('tbody tr:nth-of-type(16) td:nth-of-type(3)').text),
        '越南盾(VND)':float(htmlfile.select_one('tbody tr:nth-of-type(17) td:nth-of-type(3)').text),
        '馬來幣(MYR)':float(htmlfile.select_one('tbody tr:nth-of-type(18) td:nth-of-type(3)').text),
        '人民幣(CNY)':float(htmlfile.select_one('tbody tr:nth-of-type(19) td:nth-of-type(3)').text),
    }
    # 即期匯率/本行買入
    rates03 = {
        '新台幣(TWD)': 1,
        '美金(USD)': float(htmlfile.select_one('tbody tr:nth-of-type(1) td:nth-of-type(4)').text),
        '港幣(HKD)': float(htmlfile.select_one('tbody tr:nth-of-type(2) td:nth-of-type(4)').text),
        '英鎊(GBP)': float(htmlfile.select_one('tbody tr:nth-of-type(3) td:nth-of-type(4)').text),
        '澳幣(AUD)': float(htmlfile.select_one('tbody tr:nth-of-type(4) td:nth-of-type(4)').text),
        '加拿大幣(CAD)': float(htmlfile.select_one('tbody tr:nth-of-type(5) td:nth-of-type(4)').text),
        '新加坡幣(SGD)': float(htmlfile.select_one('tbody tr:nth-of-type(6) td:nth-of-type(4)').text),
        '瑞士法郎(CHF)': float(htmlfile.select_one('tbody tr:nth-of-type(7) td:nth-of-type(4)').text),
        '日圓(JPY)': float(htmlfile.select_one('tbody tr:nth-of-type(8) td:nth-of-type(4)').text),
        '南非幣(ZAR)':float(htmlfile.select_one('tbody tr:nth-of-type(9) td:nth-of-type(4)').text),
        '瑞典幣(SEK)':float(htmlfile.select_one('tbody tr:nth-of-type(10) td:nth-of-type(4)').text),
        '紐元(NZD)': float(htmlfile.select_one('tbody tr:nth-of-type(11) td:nth-of-type(4)').text),
        '泰幣(THB)': float(htmlfile.select_one('tbody tr:nth-of-type(12) td:nth-of-type(4)').text),
        '歐元(EUR)': float(htmlfile.select_one('tbody tr:nth-of-type(15) td:nth-of-type(4)').text),
        '人民幣(CNY)': float(htmlfile.select_one('tbody tr:nth-of-type(19) td:nth-of-type(4)').text),
    }
    # 即期匯率/本行賣出
    rates04 = {
        '新台幣(TWD)': 1,
        '美金(USD)': float(htmlfile.select_one('tbody tr:nth-of-type(1) td:nth-of-type(5)').text),
        '港幣(HKD)': float(htmlfile.select_one('tbody tr:nth-of-type(2) td:nth-of-type(5)').text),
        '英鎊(GBP)': float(htmlfile.select_one('tbody tr:nth-of-type(3) td:nth-of-type(5)').text),
        '澳幣(AUD)': float(htmlfile.select_one('tbody tr:nth-of-type(4) td:nth-of-type(5)').text),
        '加拿大幣(CAD)': float(htmlfile.select_one('tbody tr:nth-of-type(5) td:nth-of-type(5)').text),
        '新加坡幣(SGD)': float(htmlfile.select_one('tbody tr:nth-of-type(6) td:nth-of-type(5)').text),
        '瑞士法郎(CHF)': float(htmlfile.select_one('tbody tr:nth-of-type(7) td:nth-of-type(5)').text),
        '日圓(JPY)': float(htmlfile.select_one('tbody tr:nth-of-type(8) td:nth-of-type(5)').text),
        '南非幣(ZAR)': float(htmlfile.select_one('tbody tr:nth-of-type(9) td:nth-of-type(5)').text),
        '瑞典幣(SEK)': float(htmlfile.select_one('tbody tr:nth-of-type(10) td:nth-of-type(5)').text),
        '紐元(NZD)': float(htmlfile.select_one('tbody tr:nth-of-type(11) td:nth-of-type(5)').text),
        '泰幣(THB)': float(htmlfile.select_one('tbody tr:nth-of-type(12) td:nth-of-type(5)').text),
        '歐元(EUR)': float(htmlfile.select_one('tbody tr:nth-of-type(15) td:nth-of-type(5)').text),
        '人民幣(CNY)': float(htmlfile.select_one('tbody tr:nth-of-type(19) td:nth-of-type(5)').text),
    }

    return rates01,rates02,rates03,rates04

app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
w.setWindowTitle('匯率轉換器')

w.setStyleSheet('font-size: 24px')


dollar_label = QtWidgets.QLabel(w)
grid = QtWidgets.QGridLayout(w)
dollar_label.setText('換匯方式 ')
grid.addWidget(dollar_label, 0,0)
dollar_sel0 = QtWidgets.QComboBox(w)
dollar_sel0.addItems(["需要外幣現鈔","帳戶間的換匯"])
grid.addWidget(dollar_sel0,0,1)
dollar_label0 = QtWidgets.QLabel(w)
dollar_label0.setText('我想要將')
grid.addWidget(dollar_label0, 2,0)
dollar_sel1 = QtWidgets.QComboBox(w)
dollar_sel1.addItems(['新台幣(TWD)','美金(USD)','港幣(HKD)','英鎊(GBP)','澳幣(AUD)','加拿大幣(CAD)','新加坡幣(SGD)','瑞士法郎(CHF)','日圓(JPY)','南非幣(ZAR)','瑞典幣(SEK)','紐元(NZD)','泰幣(THB)','菲國比索(PHP)','印尼幣(IDR)','歐元(EUR)','韓元(KRW)','越南盾(VND)','馬來幣(MYR)','人民幣(CNY)'])
grid.addWidget(dollar_sel1, 2,1)
dollar_label1 = QtWidgets.QLabel(w)
dollar_label1.setText('兌換為')
grid.addWidget(dollar_label1, 2,2)
dollar_sel2 = QtWidgets.QComboBox(w)
dollar_sel2.addItems(['新台幣(TWD)','美金(USD)','港幣(HKD)','英鎊(GBP)','澳幣(AUD)','加拿大幣(CAD)','新加坡幣(SGD)','瑞士法郎(CHF)','日圓(JPY)','南非幣(ZAR)','瑞典幣(SEK)','紐元(NZD)','泰幣(THB)','菲國比索(PHP)','印尼幣(IDR)','歐元(EUR)','韓元(KRW)','越南盾(VND)','馬來幣(MYR)','人民幣(CNY)'])
grid.addWidget(dollar_sel2, 2,3)
dollar_label2 = QtWidgets.QLabel(w)
dollar_label2.setText('金額')
grid.addWidget(dollar_label2,4,0)
dollar_input = QtWidgets.QLineEdit(w)
grid.addWidget(dollar_input, 4,1,1,2)
dollar_btn = QtWidgets.QPushButton(w)
dollar_btn.setText('換算')
grid.addWidget(dollar_btn, 4, 3,1,1)
result = QtWidgets.QTextEdit(w)
grid.addWidget(result, 5, 0,1,4)

def dollar():
    # 每次按下按鈕都抓一次最新資料
    rates01, rates02, rates03, rates04 = fetch_rates()

    match dollar_sel0.currentText():
        case "需要外幣現鈔":
            if dollar_sel1.currentText()== '南非幣(ZAR)' or dollar_sel1.currentText()== '瑞典幣(SEK)':
                result.setText(f'此幣別沒有提供直接兌換外幣現鈔服務')
            elif dollar_sel2.currentText()== '南非幣(ZAR)' or dollar_sel2.currentText()== '瑞典幣(SEK)':
                result.setText(f'此幣別沒有提供直接兌換外幣現鈔服務')
            elif dollar_sel1.currentText() == dollar_sel2.currentText():
                result.setText(f'幣別相同無須匯率換算，還是{dollar_sel1.currentText()}{dollar_input.text()}\n現金匯率的買入/賣出匯率={rates01[dollar_sel1.currentText()]}/{rates02[dollar_sel2.currentText()]}')
            else:
                result.setText(f'換算匯率為{rates02[dollar_sel2.currentText()]/rates01[dollar_sel1.currentText()]:.3f}\n{dollar_sel1.currentText()}{dollar_input.text()}約為{dollar_sel2.currentText()}{float(dollar_input.text())*rates01[dollar_sel1.currentText()]/rates02[dollar_sel2.currentText()]:.2f}')
        case "帳戶間的換匯":
            if dollar_sel1.currentText()== '菲國比索(PHP)' or dollar_sel1.currentText()== '印尼幣(IDR)' or dollar_sel1.currentText()== '韓元(KRW)' or dollar_sel1.currentText()== '越南盾(VND)' or dollar_sel1.currentText()== '馬來幣(MYR)':
                result.setText(f'此幣別沒有提供帳戶間的換匯服務')
            elif dollar_sel2.currentText()== '菲國比索(PHP)' or  dollar_sel1.currentText()== '印尼幣(IDR)' or dollar_sel1.currentText()== '韓元(KRW)' or dollar_sel1.currentText()== '越南盾(VND)' or dollar_sel1.currentText()== '馬來幣(MYR)':
                result.setText(f'此幣別沒有提供帳戶間的換匯服務')
            elif dollar_sel1.currentText() == dollar_sel2.currentText():
                result.setText(f'幣別相同無須匯率換算，還是{dollar_sel1.currentText()}{dollar_input.text()}\n即期匯率的買入/賣出匯率={rates03[dollar_sel1.currentText()]}/{rates04[dollar_sel2.currentText()]}')
            else:
                result.setText(f'換算匯率為{rates04[dollar_sel2.currentText()]/rates03[dollar_sel1.currentText()]:.3f}\n{dollar_sel1.currentText()}{dollar_input.text()}約為{dollar_sel2.currentText()}{float(dollar_input.text())*rates03[dollar_sel1.currentText()]/rates04[dollar_sel2.currentText()]:.2f}')

dollar_btn.clicked.connect(dollar)

w.show()
sys.exit(app.exec())
