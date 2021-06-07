import os
import requests
import shutil
import xlwt
import xlrd
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Tools:
    files = []

    def price_gen_decast(self):
        digit=int(input('Введите пороговый диапазон (например: 20000): '))
        f = open(os.path.dirname(os.path.abspath(__file__)) + '\\dekastprice.txt', encoding='UTF8')
        wr = open(os.path.dirname(os.path.abspath(__file__)) + '\\dekastGen.txt', 'w')
        print('Скрипт генерации цен начал работу')
        for line in f:
            name = line.replace("\n", "")
            print(name)
            if name != '' and name != 'по запросу':
                name = float(line.replace("\n", ""))
                if name < digit:
                    name += (name / 100) * 20
                elif name > digit:
                    name += (name / 100) * 25
                wr.write(str(round(name)) + '\n')
            else:
                wr.write('' + '\n')
        print('Закончил работу')

    def dublicate_images(self):
        data = xlrd.open_workbook(os.path.dirname(os.path.abspath(__file__)) + '\\дублив.xls')  # вставляем ФАЙЛ ГОТОВЫЙ ДЛЯ ИМПОРТА
        sheet = data.sheet_by_index(0)
        row_number = sheet.nrows
        cols_number = sheet.ncols
        ittn = 0
        groupFind = 1
        for row in range(1, row_number):
            print('откр')
            name = str(sheet.col(1)[row]).replace("text:", "").replace("'", "").replace('\r', '').replace("number:", "")
            group = str(sheet.col(11)[row]).replace("text:", "").replace("'", "").replace('\r', '').replace("number:",
                                                                                                            "")
            try:
                shutil.copy(
                    os.path.dirname(os.path.abspath(__file__)) + "\\изображенияБезДублей\\" + name,
                    os.path.dirname(os.path.abspath(__file__)) + "\\изображенияСДублями\\" + name)
                print(name + 'Нашелся и перемещен ---')
                groupFind = group
                finedFile = name
                ittn += 1
            except FileNotFoundError:
                print('nety')
            if group == groupFind:
                shutil.copy(
                    os.path.dirname(os.path.abspath(__file__)) + "\\изображенияБезДублей\\" + finedFile,
                    os.path.dirname(os.path.abspath(__file__)) + "\\изображенияСДублями\\" + name)
            else:
                groupOld = group
                print('Сменили группу')
        print('Найдено и перемещено:')
        print(ittn)
        pse = input()

    def chars_gen(self):
        book = xlwt.Workbook(encoding="utf-8")
        name = '\\Характеристики.xls'
        sheet1 = book.add_sheet("Sheet 1", cell_overwrite_ok=True)
        data = xlrd.open_workbook(
            os.path.dirname(os.path.abspath(__file__)) + name)
        string = ''
        sheet = data.sheet_by_index(0)
        row_number = sheet.nrows
        cols_number = sheet.ncols
        itt = 1
        iter = 0
        code = 1
        for row in range(1, row_number):
            while itt < cols_number:
                code = str(sheet.col(0)[row]).replace("text:", "").replace("'", "").replace('\r', '').replace("number:",
                                                                                                              "")
                char = str(sheet.col(itt)[0]).replace("text:", "").replace("'", "").replace('\r', '').replace("number:",
                                                                                                              "")
                value = str(sheet.col(itt)[row]).replace("text:", "").replace("'", "").replace('\r', '').replace(
                    "number:", "").replace(".0", "")
                itt += 1
                if value != 'empty:':
                    string += char + ' [' + value + ']; '
            itt = 0
            sheet1.write(iter, 0, code.replace(".0",""))
            sheet1.write(iter, 1, string.replace("empty:","Код:"))
            iter += 1
            book.save("chars.xls")
            string = ''
        pse = input()

    def spisok_v_papke(self):
        directory = input('Введите путь к искомой папке (пример D:\imgs): ')
        files = os.listdir(directory)
        print(files)
        i = 0
        while i < len(files):
            print(files[i])
            i += 1
        pse = input()

    def items_name(self):
        f = open('items.txt', encoding='UTF8')
        s = open('DoneItems.txt', "w")
        lineIter = 1
        for line in f:
            name = line.replace("\n", "")
            if 'Кран' in name:
                if 'Латунь' in name:
                    s.write('Краны латунные')
                else:
                    if 'Шаровой' in name:
                        s.write('Краны шаровые')
                    else:
                        s.write('Краны')
            else:
                if 'Воздухоотводчик' in name:
                    if 'Автоматический' in name:
                        if 'Сталь':
                            s.write('Воздухоотводчики стальные автоматические')
                        if 'Латунь':
                            s.write('Воздухоотводчики латунные автоматические')
                    else:
                        if 'Ручной':
                            if 'Сталь':
                                s.write('Воздухоотводчики стальные ручные')
                            if 'Латунь':
                                s.write('Воздухоотводчики латунные ручные')
                if 'Вантуз' in name:
                    if 'Автоматический' in name:
                        if 'Чугун' in name:
                            s.write('Вантузы автоматические чугун')
                        if 'Сталь' in name:
                            s.write('Вантузы автоматические сталь')
                    else:
                        s.write('Вантузы')
                if 'Сепаратор воздуха' in name:
                    if 'Латунь' in name:
                        if 'Danfoss' in name:
                            s.write('Сепаратор воздуха латунь Danfoss')
                        if 'Exvoid' in name:
                            s.write('Сепаратор воздуха латунь Exvoid')
                    if 'Сталь' in name:
                        if 'Danfoss' in name:
                            s.write('Сепаратор воздуха сталь Danfoss')
                        if 'Exvoid' in name:
                            s.write('Сепаратор воздуха сталь Exvoid')
                if 'Ключ' in name:
                    s.write('Ключи')
                if 'Клапан' in name:
                    if 'Китай':
                        s.write('Клапаны Китай')
                    if 'Италия':
                        s.write('Клапаны Италия')
                if 'Задвижка' in name:
                    if 'Чугун':
                        s.write('Задвижка чугунная')
                    if 'Сталь':
                        s.write('Клапаны стальная')
            s.write('\n')
            lineIter += 1
        print('[УСПЕШНО] Программа завершена')
        pse = input()

    def images_spisok_cat(self):
        name = 'spisokdublei.txt'
        name2 = 'spisokdubleiout.txt'
        f = open(name, encoding='UTF8')
        directory = os.path.dirname(os.path.abspath(__file__)) + "\\изображенияСДублями"
        files = os.listdir(directory)
        mas2 = []
        s = open(name2, "w")
        for line in f:
            name = line.replace("\n", "")
            if name not in files:
                print('Файл, который есть в списке, но его нет в папке: ' + name)
                s.write('\n' + name)

    def images_directory(self):
        dir1=''
        dir2=''
        while os.path.exists(dir1)== False:
            dir1=input('Укажите путь к директории со всеми изображениями в формате D:\директория1 ')
            if os.path.exists(dir1) == False:
                print('Директория 1 не существует!')
            else:
                print('Директория существует')
        while os.path.exists(dir2)== False:
            dir2=input('Укажите путь к директории с неполным количеством в формате D:\директория2 ')
            if os.path.exists(dir2) == False:
                print('Директория 2 не существует!')
            else:
                print('Директория существует')
        files1 = os.listdir(dir1)
        files2 = os.listdir(dir2)
        name2 = 'spisokdel.txt'
        s = open(name2, "w")
        i=0
        while i < len(files1):
            if files1[i] not in files2:
                print('Изображение '+ files1[i]+ ' не найдено в основной директории')
                s.write('\n' + files1[i])
            i+=1

    def images_copy_in_dir(self):
        dir1=''
        dir2=''
        file=''
        while os.path.exists(dir1)== False:
            dir1=input('Укажите путь к директории откуда перенести изображения в формате D:\директория1 ')
            if os.path.exists(dir1) == False:
                print('Директория 1 не существует!')
            else:
                print('Директория существует')
        while os.path.exists(dir2)== False:
            dir2=input('Укажите путь к директории куда перенести изображения в формате D:\директория2 ')
            if os.path.exists(dir2) == False:
                print('Директория 2 не существует!')
            else:
                print('Директория существует')
        while os.path.isfile(file)== False:
            file=input('Укажите путь к файлу содержащему список в формате D:\директория1\spisok1.txt ')
            if os.path.exists(file) == False:
                print('Файл не существует!')
            else:
                print('Файл существует')
        f = open(file, encoding='UTF8')
        for line in f:
            name = line.replace("\n", "")
            print(name)
            if name != '':
                print(dir1+'\\'+name)
                print(' Перемещен в ')
                print(dir2+'\\'+name)
                shutil.copyfile(dir1+'\\'+name, dir2+'\\'+name)
