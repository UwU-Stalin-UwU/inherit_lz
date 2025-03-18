#UwU-Stalin-UwU
#Second lz of classes
from os.path import isdir
import os

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def get_info(self):
        print('Название книги: ', self.title)
        print('Автор книги: ', self.author)
        print('Год выпуска книги: ', self.year)
    
    def is_actual(self):
        if 2025 - self.year <= 5 :
            print("Книга свежая")
        else:
            print("Книга старая")

    def __del__(self):
        pass


class EBook(Book):
    def __init__(self, title, author, year, file_size, format, links):
        super().__init__(title, author, year)
        self.file_size = file_size
        self.format = format
        self.links = links
    
    def get_info(self):
        super().get_info()
        print("Размер книги: ", self.file_size)
        print("Формат файла с книгой: ", self.format)
    
    def is_actual(self):
        super().is_actual()
    
    def is_free(self):
        k=0
        ran = len(self.title)
        for i in range(0, ran-4):
            if self.title[i] + self.title[i+1] + self.title[i+2] + self.title[i+3] == "free":
                k+=1
        if k==0:
            print("Книга платная")
        else:
            print("Книга бесплатная")


    def is_available(self) :
        n=0
        for i in self.links:
            if self.title == i:
                n+=1
        if n == 1:
            print("Книга доступна")
            self.is_free()
        else:
            print("Книга недоступна")


def parse_folder(path):
    files = []
    for file in os.listdir(path):
        if isdir(path + '/' + file):
            files.extend(parse_folder(path + '/' + file))
        else:
            files.append(file)
    
    return files

def program():
    user_choose = int(input("Если вы работаете с книгами введите 1, если работаете с электронными введите 2: "))
    if user_choose == 1:
        title = input('Введите название книги: ')
        author = input('Введите автора книги: ')
        year = int(input('Введите год выпуска книги: '))
        book1 = Book(title, author, year)
        book1.get_info()
        book1.is_actual()
    if user_choose == 2:
        title = input('Введите название книги: ')
        author = input('Введите автора книги: ')
        year = int(input('Введите год выпуска книги: '))
        size = int(input('Введите размер книги: '))
        format = input('Введите формат файла с книгой: ')
        links = parse_folder("books")
        # for i in links:
        #     print(i)
        book1 = EBook(title, author, year, size, format, links)
        book1.get_info()
        book1.is_actual()
        book1.is_available()

def main():
    program()

if __name__=="__main__":
    main()