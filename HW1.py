import re
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not re.match(r'^\d{10}$', value):
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        new_phone_obj = Phone(new_phone)  
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone_obj.value

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

# Examples of usage
book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

print("All records in the book:")
for record in book.data.values():
    print(record)

john = book.find("John")
if john:
    john.edit_phone("1234567890", "1112223333")
    print(f"\nEdited record for John:\n{john}")

    found_phone = john.find_phone("5555555555")
    if found_phone:
        print(f"Found phone in John's record: {found_phone.value}")
    else:
        print("Phone not found in John's record.")

book.delete("Jane")
print("\nAll records in the book after deleting Jane's record:")
for record in book.data.values():
    print(record)
