import json
import os.path
from datetime import datetime


class Note:
    def __init__(self, id, title, body, creation_time):
        self.id = id
        self.title = title
        self.body = body
        self.creation_time = creation_time
        self.last_modified_time = creation_time

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "creation_time": str(self.creation_time),
            "last_modified_time": str(self.last_modified_time)
        }

    @classmethod
    def from_dict(cls, d):
        return cls(id=d["id"], title=d["title"], body=d["body"],
                   creation_time=datetime.fromisoformat(d["creation_time"]))

    def __repr__(self):
        return f"<Note {self.title} ({self.id})>"

def load_notes():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as f:
            data = json.load(f)
    else:
        data = {"notes": []}
    return data

def save_notes(data):
    with open("notes.json", "w") as f:
        json.dump(data, f, indent=4)

def create_note():
    title = input("Введите название заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.now()
    id = len(data["notes"]) +1
    note = Note(id, title, body, timestamp)
    data["notes"].append(note.to_dict())
    save_notes(data)
    print(f"Зематка '{title}' сохранена.")

def read_note():
    ident = input("Введите номер или название заметки: ")
    for note_dict in data["notes"]:
        if str(note_dict["id"]) == ident or note_dict["title"] == ident:
            note = Note.from_dict(note_dict)
            print(note.title)
            print(note.body)
            print(note.creation_time)
            print(note.last_modified_time)
            return
    print(f" Заметка '{ident}' не найдена.")


def update_note():
    ident = input("Введите номер или название заметки: ")
    for note_dict in data["notes"]:
        if str(note_dict["id"]) == ident or note_dict["title"] == ident:
            title = input(f"Введите новое название заметки ({note_dict['title']}): ")
            body = input(f"Введите новый текст заметки ({note_dict['body']}): ")
            note_dict["title"] = title or note_dict["title"]
            note_dict["body"] = body or note_dict["body"]
            note_dict["last_modified_time"] = str(datetime.now())
            save_notes(data)
            print(f"Заметка '{note_dict['title']}' обновлена.")
            return
        print(f"Заметка '{ident}' не найдена.")

def delete_note():
    ident = input("Введите номер или название заметки: ")
    for note_dict in data["notes"]:
        if str(note_dict["id"]) == ident or note_dict["title"] == ident:
            data["notes"].remove(note_dict)
            save_notes(data)
            print(f" Заметка '{note_dict['title']}' удалена.")
            return
    print(f" Заметка '{note_dict['title']}' не найдена.")

def list_notes():
    for note_dict in data["notes"]:
        note = Note.from_dict(note_dict)
        print(note.title)
        print(note.body)
        print(note.creation_time)
        print(note.last_modified_time)
        print()


def main():
    global data
    data = load_notes()

    while True:
        action = input("Введите 'n' для создания новой заметки, 'u' для редактирования"
                       "'r' для просмотра, 'd' для удаления,"
                       "'l' для просмотра всех заметок, 'q' для выхода:  ")
        if action == "n": create_note()
        elif action == "r": read_note()
        elif action == "u": update_note()
        elif action == "d": delete_note()
        elif action == "l": list_notes()
        elif action == "q": break
        else: print("Незнакомая буква.")


if __name__ == "__main__":
    main()












