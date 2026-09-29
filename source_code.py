# sahur system - [1] / v-1.2 / 26.08.2026

#    \____
#   sa\____\
#    hur\__\
#         \

import os
import sys
import time 
import datetime
import subprocess
import json
import webbrowser
import pyperclip
from colorama import init, Fore, Back, Style


init()
#os.system('mode con: cols=60 lines=17')

GENERAL_COLOR = Fore.WHITE
HIGHLIGHT_COLOR = Fore.YELLOW
RESET_COLOR = Fore.RESET
RESET_ALL = Style.RESET_ALL

parameters = {'system':"none", 'clearOutput':'none','runFile':'none'}
def crossPlatform():
  global parameters
  if sys.platform == "win32": parameters = {'system': "win32", 'clearOutput': "cls", 'runFile': "os.startfile"}
  if sys.platform == "darwin": parameters = {'system': "drawin", 'clearOutput':"clear",'runFile': "subprocess.run"}
  if sys.platform == "xdg-open": parameters = {'system': "xdg-open", 'clearOutput':"clear", 'runFile': "subprocess.run"}
  if sys.platform == "Linux": parameters = {'system': "xdg-open", 'clearOutput':"clear", 'runFile': "subprocess.run"}

programs = {
 'pr_1' : {'num':'1', 'par': 'none', 'name':'none', 'dir': 'none', 'delay':1},
 'pr_2' : {'num':'2', 'par': 'none', 'name':'none', 'dir': 'none', 'delay':1},
 'pr_3' : {'num':'3', 'par': 'none', 'name':'none', 'dir': 'none', 'delay':1},
 'pr_4' : {'num':'4', 'par': 'none', 'name':'none', 'dir': 'none', 'delay':1},
 'pr_5' : {'num':'5', 'par': 'none', 'name':'none', 'dir': 'none', 'delay':1},
 'pr_6' : {'num':'6', 'par': 'none', 'name':'none', 'dir': 'none', 'delay':1},
 'pr_7' : {'num':'7', 'par': 'none', 'name':'none', 'dir': 'none', 'delay':1},
 'pr_8' : {'num':'8', 'par': 'none', 'name':'none', 'dir': 'none', 'delay':1},
 'pr_9' : {'num':'9', 'par': 'none', 'name':'none', 'dir': 'none', 'delay':1},
 'pr_10' : {'num':'10', 'par': 'none', 'name':'none', 'dir': 'none', 'delay':1},
 'main_delay' : 1,
 'sessions' : {}
}


b_m = [None, None, None, None, None, None, None, None, None, None] 

def write() : 
  with open('data/data.json', 'w', encoding='utf-8') as file:  
    json.dump(programs, file, ensure_ascii=False, indent=2)

def read() :
  try: 
    with open('data/data.json', 'r', encoding='utf-8') as file:
      new_data = json.load(file)
      programs.clear(); programs.update(new_data)
  except FileNotFoundError: 
    print('файл "data.json" не найден'); time.sleep(1)
    _write = write(); print("создан в локальной папке"); time.sleep(1)

def _exit() :
  print("закругляемся")
  update_write = write()
  print(Fore.BLUE, " [ℹ]-System : stop ", Style.RESET_ALL); time.sleep(0.5)
  exit()

def information_notification() : 
  """
  print(Fore.GREEN+"sahur system - [1] / v-1.2 / 26.08.2026"+Style.RESET_ALL), time.sleep(1)
  print(Fore.BLUE,"[1]-System : Запуск \n"), time.sleep(0.5)
  print(" [2]-System : Проверка систем (1) "), time.sleep(0.3)
  print('  расположение:', os.getcwd()), time.sleep(0.3)
  print(" [3]-System : Проверка систем (2) \n"), time.sleep(1)
  os.system('cls') 
  """
  #print(Fore.MAGENTA, '')
  _read = read()
  if len(programs['sessions']) > 0: last_log = list(programs['sessions'].values())[-1]
  else: last_log = "none"
  print("последняя сессия :", last_log)
  programs['sessions'][str(len(programs['sessions'])+1)] = str(datetime.datetime.now())[:-10]
  update_write = write()
  print("текущая сессия   :", str(datetime.datetime.now())[:-10]); time.sleep(0.5)
  #print(Fore.GREEN, '')

  print('main_delay:', programs['main_delay'])
  print("Добро пожаловать!"); time.sleep(1)

  #os.system(parameters['clearOutput'])


def calculation_names():
    get_data = read()
     # посчёт символов
    a1 = len(programs['pr_1']['num']+'. '+programs['pr_1']['name'])
    a2 = len(programs['pr_2']['num']+'. '+programs['pr_2']['name'])
    a3 = len(programs['pr_3']['num']+'. '+programs['pr_3']['name'])
    a4 = len(programs['pr_4']['num']+'. '+programs['pr_4']['name'])
    a5 = len(programs['pr_5']['num']+'. '+programs['pr_5']['name'])
    a6 = len(programs['pr_6']['num']+'. '+programs['pr_6']['name'])
    a7 = len(programs['pr_7']['num']+'. '+programs['pr_7']['name'])
    a8 = len(programs['pr_8']['num']+'. '+programs['pr_8']['name'])
    a9 = len(programs['pr_9']['num']+'. '+programs['pr_9']['name'])
    a10 = len(programs['pr_10']['num']+'. '+programs['pr_10']['name'])
     # сборка имён
    b_m[0] = programs['pr_1']['num']+'. '+programs['pr_1']['name']+' ' * (14 - a1)
    b_m[1] = programs['pr_2']['num']+'. '+programs['pr_2']['name']+' ' * (14 - a2)
    b_m[2] = programs['pr_3']['num']+'. '+programs['pr_3']['name']+' ' * (14 - a3)
    b_m[3] = programs['pr_4']['num']+'. '+programs['pr_4']['name']+' ' * (14 - a4)
    b_m[4] = programs['pr_5']['num']+'. '+programs['pr_5']['name']+' ' * (14 - a5)
    b_m[5] = programs['pr_6']['num']+'. '+programs['pr_6']['name']+' ' * (14 - a6)
    b_m[6] = programs['pr_7']['num']+'. '+programs['pr_7']['name']+' ' * (14 - a7)
    b_m[7] = programs['pr_8']['num']+'. '+programs['pr_8']['name']+' ' * (14 - a8)
    b_m[8] = programs['pr_9']['num']+'. '+programs['pr_9']['name']+' ' * (14 - a9)
    b_m[9] = programs['pr_10']['num']+'. '+programs['pr_10']['name']+' ' * (14 - a10)


def start_menu():
  while True:
    #os.system(parameters['clearOutput'])
    get_names = calculation_names()
    # основное меню
    print("╭─────────────────── ╭────────────╮"); time.sleep(0.05)
    print("│  Sahur System [1]  │  v - 1.2.  │"); time.sleep(0.05)
    print("╰────────────────╮ ──╯ ────────── │"); time.sleep(0.05)
    print("│  главное меню  │ ", b_m[0] +   "│"); time.sleep(0.05)
    print("│ ────────────── │ ", b_m[1] +   "│"); time.sleep(0.05)
    print("│ [1] - Старт    │ ", b_m[2] +   "│"); time.sleep(0.05)
    print("│ [2] - Настр    │ ", b_m[3] +   "│"); time.sleep(0.05)
    print("│ [3] - Сессии   │ ", b_m[4] +   "│"); time.sleep(0.05)
    print("╰─────────────── ╰────────────────╯"); time.sleep(0.5) 
    de = input('>> ')

    def start():
        try:
          print('Запуск'); time.sleep(1)
          os.system(parameters['clearOutput'])
          for proc in range(len(programs)-2):
            proc = str(proc + 1)
            if programs[f'pr_{proc}']['name'] == 'none':
              print(f'запуск ({proc}) небудем это хапускать'); time.sleep(programs[f'pr_{proc}']['delay'])
            else: 
              print(f"запуск ({proc})"); time.sleep(programs[f'pr_{proc}']['delay'])
              exec(programs['pr_'+proc]['dir'])

        except FileNotFoundError: print('Один из файлов не был найден')
        except KeyboardInterrupt: 
          print("Искусcтвенная остановка запуска"); time.sleep(0.5)
          return "artificial_stoppage"
       #except: print("[start] неизвестная ошибка"), time.sleep(3)
        
        time.sleep(1)
        #os.system(parameters['clearOutput'])
        return "completed"
    
    if de == '1': 
      _start = start()
      print(_start); time.sleep(0.5)
      input("< ")

    elif de == '2': return "settings"
    elif de == '3': return "sessions"
    elif de == ' ': return "exit"


def settings() :
    get_names = calculation_names()
    number_menu = 1
    is_v = "Вниз    "
    while True:
        #os.system(parameters['clearOutput'])
        n = [0, 1, 2, 3, 4]
        if number_menu == 2: n = [5, 6, 7, 8, 9]
        print("╭─────────────────── ╭────────────╮"); 
        print("│  Sahur System [1]  │  v - 1.2.  │"); 
        print("╰────────────────╮ ──╯ ────────── │"); 
        print("│   настройки    │ ", b_m[n[0]] +"│"); 
        print("│ ────────────── │ ", b_m[n[1]] +"│"); 
        print("│ [1] - Задержка │ ", b_m[n[2]] +"│"); 
        print("│ [2] - Конфиги  │ ", b_m[n[3]] +"│"); 
        print("│ [3] - "+is_v+" │ ", b_m[n[4]] +"│"); 
        print("╰─────────────── ╰────────────────╯"); time.sleep(0.5) 
        de = input('>> ')
        if de == '1':
          print("Задайте скорость задержки при запуске")
          try: delay = int(input(" > "))
          except ValueError: 
            print("цифры вводи нормальные да"); time.sleep(1)
            continue
          else: 
            programs['delay'] = delay
            update_write = write()
            print("Сохранено успешно!"); time.sleep(1)
            continue
        elif de == '2': return "configs"
        elif de == '3': 
          if is_v != "Вверх   ":
            number_menu = 2
            is_v = "Вверх   "
            continue
          else: 
            number_menu = 1
            is_v = "Вниз    "
            continue
        elif de == 'exit' or de == ' ': return "return_to_menu"
        else: continue

def configurations() :
  while True:
    is_v = "Вниз    "
    n = [0, 1, 2, 3, 4]
    try:
            proga = input('Номер проги: ')
            if proga == " ": return "return_to_settings"
            proga1 = 'pr_' + proga
            if proga1 in programs:
              if int(proga) in [5, 6, 7, 8, 9]:
                n = [5, 6, 7, 8, 9]; is_v = "Вверх   "

              os.system(parameters['clearOutput'])

              while True:
                get_names = calculation_names()
                
                b = b_m
                b[int(proga)-1] = HIGHLIGHT_COLOR+b_m[int(proga)-1]+GENERAL_COLOR

                print("╭─────────────────── ╭────────────╮"); 
                print("│  Sahur System [1]  │  v - 1.2.  │"); 
                print("╰────────────────╮ ──╯ ────────── │"); 
                print("│  конфигурация  │ ", b[n[0]] +  "│"); 
                print("│ ────────────── │ ", b[n[1]] +  "│");  
                print("│ [1] - Изменить │ ", b[n[2]] +  "│");  
                print("│ [2] - Удалить  │ ", b[n[3]] +  "│"); 
                print("│ [3] - "+is_v+" │ ", b[n[4]] +  "│");  
                print("╰─────────────── ╰────────────────╯"); time.sleep(0.5)  
                de = input('>> ')
                if de == '1': 
                  print(programs[proga1])
                  print('Доступные функции:\n [1] - os.startfile (запуск файла)\n [2] - pyperclip.copy (копирование в буфер)\n [3] - webbrowser.open (открытие ссылки)')
                  de = input('>> ')
                  if de == '1': 
                   print('выберете вариант запуска:\n[1] - subprocess.Popen\n[2] - subprocess.run (пока нету)\n[3] - os.startfile (пока нету)')
                   de = input('>> ') 
                   if de == '1':
                    par = 'subprocess.Popen'
                    print("[1] - Оставить старое")
                    name = str(input("Имя (не более 10 символов): "))
                    if name == '1': name = programs[proga1]['name']
                    if name == ' ': continue
                    if len(name) < 10:
                      print('поддерживается только запуск файлов, папки не запустим.')
                      print("[1] - Оставить старый")
                      dir = input("Путь: ") 
                      if dir == '1': dir = programs[proga1]['dir']
                      #dir_1 = dir.replace("\\", "/")
                      #print(dir_1), time.sleep(3)
                      try: # проверка процесса 
                          print(dir); time.sleep(1)
                          dir = dir.replace('\\', '/')
                          print(dir); time.sleep(1)
                          proc = subprocess.Popen([dir])
                          time.sleep(2)
                      except FileNotFoundError: 
                        print('Ошибка: Директория не найдена'); time.sleep(2)
                        continue
                      except PermissionError: 
                        print("Ошибка: Отказано в доступе"); time.sleep(2)
                      #except: print('неизвестная ошибка')
                      else: # остановка тестового процесса
                        #try:
                          print("попытка остановки тестового процесса"); time.sleep(0.5)
                          proc.terminate()
                          #os.system(f"taskkill /F /T /PID {proc.pid}") # резерв
                          while True:
                            try: delay = int(input("задержка: "))
                            except ValueError: print("цифры вводи нормальные да"); time.sleep(1)
                            else: break
                          print("Сохранено успешно")
                          programs[proga1]['par'] = par
                          programs[proga1]['name'] = name
                          programs[proga1]['dir'] = f"{par}(['{dir}'])"
                          programs[proga1]['delay'] = delay
                          update_write = write()
                          print(programs), time.sleep(1)
                          return "return_to_menu"
                    else: 
                      print('имя содержит более 10 символов!'); time.sleep(1)
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
                        except ValueError: print("цифры вводи нормальные да"); time.sleep(1)
                        else: break
                      programs[proga1]['par'] = par
                      programs[proga1]['name'] = name
                      programs[proga1]['dir'] = f"{par}('{text}')"
                      programs[proga1]['delay'] = delay
                      update_write = write()
                      print('сохранено успешно')
                      print(programs); time.sleep(1)
                      return "return_to_menu"
                    else: 
                      print('имя содержит более 10 символов!'); time.sleep(1)
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
                        print("тест"); time.sleep(0.5)
                        webbrowser.open_new_tab(url); time.sleep(2)
                        print("[1] - Работает, сохранить\n[2] - Не работает, изменить адрес")
                        pr = input(">> ")
                        if pr == "1": 
                          while True:
                            try: delay = int(input("задержка: "))
                            except ValueError: print("цифры вводи нормальные да"); time.sleep(1)
                            else: break
                          programs[proga1]['par'] = par
                          programs[proga1]['name'] = name
                          programs[proga1]['dir'] = f"{par}('{url}')"
                          programs[proga1]['delay'] = delay
                          update_write = write()
                          print('сохранено успешно'); time.sleep(0.5)
                          print(programs); time.sleep(0.5)
                          return "return_to_menu"
                        else: continue
                  
                  else: 
                    print("нормально вводи да"); time.sleep(1)
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
                    programs[proga1]['delay'] = 0
                    update_write = write()
                    print(programs); time.sleep(1)
                    continue
                  elif de == '2': continue

                elif de == '3': 
                  if is_v != "Вверх   ":
                      number_menu = 2; n = [5, 6, 7, 8, 9]; is_v = "Вверх   "
                  else: 
                      number_menu = 1; n = [0, 1, 2, 3, 4]; is_v = "Вниз    "
                  continue
                
                elif de == 'exit' or de == ' ': return "return_to_settings"
                else: continue
            else: 
              print("нету таких"); time.sleep(1)       
              continue
    except KeyboardInterrupt: break 
    #except: print("[configs] неизвестная ошибка")

def sessions() :
  try:
    while True:
      if len(programs['sessions']) < 1: print(" пусто"); time.sleep(0.5)
      else: 
        for sess in programs['sessions']:
          if len(sess) == 1: print('0'+sess,'-', programs['sessions'][sess]); time.sleep(0.05)
          else: print(sess, '-', programs['sessions'][sess]); time.sleep(0.05)
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
def main() :
  # get_start_info_notf = information_notification()
  while True:
    try:
      _crossPlatform = crossPlatform()
      _start_menu = start_menu()
      if _start_menu == "settings": 
          while True:
            _settings = settings()
            if _settings == "configs":
              _configs = configurations()
              if _configs == None: None
              elif _configs == "return_to_settings": continue
              elif _configs == 'return_to_menu': break
            elif _settings == "return_to_menu": break

      elif _start_menu == "sessions":
            _sessions = sessions()
            if _sessions == "completed": continue
            elif _sessions == "return_to_menu": continue 

      elif _start_menu == "exit":
          print("До свидания!"); time.sleep(0.3)
          safe_exit = _exit()
    except KeyboardInterrupt: break 
    #except: print("[main] неизвестная ошибка")

if __name__ == "__main__":
    _main = main()