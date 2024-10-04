from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

send_contact = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kontakt yuboish ☎️", request_contact=True)]
    ],
    resize_keyboard=True,
)

location_contact = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📍 joylashuvni yuboish", request_location=True)]
    ],
    resize_keyboard=True,
)


menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💻 Laptop"),KeyboardButton(text="📱 Phones")],
        [KeyboardButton(text="💁🏻‍♂️ About us"),KeyboardButton(text="📍 Location")],
        [KeyboardButton(text="☎️ Contact admin")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Tugmalardan birini tanlang ..."
)

computers = [
    "Mackbook",
    "Lenovo",
    "HP",
    "ASUS",
    "Victus",
    "ACER",
    "Samsung",
]

computer_button = ReplyKeyboardBuilder()

for computer in computers:
    computer_button.add(KeyboardButton(text=computer))

computer_button.add(KeyboardButton(text="Orqaga qaytish 🔙"))

computer_button.adjust(2,repeat=True)

computer_button = computer_button.as_markup(
    resize_keyboard=True,
    input_field_placeholder="Choise computer..."
)



phones = [
    "samsung",
    "Redmi",
    "Iphone",
    "Honor",
    "Infinix"
]


phones_button = ReplyKeyboardBuilder()

for phone in phones:
    phones_button.add(KeyboardButton(text=phone))

phones_button.add(KeyboardButton(text="Orqaga qaytish 🔙"))

phones_button.adjust(2,repeat=True)

phones_button = phones_button.as_markup(
    resize_keyboard=True,
    input_field_placeholder="Choise phone..."
)

# back = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Orqaga qaytish 🔙", request_location=True)]
#     ],
#     resize_keyboard=True,
# )