import time
import csv
import smtplib
from datetime import datetime
from kivy.storage.jsonstore import JsonStore
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText


class ExportData:
    def __init__(self):
        self.store = JsonStore('Results.json')
        self.time_list = []
        self.react_time_list_pos = []
        self.react_time_list_sound = []
        self.comment_list_pos = []
        self.comment_list_sound = []
        self.diff_time_list_pos = []
        self.diff_time_list_sound = []
        self.dict_pos = {}
        self.dict_sound = {}
        self.export_list = []

    def time(self, step):
        curr = datetime.now()
        self.time_list.append(curr)
        print(step, time.localtime())

    def react_time_pos(self, result):
        curr = datetime.now()
        self.react_time_list_pos.append(curr)
        self.comment_list_pos.append(result)
        print(result, curr)

    def react_time_sound(self, result):
        curr = datetime.now()
        self.react_time_list_sound.append(curr)
        self.comment_list_sound.append(result)
        print(result, curr)

    def diff_time(self, result):
        for i in range(len(self.time_list)):
            self.diff_time_list_pos.append(self.react_time_list_pos[i] - self.time_list[i])
            self.diff_time_list_sound.append(self.react_time_list_sound[i] - self.time_list[i])
        print(self.diff_time_list_pos)
        print(self.diff_time_list_sound)
        text = result
        for i in range(len(self.diff_time_list_pos)):
            # self.store.put(key=i, diff_time=str(self.diff_time_list_pos[i]), comment=str(self.comment_list_pos[i]))
            self.dict_pos = {'step': 'Pos '+str(i),
                             'diff_time': str(self.diff_time_list_pos[i]),
                             'comment': str(self.comment_list_pos[i])}
            self.export_list.append(self.dict_pos)
        for i in range(len(self.diff_time_list_sound)):
            # self.store.put(key=i, diff_time=str(self.diff_time_list_sound[i]), comment=str(self.comment_list_sound[i]))
            self.dict_sound = {'step': 'Sound '+str(i),
                             'diff_time': str(self.diff_time_list_sound[i]),
                             'comment': str(self.comment_list_sound[i])}
            self.export_list.append(self.dict_sound)
        self.send_email(subject=str(self.time_list[0]), to_addr='roman_nasyrov00@mail.ru', body_text=text)
        print('end !!!')

    def send_email(self, subject, to_addr, body_text):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = 'fo180006@mail.ru'
        msg['To'] = to_addr
        msgText = MIMEText('<b>%s</b>' % (body_text), 'html')
        msg.attach(msgText)
        cols = ['step', 'diff_time', 'comment']
        print(self.dict_pos)
        print(self.dict_sound)
        with open('file.csv', 'w', newline='', encoding='UTF-8') as file:
            writer = csv.DictWriter(file, fieldnames=cols, delimiter=',')
            writer.writerows(self.export_list)
        export_file = MIMEApplication(open('file.csv', 'rb').read())
        export_file.add_header('Content-Disposition', 'attachment', filename='file.csv')
        msg.attach(export_file)
        server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        server.login('fo180006@mail.ru', 'qbWx16dcMSuySCJwtZtu')
        server.sendmail('fo180006@mail.ru', to_addr, msg.as_string())
        server.quit()




