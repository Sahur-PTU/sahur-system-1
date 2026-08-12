# sahur system - [1] / v-1.2 / 25.07.2026

#    \____
#   sa\____\
#    hur\__\
#         \

import os
import time 
import datetime
import subprocess
import json
import webbrowser
import pyperclip
from colorama import init, Fore, Back, Style

init()
#os.system('mode con: cols=60 lines=17')


programs = {
 'pr_1' : {'num':'1', 'par': 'none', 'name':'none', 'dir': 'none', 'delay':1},
 'pr_2' : {'num':'2', 'par': 'none', 'name':'none', 'dir': 'none', 'delay':1},
 'pr_3' : {'num':'3', 'par': 'none', 'name':'none', 'dir': 'none', 'delay':1},
 'pr_4' : {'num':'4', 'par': 'none', 'name':'none', 'dir': 'none', 'delay':1},
 'pr_5' : {'num':'5', 'par': 'none', 'name':'none', 'dir': 'none', 'delay':1},
 'main_delay' : 1,
 'sessions' : {}
}

b_m = [None, None, None, None, None] 

def write() : 
  with open('data.json', 'w', encoding='utf-8') as file:  
    json.dump(programs, file, ensure_ascii=False, indent=2)

def read() :
  try: 
    with open('data.json', 'r', encoding='utf-8') as file:
      data = json.load(file)
      programs.clear()
      programs.update(data)
  except FileNotFoundError: 
    print('файл "data.json" не найден'), time.sleep(1)
    _write = write()

def _exit() :
  print("закругляемся")
  _read = read(), time.sleep(0.5)
  update_write = write()
  print(Fore.BLUE, " [ℹ]-System : stop ", Style.RESET_ALL), time.sleep(0.5)
  exit()

print(Fore.GREEN+"sahur system - [1] / v-1.2 / 25.07.2026"+Style.RESET_ALL), time.sleep(1)
print(Fore.BLUE,"[1]-System : Запуск \n"), time.sleep(0.5)
print(" [2]-System : Проверка систем (1) "), time.sleep(0.3)
print('  расположение:', os.getcwd()), time.sleep(0.3)
print(" [3]-System : Проверка систем (2) \n"), time.sleep(1)
os.system('cls') 

print(Fore.MAGENTA,'')
_read = read()
if len(programs['sessions']) > 0: last_log = list(programs['sessions'].values())[-1]
else: last_log = "none"
print("последняя сессия :", last_log)
programs['sessions'][str(len(programs['sessions'])+1)] = str(datetime.datetime.now())[:-10]
update_write = write()
print("текущая сессия   :", str(datetime.datetime.now())[:-10]), time.sleep(2)
print(Fore.GREEN,'')


#os.system('cls')

print(programs['main_delay'])
print("Добро пожаловать!"), time.sleep(1)
def menu():
  while True:
    #os.system('cls')
    # посчёт символов
    a1 = len(str(programs['pr_1']['num']+'. '+programs['pr_1']['name']))
    a2 = len(programs['pr_2']['num']+'. '+programs['pr_2']['name'])
    a3 = len(programs['pr_3']['num']+'. '+programs['pr_3']['name'])
    a4 = len(programs['pr_4']['num']+'. '+programs['pr_4']['name'])
    a5 = len(programs['pr_5']['num']+'. '+programs['pr_5']['name'])
    # подсчёт отступов
    a_1 = ' ' * (14 - a1)
    a_2 = ' ' * (14 - a2)
    a_3 = ' ' * (14 - a3)
    a_4 = ' ' * (14 - a4)
    a_5 = ' ' * (14 - a5)
    # сборка имён
    b_m[0] = programs['pr_1']['num']+'. '+programs['pr_1']['name']+a_1
    b_m[1] = programs['pr_2']['num']+'. '+programs['pr_2']['name']+a_2
    b_m[2] = programs['pr_3']['num']+'. '+programs['pr_3']['name']+a_3
    b_m[3] = programs['pr_4']['num']+'. '+programs['pr_4']['name']+a_4
    b_m[4] = programs['pr_5']['num']+'. '+programs['pr_5']['name']+a_5

    # основное меню
    print("╭─────────────────── ╭────────────╮"), time.sleep(0.05)
    print("│  Sahur System [1]  │  v - 1.2.  │"), time.sleep(0.05)
    print("╰────────────────╮ ──╯ ────────── │"), time.sleep(0.05)
    print("│  главное меню  │ ", b_m[0] +   "│"), time.sleep(0.05)
    print("│ ────────────── │ ", b_m[1] +   "│"), time.sleep(0.05)
    print("│ [1] - Старт    │ ", b_m[2] +   "│"), time.sleep(0.05)
    print("│ [2] - Настр    │ ", b_m[3] +   "│"), time.sleep(0.05)
    print("│ [3] - Сессии   │ ", b_m[4] +   "│"), time.sleep(0.05)
    print("╰─────────────── ╰────────────────╯"), time.sleep(0.5) 
    de = input('>> ')

    def start():
        try:
          print('Запуск'), time.sleep(1), os.system('cls')
          if programs['pr_1']['name'] == 'none':
            print('запуск (1) небудем это хапускать'), time.sleep(programs['pr_1']['delay'])
          else: 
            print("запуск (1)"), time.sleep(programs['pr_1']['delay'])
            exec(programs['pr_1']['par']+'("'+programs['pr_1']['dir']+'")')

          if programs['pr_2']['name'] == 'none':
            print('запуск (2) небудем это хапускать'), time.sleep(programs['pr_2']['delay'])
          else: 
            print("запуск (2)"), time.sleep(programs['pr_2']['delay'])
            exec(programs['pr_2']['par']+'("'+programs['pr_2']['dir']+'")')
            
          if programs['pr_3']['name'] == 'none':
            print('запуск (3) небудем это хапускать'), time.sleep(programs['pr_3']['delay'])
          else: 
            print("запуск (3)"), time.sleep(programs['pr_3']['delay'])
            exec(programs['pr_3']['par']+'("'+programs['pr_3']['dir']+'")') # СДЕЛАТЬ ПОЛЬХОВАТЕЛЬСКУЮ НАСТРОЙКУ СКОРОСТИ ЗАПУСАКА

          if programs['pr_4']['name'] == 'none':
            print('запуск (4) небудем это хапускать'), time.sleep(programs['pr_4']['delay'])
          else: 
            print("запуск (4)"), time.sleep(programs['pr_4']['delay'])
            exec(programs['pr_4']['par']+'("'+programs['pr_4']['dir']+'")')

          if programs['pr_5']['name'] == 'none':
            print('запуск (5) небудем это хапускать'), time.sleep(programs['pr_5']['delay'])
          else: 
            print("запуск (5)"), time.sleep(programs['pr_5']['delay'])
            exec(programs['pr_5']['par']+'("'+programs['pr_5']['dir']+'")')
        
        except FileNotFoundError: print('Один из файлов не был найден')
        except KeyboardInterrupt: 
          print("Искусcтвенная остановка запуска"), time.sleep(0.5)
          return "artificial_stoppage"
       #except: print("[start] неизвестная ошибка"), time.sleep(3)
        
        time.sleep(1)
        #os.system('cls')
        return "completed"
    if de == '1': 
      _start = start()
      print(_start), time.sleep(0.5)
      input()
    elif de == '2': return "settings"
    elif de == '3': return "sessions"
    elif de == ' ': return "exit"


def settings() :
      while True:
        print("╭─────────────────── ╭────────────╮"), 
        print("│  Sahur System [1]  │  v - 1.2.  │"), 
        print("╰────────────────╮ ──╯ ────────── │"), 
        print("│   настройки    │ ", b_m[0] +   "│"), 
        print("│ ────────────── │ ", b_m[1] +   "│"),
        print("│ [1] - Задержка │ ", b_m[2] +   "│"),
        print("│ [2] - Конфиги  │ ", b_m[3] +   "│"),
        print("│ [3] - Назад    │ ", b_m[4] +   "│"), 
        print("╰─────────────── ╰────────────────╯"), time.sleep(0.5) 
        de = input('>> ')
        if de == '1':
          print("Задайте скорость задержки при запуске")
          try: delay = int(input(" > "))
          except ValueError: 
            print("цифры вводи нормальные да"), time.sleep(1)
            continue
          else: 
            programs['delay'] = delay
            update_write = write()
            print("Сохранено успешно!"), time.sleep(1)
            continue
        elif de == '2': return "configs"
        elif de == '3' or de == ' ': return "return_to_menu"
        else: continue

def configurations() :
  while True:
    #try:
            proga = str(input('Номер проги: '))
            if proga == " ": return "return_to_settings"
            proga1 = 'pr_' + proga
            if proga1 in programs:
              os.system('cls')
              while True:
                if proga1 == 'pr_1': b = [Fore.YELLOW+b_m[0]+Fore.GREEN, b_m[1], b_m[2], b_m[3], b_m[4]]
                if proga1 == 'pr_2': b = [b_m[0], Fore.YELLOW+b_m[1]+Fore.GREEN, b_m[2], b_m[3], b_m[4]]
                if proga1 == 'pr_3': b = [b_m[0], b_m[1], Fore.YELLOW+b_m[2]+Fore.GREEN, b_m[3], b_m[4]]
                if proga1 == 'pr_4': b = [b_m[0], b_m[1], b_m[2], Fore.YELLOW+b_m[3]+Fore.GREEN, b_m[4]]
                if proga1 == 'pr_5': b = [b_m[0], b_m[1], b_m[2], b_m[3], Fore.YELLOW+b_m[4]+Fore.GREEN]

                print("╭─────────────────── ╭────────────╮"), 
                print("│  Sahur System [1]  │  v - 1.2.  │"), 
                print("╰────────────────╮ ──╯ ────────── │"), 
                print("│  конфигурация  │ ", b[0] +     "│"),# ДАТЬ ВЫБОР: ОСТАВЛЯТЬ СТАРЫЙ ПУТЬ ИЛИ НЕТ
                print("│ ────────────── │ ", b[1] +     "│"),  
                print("│ [1] - Изменить │ ", b[2] +     "│"),  
                print("│ [2] - Удалить  │ ", b[3] +     "│"), # ПОКАЗЫВАТЬ ДЕРИКТОИЮ И ПАРАМТР
                print("│ [3] - Назад    │ ", b[4] +     "│"),  
                print("╰─────────────── ╰────────────────╯"), time.sleep(0.5)  
                de = input('>> ')
                if de == '1': 
                  print(programs[proga1])
                  print('Доступные функции:\n [1] - os.startfile (запуск файла)\n [2] - pyperclip.copy (копирование в буфер)\n [3] - webbrowser.open (открытие ссылки)'), time.sleep(0.5)
                  de = input('>> ') # ДОБАВИТЬ ФУНКЦИЮ ОТКРЫТИЯ ССЫЛОК 
                  if de == '1': 
                    par = 'os.startfile'
                    print("[1] - Оставить старое")
                    name = str(input("Имя (не более 10 символов): "))
                    if name == '1': name = programs[proga1]['name']
                    if name == ' ': continue
                    if len(name) < 10:
                      print('поддерживается только запуск файлов, папки не запустим.')
                      print("[1] - Оставить старый")
                      dir = input("Путь: ") 
                      if dir == '1': dir = programs[proga1]['dir']
                      dir_1 = dir.replace("\\", "/")
                      print(dir_1), time.sleep(3)
                      try: # проверка процесса 
                        exec('os.startfile('+'"'+dir_1+'"'+')'), time.sleep(3) 
                      except FileNotFoundError: 
                        print('Директория не найдена'), time.sleep(1)
                        continue
                      #except: print('неизвестная ошибка')
                      else:
                        #try:
                          v = str("taskkill /f /im " + dir_1)# НА ЗАКРЫТИИ НЕ ИСПОЛЬЗОВАТЬ РАЗВЁРНУТЫЫЙ ПУТЬ 
                          os.system(v)
                          time.sleep(1)
                        #except: 
                          #print("кажется, вы ввели неправильный путь к файлу. (папки не поддерживаются)"), time.sleep(2)
                          #continue
                        #else: 
                          while True:
                            try: delay = int(input("задержка: "))
                            except ValueError: print("цифры вводи нормальные да"), time.sleep(1)
                            else: break
                          print("Сохранено успешно")
                          programs[proga1]['par'] = par
                          programs[proga1]['name'] = name
                          programs[proga1]['dir'] = dir_1
                          programs[proga1]['delay'] = delay
                          update_write = write()
                          print(programs), time.sleep(1)
                          menu()
                    else: 
                      print('имя содержит более 10 символов!'), time.sleep(1)
                      continue

                  elif de == '2':
                    par = 'pyperclip.copy'
                    print("[1] - Оставить старое")
                    name = str(input("Имя (не более 10 символов): "))
                    if name == '1': name = programs[proga1]['name']
                    if name == ' ': continue
                    if len(name) < 10:
                      print("[1] - Оставить старый")
                      text = str(input("Текст: "))
                      if text == '1': text = programs[proga1]['dir']
                      while True:
                        try: delay = int(input("задержка: "))
                        except ValueError: print("цифры вводи нормальные да"), time.sleep(1)
                        else: break
                      programs[proga1]['par'] = par
                      programs[proga1]['name'] = name
                      programs[proga1]['dir'] = text
                      update_write = write()
                      print('сохранено успешно')
                      print(programs), time.sleep(1)
                      menu()
                    else: 
                      print('имя содержит более 10 символов!'), time.sleep(1)
                      continue
                  elif de == '3': 
                    while True:
                      par = 'webbrowser.open'
                      print("[1] - Оставить старое")
                      name = str(input("Имя (не более 10 символов): "))
                      if name == '1': name = programs[proga1]['name']
                      if name == ' ': break
                      if len(name) < 10: 
                        print("[1] - Оставить старую")
                        url = input("Ссылка: ")
                        if url == '1': url = programs[proga1]['dir']
                        print("тест"), time.sleep(0.5)
                        webbrowser.open_new_tab(url), time.sleep(2)
                        print("[1] - Работает, сохранить\n[2] - Не работает, изменить адрес")
                        pr = input(">> ")
                        if pr == "1": 
                          while True:
                            try: delay = int(input("задержка: "))
                            except ValueError: print("цифры вводи нормальные да"), time.sleep(1)
                            else: break
                          programs[proga1]['par'] = par
                          programs[proga1]['name'] = name
                          programs[proga1]['dir'] = url
                          update_write = write()
                          print('сохранено успешно'), time.sleep(0.5)
                          print(programs), time.sleep(0.5)
                          break
                        else: continue
                  
                  else: 
                    print("нормально вводи да"), time.sleep(1)
                    continue
            
                elif de == '2':
                  print("Точно дэлете?")
                  print("[1] - Да")
                  print("[2] - Не")
                  de = input('>> ')
                  if de == '1':
                    programs[proga1]['par'] = 'none'
                    programs[proga1]['name'] = 'none'
                    programs[proga1]['dir'] = 'none'
                    programs[proga1]['delay'] = 1
                    update_write = write()
                    print(programs), time.sleep(1)
                    menu()
                  elif de == '2': continue
                elif de == '3' or de == ' ': return "return_to_settings"
                else: continue
            else: 
              print("нету таких"), time.sleep(1)       
              continue
    #except: print("[configs] неизвестная ошибка")

def sessions() :
  while True:
    try:
      for sess in programs['sessions']:
        if len(sess) == 1: print('0'+sess,'-', programs['sessions'][sess]), time.sleep(0.05)
        else: print(sess, '-', programs['sessions'][sess]), time.sleep(0.05)
      print("[1] - Очистить историю")
      print("[2] - Назад")
      de = input(" > ")
      if de == '1': 
        programs['sessions'].clear()
        update_write = write()
        return "completed"
      elif de == '2' or de == ' ': return "return_to_menu"
    except: print("[sessions] неизвестная ошибка")


# общий алгоритм процессов
def main():
  while True:
    #try:
      _menu = menu()
      if _menu == "settings": 
          while True:
            _settings = settings()
            if _settings == "configs":
              _configs = configurations()
              if _configs == None: None
              elif _configs == "return_to_settings": continue
            elif _settings == "return_to_menu": break

      elif _menu == "sessions":
            _sessions = sessions()
            if _sessions == "completed": continue
            elif _sessions == "return_to_menu": continue 

      elif _menu == "exit":
          print("До свидания!"), time.sleep(0.3)
          safe_exit = _exit()
    #except: print("[main] неизвестная ошибка")

_main = main()