import json 
import uuid
import unicodedata

class Note:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        
def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump([note.__dict__ for note in notes], file, indent=4, separators=(',', ': '))

def read_notes():
    
    try:
        with open('notes.json', 'r') as file:
            data = json.load(file)
            
            notes = [Note(**note) for note in data]
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        notes = []
    return notes 

def add_note():
    
    title = input('Введите заголовок заметки: ')
    
    body = input('Введите тело заметки: ')
    
    id = str(uuid.uuid4())
    
    note = Note(id, title, body)  
    
    notes.append(note)
    
    save_notes(notes)
    
def edit_note():
    
    id = input('Введите идентификатор заметки для редактирования: ')
    
    note = next((note for note in notes if note.id == id), None)
    
    if note:
        print(f'Редактирование заметки: {note.title}')
        title = input('Введите новый заголовок заметки: ')
        body = input('Введите новый текст заметки: ')
        
        if title:
            note.title = title
        if body:
            note.body = body
            
        save_notes(notes)
    else: 
        print('Заметка не найдена!')
        
def delete_note():
    id = input('Введите идентификатор заметки для удаления: ')
    
    note = next((note for note in notes if note.id == id), None)
    
    if note:
        notes.remove(note)
        
        save_notes(notes)
        
    else:
        print('Заметка не найдена!')
        
def view_notes():
    filter_notes = notes
    
    if filter_notes:
        for note in filter_notes:
            print(f'{note.id} {note.title} {note.body}')
    else:
        print('Нет заметок для отображения')
        
def main():
    
    global notes
    
    notes = read_notes()
    
    while True:
        
        print('\n 1. Показать список заметок \n 2. Добавить заметку \n 3. Редактировать заметку \n 4. Удалить заметку \n 5. Выход \n')
        
        choice = input('Выберите действие: ')
        
        if choice == '1':
            view_notes()
        
        elif choice == '2':
            add_note()
        
        elif choice == '3':
            edit_note()
        
        elif choice == '4':
            delete_note()
            
        elif choice == '5':
            break
        else:
            print('Недопустимый выбор!')
            
main()
    