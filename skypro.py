import random
import os
import time

clear = lambda: os.system('clear')
role = {'1': 'Воин', '2': 'Лучник', '3': 'Mar'}

classes = {
    'Воин': {
        'здоровье': 100,
        'атака': 30,
        'защита': 25,
        'навыки': {
            'щит': 10
        }
    },
    'Лучник': {
        'здоровье': 50,
        'атака': 40,
        'защита': 20,
        'навыки': {
            'убежать': 10
        }
    },
    'Maг': {
        'здоровье': 30,
        'атака': 50,
        'защита': 15,
        'навыки': {
            'магический щит': 10,
            'лечение': 5
        }
    }
}


def init_person(name: str, is_enemy: bool = False) -> dict:
    while True:
        try:
            if is_enemy:
                person = {'класс': role[random.choice(list(role.keys()))]}
            else:
                person = {'класс': role[input('Введите класс: 1-Воин, 2-Лучник, 3-Маг\n')]}

            person.update({'характеристики': classes[person['класс']]})
            person.update({'имя': name})

            print(f"{person['имя']} - {person['класс']}, имеет характеристики: {person['характеристики']}")
            return person
            break
        except:
            print(f"Вы ввели не правильные данные, можно ввести от 1 до {len(role)}\n")


def get_player_name() -> str:
    while True:
        try:
            name = input('Введите свой никнейм: \n')
            return name
            break
        except:
            print('Вы не можете ввести такое имя :(')


def get_random_name():
    adjective = ['Доктор', 'Летающий', 'Светящийся', 'Профессор', 'Неимоверный', 'Мега', 'Железный', 'Голодный',
                 'Капитан',
                 'Быстрый', 'Мистер', 'Горячий', 'Звездный', 'Космический', 'Стойкий', 'Восхитительный', 'Непопедимый']
    noun = ['слесарь', 'мухомор', 'пепел', 'лемур', 'шаман', 'пельмень', 'слизень', 'алхимик', 'крот', 'фикус',
            'господин',
            'кролик', 'танцор', 'пингвин', 'викинг', 'паук', 'плащ']

    full_name = ''
    full_name += random.choice(adjective) + ' ' + random.choice(noun)
    return full_name


def attack_enemy(enemy1: dict, enemy2: dict) -> None:
    print(f'{enemy1["имя"]} атакует {enemy2["имя"]}!')
    time.sleep(2)
    if random.randint(1, 2) == 1:
        apply_skill(enemy2)
    damage = enemy1['характеристики']['атака'] - enemy2['характеристики']['защита']
    if damage < 0:
        damage = 1

    enemy2['характеристики']['здоровье'] -= damage
    print(
        f"{enemy1['имя']} наносит {damage} урона и у {enemy2['имя']} остается {enemy2['характеристики']['здоровье']} здоровья!")


def apply_skill(enemy2: dict) -> None:
    print(f'{enemy2["имя"]} применяет способность {enemy2["характеристики"]["навыки"]}!')
    if enemy2["характеристики"]["навыки"] == 'щит':
        enemy2['характеристики']['защита'] += enemy2["характеристики"]["навыки"]['щит']

    elif enemy2["характеристики"]["навыки"] == 'убежать':
        enemy2['характеристики']['защита'] += enemy2["характеристики"]["навыки"]["убежать"]

    elif enemy2['характеристики']['защита'] == 'лечение':
        enemy2['характеристики']['здоровье'] += enemy2['характеристики']["навыки"]['лечение']

    elif enemy2['характеристики']['защита'] == 'магический щит':
        enemy2['характеристики']['защита'] += enemy2["характеристики"]["навыки"]['магический щит']


def enter_to_continue():
    input("Нажмите Enter, чтобы продолжить")


def fight_for_the_win(attacker, defender):
    while True:
        time.sleep(2)
        clear()

        if attacker['характеристики']['здоровье'] > 0:
            attack_enemy(attacker, defender)
        else:
            print(f"{attacker['имя']} потерпел поражение")
            return False

        if defender['характеристики']['здоровье'] > 0:
            attacker(defender, attacker)
        else:
            print(f"{defender['имя']} потерпел поражение")
            return False
        enter_to_continue()


clear()

player = init_person(get_player_name())
enemy = init_person(get_random_name(), False)


enter_to_continue()
clear()

fight_for_the_win(player, enemy)




















