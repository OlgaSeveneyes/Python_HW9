def read_file_string(lst):
    with open ('Phonebook_string.csv', 'r', encoding='utf-8', newline='') as file:
        lst = file.read()
        some_list = lst.replace(','," ")
        return(some_list)
        
def search_string(surname):
    surname = input('Введите фамилию: ')
    file = read_file_string(surname)
    new_file = file.split()
    if surname in new_file:
        for i in range(len(new_file)):
            if surname == new_file[i]:
                print(new_file [i], new_file[i+1], new_file[i+2], new_file[i+3])
    else:
       print('Контакт не найден') 
