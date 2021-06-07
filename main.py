from ToolsMode import Tools
import os


class ToolsMain():
    r1 = Tools()

    def __init__(self):
        self.menu_change()

    def menu_change(self):
        os.system("cls")
        print('█░░░█ ▄▀▀▄ █▀▄ █░█ . ▀█▀ ▄▀▀▄ ▄▀▀▄ █░░ ▄▀▀')
        print('█▄█▄█ █░░█ █▀▄ █▀▄ . ░█░ █░░█ █░░█ █░░ ░▀▄')
        print('▀▀░▀▀ ░▀▀░ ▀░▀ ▀░▀ . ░▀░ ░▀▀░ ░▀▀░ ▀▀▀ ▀▀░')
        print('==========МЕНЮ НАВИГАЦИИ ПО ИНСТРУМЕНТАМ============')
        print('1. Регулирование цен Dekast')
        print('2. Дублирование изображений')
        print('3. Генерация характеристик для CS CART')
        print('4. Показать список изображений в папке')
        print('5. Распределение товарных категорий')
        print('6. Сравнение изображений в папке и списке')
        print('7. Найти недостающие изображения сравнивая две папки')
        print('8. Переместить изображения по списку в txt файле из папки в папку')
        print('9. Меню помощи')
        i=False
        while i != True:
            change = int(input('Введите цифру(пункт меню) для запуска нужного процесса: '))
            if change == 1:
                os.system("cls")
                print("В корневой папке лежит файл с актуальными ценами для обработки - dekastprice.txt ")
                print('Подождите, идет загрузка...')
                self.price_gen_decast_start()
                i=True
            elif change == 2:
                os.system("cls")
                print('В коренной папке внутри каталога "изображенияБезДублей" находятся изображения для дублей ')
                print('В корневой папке файл - дублив.xlsx - данные о дублирующихся изображениях')
                print('Подождите, идет загрузка...')
                self.dublicate_images_start()
                i=True
            elif change ==3:
                os.system("cls")
                print('В корневой папке файл с характеристиками - Характеристики.xls')
                print('Сгенерированные характеристики - chars.xls')
                print('Подождите, идет загрузка...')
                self.chars_gen_start()
                i=True
            elif change ==4:
                os.system("cls")
                print('Введите путь к папке с изображениями')
                print('Подождите, идет загрузка...')
                self.spisok_v_papke_start()
                i=True
            elif change ==5:
                os.system("cls")
                print('Распределение товарных категорий. Файл - items.txt')
                print('Подождите, идет загрузка...')
                self.items_name_start()
                i=True
            elif change ==6:
                os.system("cls")
                print('Сравнение изображений в папке и списке. Файл со списком для сравнения - spisokdublei.txt')
                print('Выходной файл spisokdubleiout.txt')
                print('Подождите, идет загрузка...')
                self.images_spisok_cat_start()
                i=True
            elif change ==7:
                os.system("cls")
                print('Найти недостающие изображения в двух директориях')
                print('Подождите, идет загрузка...')
                self.images_directory_start()
                i=True
            elif change ==8:
                os.system("cls")
                print('Переместить изображения по списку в txt файле из папки в папку')
                print('Подождите, идет загрузка...')
                self.images_copy_in_dir_start()
                i=True
            elif change ==9:
                os.system("cls")
                self.help_menu()
                i=True
            else:

                print('ОШИБКА! Введите цифру, соответствующую пункту меню!')

    def price_gen_decast_start(self):
        self.r1.price_gen_decast()

    def dublicate_images_start(self):
        self.r1.dublicate_images()

    def chars_gen_start(self):
        self.r1.chars_gen()

    def spisok_v_papke_start(self):
        self.r1.spisok_v_papke()

    def items_name_start(self):
        self.r1.items_name()

    def images_spisok_cat_start(self):
        self.r1.images_spisok_cat()

    def images_directory_start(self):
        self.r1.images_directory()

    def images_copy_in_dir_start(self):
        self.r1.images_copy_in_dir()

    def help_menu(self):
        print('[̲̅H̲̅][̲̅E̲̅][̲̅L̲̅][̲̅P̲̅]')
        print('1. Регулирование цен Dekast')
        print('2. Дублирование изображений')
        print('3. Генерация характеристик для CS CART')
        print('4. Показать список изображений в папке')
        print('5. Распределение товарных категорий')
        print('6. Сравнение изображений в папке и списке')
        print('7. Найти недостающие изображения сравнивая две папки')
        print('8. Переместить изображения по списку в txt файле из папки в папку')
        i = False
        change=''
        while change != 'exit':
            change = str(input('Введите цифру(пункт меню) для получения помощи по нужному процессу: '))
            if change == '1':
                os.system("cls")
                print('Данный скрипт формирует цены для магазина')
                print('добавляя к ним наценку, которую нужно указать введя число с клавиатуры при появлении')
                print('надписи "Введите пороговый диапазон:"')
                print("Файл со списком артикулов для обновления находится в корневой папке 'dekastprice.txt' ")
                print('После генерируется файл dekastGen.txt')
                print('Выйти в главное меню: exit')
            elif change == '2':
                os.system("cls")
                print('В коренной папке внутри каталога "изображенияБезДублей" находятся изображения для дублей ')
                print('В корневой папке файл - дублив.xlsx - данные о дублирующихся изображениях')
                print('В корнейвой папке так же есть каталог "изображенияСДублями" туда по окончании')
                print('Сохраняются дублированные изображения')
                print('Выйти в главное меню: exit')
            elif change == '3':
                os.system("cls")
                print('Генерация характеристик для CS CART')
                print('Данный скрипт генерирует характеристики для поля товара Features ')
                print('в CMS CS CART.В корневой папке есть пример - файл с характеристиками - Характеристики.xls ')
                print('Сгенерированные характеристики сохраняются в chars.xls')
                print('Выйти в главное меню: exit')
            elif change == '4':
                os.system("cls")
                print('Данный скрипт отображает количество изображений в папке,')
                print('использование - просмотр конечного списка файлов для формирования прайса ')
                print('Выйти в главное меню: exit')
            elif change =='5':
                os.system("cls")
                print('Информация о функции программы: Данный скрипт распределяет товары по категориям,')
                print('В результате получаем txt файл с категорией товара, находящейся на той же строке')
                print('что и товар в искомом файле')
                print('Выйти в главное меню: exit')
            elif change =='6':
                os.system("cls")
                print('Информация о функции программы: Данный скрипт сравнивает количество изображений,')
                print('в папке \изображенияСДублями с количеством изображений перечисленным в списке')
                print('spisokdublei.txt - лежит в корневом катлоге программы. Результаты выводятся на экран')
                print('и сохраняются в spisokdubleiout.txt')
                print('Выйти в главное меню: exit')
            elif change =='7':
                os.system("cls")
                print('Информация о функции программы: Найти недостающие изображения в двух директориях ')
                print('Сначала нужно ввести директорию со всеми изображениями, затем директорию с неполным количеством')
                print('После выполнения программы будет создан файл - spisokdel.txt в котором перечислен')
                print('список файлов, которые находятся в первой директории, но не находятся во второй')
                print('Выйти в главное меню: exit')
            elif change =='8':
                os.system("cls")
                print('Информация о функции программы: Переместить изображения по списку в txt файле из папки в папку ')
                print('Сначала нужно ввести путь к директории со всеми изображениями, затем путь')
                print('к директории, в которую переместить изображения. Затем файл - список, его можно получить')
                print('путем выполнения функции 7 (Найти недостающие изображения сравнивая две папки)')
                print('После выполнения скрипта во второй введенной директории появятся')
                print('изображения из списка в txt файле.')
                print('Выйти в главное меню: exit')
        self.menu_change()


app = ToolsMain()


