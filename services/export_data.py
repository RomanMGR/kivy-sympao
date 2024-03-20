import time
import csv
import smtplib
from datetime import datetime
from kivy.storage.jsonstore import JsonStore
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from jnius import autoclass
from android import activity


class ExportData:
    def __init__(self):
        self.store = JsonStore('Results.json')
        self.time_list = []
        self.react_time_list_pos = []
        self.react_time_list_sound = []
        self.comment_list_corsi = []
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

    def react_time_corsi(self, pressed_btns, check_list):
        curr = datetime.now()
        self.react_time_list_sound.append(curr)
        self.comment_list_sound.append(pressed_btns)
        self.comment_list_corsi.append(check_list)

    def add_time(self):
        for i in range(len(self.react_time_list_pos) - 1):
            time = self.react_time_list_pos[i+1] - self.react_time_list_pos[i]
            self.dict_pos = {'step': 'Pos ' + str(i+1),
                             'diff_time': str(time),
                             'choice': str(self.comment_list_pos[i+1])}
            self.export_list.append(self.dict_pos)

    def get_model(self):
        build = autoclass('android.os.Build')
        model_device = str(build.DEVICE)
        return model_device

    def diff_time(self, result, export_n, uuid):
        print('start')
        for i in range(len(self.time_list)):
            self.diff_time_list_pos.append(self.react_time_list_pos[i] - self.time_list[i])
            self.diff_time_list_sound.append(self.react_time_list_sound[i] - self.time_list[i])
        print('2222222222222222222222222')
        model = self.get_model()
        text = 'N-back ' + result + '\n' + 'Step back=' + str(export_n) + ' model=' + model + ' uuid=' + str(uuid)
        for i in range(len(self.diff_time_list_pos)):
            self.dict_pos = {'step': 'Pos '+str(i),
                             'diff_time': str(self.diff_time_list_pos[i]),
                             'comment': str(self.comment_list_pos[i])}
            self.export_list.append(self.dict_pos)
        print('3333333333333')
        for i in range(len(self.diff_time_list_sound)):
            self.dict_sound = {'step_sound': 'Sound '+str(i),
                             'diff_time_sound': str(self.diff_time_list_sound[i]),
                             'comment_sound': str(self.comment_list_sound[i])}
            self.export_list.append(self.dict_sound)
        print('44444444444')
        self.send_email(subject=str(self.time_list[0]), to_addr='neyropolikor.testy@mail.ru', body_text=text,
                        cols=['step', 'diff_time', 'comment', 'step_sound', 'diff_time_sound', 'comment_sound'])
        print('end !!!')

    def send_scab(self, all_time, averange_first, averange_second, delta_averange, percent, total_first, total_second,
                  answer, uuid):
        self.dict_pos = {'all_time': 'Общее время выполнения теста',
                         'averange_first': 'Среднее время ответа в первом этапе',
                         'averange_second': 'Среднее время ответа во втором этапе',
                         'delta_averange': 'Среднее время задержки',
                         'percent': 'Процент от среднего времени реакции в первой очереди эксперимента',
                         'total_first':  'Количество ошибок в первой части теста',
                         'total_second': 'Количество ошибок во второй части теста',
                         'answer': 'комментарий',
                         'step': 'step',
                         'diff_time': 'diff_time',
                         'choice': 'choice'}
        self.export_list.append(self.dict_pos)
        self.dict_pos = {'all_time': all_time,
                         'averange_first': averange_first,
                         'averange_second': averange_second,
                         'delta_averange': delta_averange,
                         'percent': percent,
                         'total_first': 30-total_first,
                         'total_second': 30-total_second,
                         'answer': answer}
        self.export_list.append(self.dict_pos)
        self.add_time()
        self.time_list.append(datetime.now())
        text = 'Scab ' + '\n' + 'model=' + str(self.get_model()) + ' uuid=' + str(uuid)
        self.send_email(subject=str(self.time_list[0]), to_addr='neyropolikor.testy@mail.ru', body_text=text,
                        cols=['all_time', 'averange_first', 'averange_second', 'delta_averange', 'percent',
                              'total_first', 'total_second', 'answer', 'step', 'diff_time', 'choice'])

    def export_corsi(self, text, uuid, flag):
        self.dict_pos = {'text': 'шаг',
                         'flag': 'обратный порядок ответов',
                         'step': 'step',
                         'diff_time': 'diff_time',
                         'pressed_btns':  'pressed_btns',
                         'check_list': 'check_list'}
        self.export_list.append(self.dict_pos)
        self.dict_pos = {'text': text,
                         'flag': flag}
        self.export_list.append(self.dict_pos)
        for i in range(len(self.react_time_list_pos)):
            time = self.react_time_list_sound[i] - self.react_time_list_pos[i]
            self.dict_pos = {'step': 'Pos ' + str(i+2),
                             'diff_time': str(time),
                             'pressed_btns': str(self.comment_list_sound[i]),
                             'check_list': str(self.comment_list_corsi[i])}
            self.export_list.append(self.dict_pos)
        text = 'Corsi ' + '\n' + 'model=' + str(self.get_model()) + ' uuid=' + str(uuid)
        self.time_list.append(datetime.now())
        self.send_email(subject=str(self.time_list[0]), to_addr='neyropolikor.testy@mail.ru', body_text=text,
                        cols=['text', 'flag', 'step', 'diff_time', 'pressed_btns', 'check_list'])

    def export_anxiety(self, count, export, uuid):
        self.dict_pos = {'count': 'count',
                         'comment': 'comment',
                         'step': 'step',
                         'diff_time': 'diff_time',
                         'choice': 'choice'}
        self.export_list.append(self.dict_pos)
        self.dict_pos = {'count': count,
                         'comment': export}
        self.export_list.append(self.dict_pos)
        self.add_time()
        self.time_list.append(datetime.now())
        text = 'Sheehan Patient-Rated Anxiety Scale ' + '\n' + 'model=' + str(self.get_model()) + ' uuid=' + str(uuid)
        self.send_email(subject=str(self.time_list[0]), to_addr='neyropolikor.testy@mail.ru', body_text=text,
                        cols=['count', 'comment', 'step', 'diff_time', 'choice'])

    def send_asthenia(self, export, uuid, count_list):
        self.dict_pos = {'answer': 'answer',
                         'step': 'step',
                         'diff_time': 'diff_time',
                         'choice': 'choice'}
        self.export_list.append(self.dict_pos)
        self.dict_pos = {'answer': export,
                         'balls': count_list}
        self.export_list.append(self.dict_pos)
        self.add_time()
        self.time_list.append(datetime.now())
        text = 'Asthenia scale ' + '\n' + 'model=' + str(self.get_model()) + ' uuid=' + str(uuid)
        self.send_email(subject=str(self.time_list[0]), to_addr='neyropolikor.testy@mail.ru', body_text=text,
                        cols=['answer', 'balls', 'step', 'diff_time', 'choice'])

    def export_scale_beck(self, count, comment, uuid):
        self.dict_pos = {'count': 'count',
                         'comment': 'comment',
                         'step': 'step',
                         'diff_time': 'diff_time',
                         'choice': 'choice'}
        self.export_list.append(self.dict_pos)
        self.dict_pos = {'count': count,
                         'comment': comment}
        self.export_list.append(self.dict_pos)
        self.add_time()
        self.time_list.append(datetime.now())
        text = 'Scale Beck ' + '\n' + 'model=' + str(self.get_model()) + ' uuid=' + str(uuid)
        self.send_email(subject=str(self.time_list[0]), to_addr='neyropolikor.testy@mail.ru', body_text=text,
                        cols=['count', 'comment', 'step', 'diff_time', 'choice'])

    def send_email(self, subject, to_addr, body_text, cols):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = 'fo180006@mail.ru'
        msg['To'] = to_addr
        msgText = MIMEText('<b>%s</b>' % (body_text), 'html')
        msg.attach(msgText)
        with open('file.csv', 'w', newline='', encoding='UTF-16') as file:
            writer = csv.DictWriter(file, fieldnames=cols, delimiter=';')
            writer.writerows(self.export_list)
        export_file = MIMEApplication(open('file.csv', 'rb').read())
        export_file.add_header('Content-Disposition', 'attachment', filename='file.csv')
        msg.attach(export_file)
        print('send data')
        server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        server.login('fo180006@mail.ru', 'qbWx16dcMSuySCJwtZtu')
        server.sendmail('fo180006@mail.ru', to_addr, msg.as_string())
        server.quit()
        self.clear()

    def clear(self):
        self.time_list.clear()
        self.react_time_list_pos.clear()
        self.react_time_list_sound.clear()
        self.comment_list_pos.clear()
        self.comment_list_sound.clear()
        self.diff_time_list_pos.clear()
        self.diff_time_list_sound.clear()
        self.dict_pos.clear()
        self.dict_sound.clear()
        self.export_list.clear()
        self.comment_list_corsi.clear()

