# Задание 1
import random

result = random.randint(1, 100)
print("Выпало:", result)

if result <= 5:
    print("Результат крутки: SSR (ГОДЖО!!)")
elif result <= 30:
    print("Результат крутки: SR (Мегуми)")
else:
    print("Результат крутки: R (обычный талисман)")

for spin in range(2, 5):
    value = random.randint(1, 100)

    if value <= 5:
        print("Крутка ", spin, ": SSR (ГОДЖО!!)", sep="")
    elif value <= 30:
        print("Крутка ", spin, ": SR (Мегуми)", sep="")
    else:
        print("Крутка ", spin, ": R (обычный талисман)", sep="")


# Задание 2
try:
    first_number = int(input("Первое число? "))
    second_number = int(input("Второе число? "))

    quotient = first_number / second_number
    rounded_result = round(quotient, 2)

    print("Частное:", rounded_result)

except ValueError:
    print("Это не число! Вводи цифрами.")

except ZeroDivisionError:
    print("На ноль делить нельзя!")


# Задание 3
import random

character_classes = ["маг", "танк", "лучник", "хилер"]

selected_class = random.choice(character_classes)
print("Твоя роль:", selected_class)

mission_count = random.randint(1, 5)

print("Сегодня тебя ждёт(ут)", mission_count, "миссии(й)")


# Задание 4
import math

try:
    magic_number = float(input("Введи магическое число? "))

    rounded_down = math.floor(magic_number)
    print("Округление вниз:", rounded_down)

    rounded_up = math.ceil(magic_number)
    print("Округление вверх:", rounded_up)

    absolute_value = abs(magic_number)
    square_root = math.sqrt(absolute_value)
    rounded_root = round(square_root, 2)

    print("Корень из модуля:", rounded_root)

    squared_number = magic_number ** 2
    print("Число в квадрате:", squared_number)

except ValueError:
    print("Ошибка! Вводить нужно только числа.")


# Задание 5
hero = {
    "name": "Юдзи",
    "level": 7,
    "stats": {
        "hp": 850,
        "mp": 300
    },
    "items": ["меч тени", "зелье"]
}

print("HP:", hero["stats"]["hp"])
print("MP:", hero["stats"]["mp"])
print("Первый предмет:", hero["items"][0])

guild_name = input("Название клана? ")
hero["clan"] = guild_name

print("Клан:", hero.get("clan"))

for attribute, information in hero.items():
    print(attribute, "=", information)


# Задание 6
import json

character_name = input("Введи имя? ")
character_level = int(input("Уровень? "))
gold_amount = int(input("Монеты? "))

game_data = {
    "name": character_name,
    "level": character_level,
    "coins": gold_amount
}

with open("save.json", "w", encoding="utf-8") as file:
    json.dump(game_data, file, ensure_ascii=False)

with open("save.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

print(
    "Загружено из сейва:",
    loaded_data["name"],
    ", уровень ",
    loaded_data["level"],
    ", монеты ",
    loaded_data["coins"],
    sep=""
)

print("Прогресс сохранён и загружен успешно!")


# Задание 7
victory_count = int(input("Побед? "))
defeat_count = int(input("Поражений? "))

match_total = victory_count + defeat_count
victory_percentage = round(victory_count / match_total * 100, 1)

if victory_percentage >= 70:
    player_rank = "Gold"
elif victory_percentage >= 50:
    player_rank = "Silver"
else:
    player_rank = "Bronze"

print("----- ИТОГИ СЕЗОНА -----")
print(f"Побед: {victory_count}")
print(f"Поражений: {defeat_count}")
print(f"Винрейт: {victory_percentage}%")
print(f"Ранг: {player_rank}")


# Задание 8
import random

victory_total = 0
defeat_total = 0
draw_total = 0

for current_round in range(1, 6):
    player_roll = random.randint(1, 6)
    opponent_roll = random.randint(1, 6)

    print(f"Раунд {current_round}: ты {player_roll}, противник {opponent_roll}")

    if player_roll > opponent_roll:
        victory_total += 1
    elif player_roll < opponent_roll:
        defeat_total += 1
    else:
        draw_total += 1

print(f"Счёт: {victory_total} : {defeat_total} (ничьих: {draw_total})")

if victory_total > defeat_total:
    print("Ты победил!")
elif victory_total < defeat_total:
    print("Ты проиграл...")
else:
    print("Ничья!")
