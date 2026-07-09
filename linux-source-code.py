# sahur system - [1] / v-1.1 / 08.07.2026

#    \____
#   sa\____\
#    hur\__\
#         \

import os
import time 
import datetime
import subprocess
import pyperclip
from colorama import init, Fore, Back, Style

os.system('mode con: cols=60 lines=17')

print(Fore.GREEN+"sahur system - [1] / v-1.1 / 08.07.2026"+Style.RESET_ALL), time.sleep(1)
print(Fore.BLUE,"[1]-System : Запуск \n"), time.sleep(0.5)
print(" [2]-System : Проверка систем (1) "), time.sleep(0.3)
print('  расположение:', os.getcwd()), time.sleep(0.3)
print(" [3]-System : Проверка систем (2) \n"), time.sleep(1)
os.system('clear') 


print(Fore.MAGENTA,'')
try:
  log = open('sessions.txt','r')
  last_log = log.read()
  print("последняя сессия :", last_log)
  log = open('sessions.txt','w')
  a = str(str(datetime.datetime.now())[:-10])
  log.write(a)
  log = open('sessions.txt','r')
  last_log = log.read()
  print("текущая сессия   :", last_log), time.sleep(2)
  log.close()
except FileNotFoundError: print('ошибка: файл "sessions.txt" не найден.')

print(Fore.GREEN,'')

programs = {
 'pr_1' : {'num':'1', 'par': 'none', 'name':'none', 'dir': 'none'},
 'pr_2' : {'num':'2', 'par': 'none', 'name':'none', 'dir': 'none'},
 'pr_3' : {'num':'3', 'par': 'none', 'name':'none', 'dir': 'none'},
 'pr_4' : {'num':'4', 'par': 'none', 'name':'none', 'dir': 'none'},
 'pr_5' : {'num':'5', 'par': 'none', 'name':'none', 'dir': 'none'},
}

try:
  file = open('programs.txt', 'r')
except FileNotFoundError: print('ошибка: файл "programs.txt" не найден.')

else:
  a = file.readline()
  c1 = file.readline()
  c2 = file.readline()
  c3 = file.readline()
  c4 = file.readline()
  c5 = file.readline()
  file.close()

  a1 = c1.split(',')
  a2 = c2.split(',')
  a3 = c3.split(',')
  a4 = c4.split(',')
  a5 = c5.split(',')

  programs['pr_1']['par'] = a1[2]
  programs['pr_1']['name'] = a1[3]
  programs['pr_1']['dir'] = a1[4].replace("\n", "")

  programs['pr_2']['par'] = a2[2]
  programs['pr_2']['name'] = a2[3]
  programs['pr_2']['dir'] = a2[4].replace("\n", "")

  programs['pr_3']['par'] = a3[2]
  programs['pr_3']['name'] = a3[3]
  programs['pr_3']['dir'] = a3[4].replace("\n", "")

  programs['pr_4']['par'] = a4[2]
  programs['pr_4']['name'] = a4[3]
  programs['pr_4']['dir'] = a4[4].replace("\n", "")

  programs['pr_5']['par'] = a5[2]
  programs['pr_5']['name'] = a5[3]
  programs['pr_5']['dir'] = a5[4].replace("\n", "")

  print('чтение завершено'), time.sleep(0.3)
os.system('clear')


print("Добро пожаловать!"), time.sleep(1)
def menu():
  while True:
    # посчёт символов
    a1 = len(str(programs['pr_1']['num']+' '+programs['pr_1']['name']))
    a2 = len(programs['pr_2']['num']+' '+programs['pr_2']['name'])
    a3 = len(programs['pr_3']['num']+' '+programs['pr_3']['name'])
    a4 = len(programs['pr_4']['num']+' '+programs['pr_4']['name'])
    a5 = len(programs['pr_5']['num']+' '+programs['pr_5']['name'])
    # подсчёт отступов
    a_1 = ' ' * (14 - a1)
    a_2 = ' ' * (14 - a2)
    a_3 = ' ' * (14 - a3)
    a_4 = ' ' * (14 - a4)
    a_5 = ' ' * (14 - a5)
    # сборка имён
    b_1 = programs['pr_1']['num']+' '+programs['pr_1']['name']+a_1
    b_2 = programs['pr_2']['num']+' '+programs['pr_2']['name']+a_2
    b_3 = programs['pr_3']['num']+' '+programs['pr_3']['name']+a_3
    b_4 = programs['pr_4']['num']+' '+programs['pr_4']['name']+a_4
    b_5 = programs['pr_5']['num']+' '+programs['pr_5']['name']+a_5

    # основное меню
    print("╭─────────────────── ╭────────────╮"), time.sleep(0.1)
    print("│ Sahur System - [1] │  v - 1.1.  │"), time.sleep(0.1)
    print("╰────────────────╮ ──╯ ────────── │"), time.sleep(0.1)
    print("│  главное меню  │ ", b_1 +      "│"), time.sleep(0.1)
    print("│ ────────────── │ ", b_2 +      "│"), time.sleep(0.1)
    print("│ [1] - Старт    │ ", b_3 +      "│"), time.sleep(0.1)
    print("│ [2] - Смена    │ ", b_4 +      "│"), time.sleep(0.1)
    print("│ [3] - Выйти    │ ", b_5 +      "│"), time.sleep(0.1)
    print("╰─────────────── ╰────────────────╯"), time.sleep(0.5) 
    de = input('>> ')
    if de == '1':
     # def start():
        try:
          print('Запуск'), time.sleep(1), os.system('clear')
          if programs['pr_1']['name'] == 'none':
            print('запуск (1) небудем это хапускать'), time.sleep(1)
          else: 
            print("запуск (1)"), time.sleep(1)
            exec(programs['pr_1']['par']+'("'+programs['pr_1']['dir']+'")')

          if programs['pr_2']['name'] == 'none':
            print('запуск (2) небудем это хапускать'), time.sleep(1)
          else: 
            print("запуск (2)"), time.sleep(1)
            exec(programs['pr_2']['par']+'("'+programs['pr_2']['dir']+'")')
            
          if programs['pr_3']['name'] == 'none':
            print('запуск (3) небудем это хапускать'), time.sleep(1)
          else: 
            print("запуск (3)"), time.sleep(1)
            exec(programs['pr_3']['par']+'("'+programs['pr_3']['dir']+'")')

          if programs['pr_4']['name'] == 'none':
            print('запуск (4) небудем это хапускать'), time.sleep(1)
          else: 
            print("запуск (4)"), time.sleep(1)
            exec(programs['pr_4']['par']+'("'+programs['pr_4']['dir']+'")')

          if programs['pr_5']['name'] == 'none':
            print('запуск (5) небудем это хапускать'), time.sleep(1)
          else: 
            print("запуск (5)"), time.sleep(1)
            exec(programs['pr_5']['par']+'("'+programs['pr_5']['dir']+'")')
        
        except FileNotFoundError: print('Один из файлов не был найден')
        except: print("Неизвестная ошибка"), time.sleep(3)
        
        time.sleep(1)
        #os.system('clear')
        continue
    
    elif de == '2':
      proga = str(input('Номер проги: '))
      os.system('clear')
      proga1 = 'pr_' + proga
      if proga1 in programs:
        while True:

          if proga1 == 'pr_1':
            b_01 = Fore.YELLOW + b_1 + Fore.GREEN
            b_02 = b_2
            b_03 = b_3
            b_04 = b_4
            b_05 = b_5
          if proga1 == 'pr_2':
            b_01 = b_1
            b_02 = Fore.YELLOW + b_2 + Fore.GREEN
            b_03 = b_3
            b_04 = b_4
            b_05 = b_5
          if proga1 == 'pr_3':
            b_01 = b_1 
            b_02 = b_2
            b_03 = Fore.YELLOW + b_3 + Fore.GREEN
            b_04 = b_4
            b_05 = b_5
          if proga1 == 'pr_4':
            b_01 = b_1 
            b_02 = b_2
            b_03 = b_3
            b_04 = Fore.YELLOW + b_4 + Fore.GREEN
            b_05 = b_5
          if proga1 == 'pr_5':
            b_01 = b_1 
            b_02 = b_2
            b_03 = b_3
            b_04 = b_4
            b_05 = Fore.YELLOW + b_5 + Fore.GREEN

          print("╭─────────────────── ╭────────────╮"), 
          print("│ Sahur System - [1] │  v - 1.1.  │"), 
          print("╰────────────────╮ ──╯ ────────── │"), 
          print("│  главное меню  │ ", b_01 +     "│" ),
          print("│ ────────────── │ ", b_02 +     "│" ),  
          print("│ [1] - Изменить │ ", b_03 +     "│" ),  
          print("│ [2] - Удалить  │ ", b_04 +     "│" ), 
          print("│ [3] - Назад    │ ", b_05 +     "│" ),  
          print("╰─────────────── ╰────────────────╯"), time.sleep(0.5)  
          de = input('>> ')

          if de == '1': 
            print('Доступные функции:\n [1] - subprocess.Popen (запуск файла)\n [2] - pyperclip.copy (копирование в буфер)'), time.sleep(0.5)
            de = input('>> ')
            if de == '1': 
              par = 'subprocess.Popen'
              name = str(input("Имя (не более 10 символов): "))
              if len(name) < 10:
                print('Поддерживается только запуск файлов, папки не запустим.')
                dir = input("Путь: ") 
                dir_1 = dir.replace("\\", "/")
                print(dir_1), time.sleep(3)
                try: # проверка процесса 
                  process = subprocess.Popen([dir_1])
                  process.kill()
                  process.wait()
                except FileNotFoundError: 
                  print('Программа не найдена'), time.sleep(1)
                  continue
                #except: print('неизвестная ошибка')
                else:
                  #except: 
                    #print("кажется, вы ввели неправильный путь к файлу. (папки не поддерживаются)"), time.sleep(2)
                    #continue
                  #else: 
                    print("Сохранено успешно")
                    programs[proga1]['par'] = par
                    programs[proga1]['name'] = name
                    programs[proga1]['dir'] = dir_1
                    print(programs), time.sleep(1)
                    continue
              else: 
                print('имя содержит более 10 символов!'), time.sleep(1)
                continue

            elif de == '2':
              par = 'pyperclip.copy'
              name = str(input("Имя (не более 10 символов): "))
              if len(name) < 10:
                text = str(input("Текст: "))
                programs[proga1]['par'] = par
                programs[proga1]['name'] = name
                programs[proga1]['dir'] = text
                print(programs)
                time.sleep(1)
                continue
              else: 
                print('имя содержит более 10 символов!'), time.sleep(1)
                continue
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
              print(programs), time.sleep(1)
              continue
            elif de == '2':
              continue

          elif de == '3': 
             return de
      else: 
        print("нету таких"), time.sleep(1)       
        os.system('clear')
        continue

    elif de == '3':
        print("До свидания!"), time.sleep(1)
        break
    else: 
       os.system('clear')
       continue



# общий алгоритм процессов
while True:
  a = menu()
  if a == '3': 
    os.system('clear')
    continue
  break




b_1 = str('pr_1'+','+'1'+','+programs['pr_1']['par']+','+programs['pr_1']['name']+','+programs['pr_1']['dir'])
b_2 = str('pr_2'+','+'2'+','+programs['pr_2']['par']+','+programs['pr_2']['name']+','+programs['pr_2']['dir'])
b_3 = str('pr_3'+','+'3'+','+programs['pr_3']['par']+','+programs['pr_3']['name']+','+programs['pr_3']['dir'])
b_4 = str('pr_4'+','+'4'+','+programs['pr_4']['par']+','+programs['pr_4']['name']+','+programs['pr_4']['dir'])
b_5 = str('pr_5'+','+'5'+','+programs['pr_5']['par']+','+programs['pr_5']['name']+','+programs['pr_5']['dir'])

try:
  file = open('programs.txt', 'w') # запись обновленных программ 
  file.write('\n'+b_1)
  file.write('\n'+b_2)
  file.write('\n'+b_3)
  file.write('\n'+b_4)
  file.write('\n'+b_5)
  file.close()
except FileNotFoundError: print('ошибка: файл "programs.txt" не найден.')

try:
  log = open('sessions.txt','w') # запись времени последнего сеанса
  a = str(str(datetime.datetime.now())[:-10])
  log.write(a)
  log.close()
except FileNotFoundError: print('ошибка: файл "sessions.txt" не найден.')

print(Fore.BLUE, " [ℹ]-System : stop ", Style.RESET_ALL), time.sleep(1)
