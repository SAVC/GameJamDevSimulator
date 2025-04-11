# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

default inventory = []       # Можно хранить списки
default player_name = ""     # Или строки
default despair_lever = 0.     #  float


# The game starts here.

label start:
    jump room  # Начинаем в комнате

label room:
    scene room  # Показываем фон комнаты
    "Вы в своей комнате у вас отчаяние [despair_lever]"

    # Меню действий в комнате
    menu:
        "Осмотреть стол":
            "У вас повысился уровень отчаяния от вида вашего стола"
            $ despair_lever += 10
        "Подойти к окну":
            "За окном светит солнце."
        "Подойти к компьютеру":
            jump computer  # Переход к компьютеру
    # После выбора возвращаемся в комнату

    if (despair_lever >= 100):
        "Вы не выдержали и застрелились."
        return
    else:
        jump room

label computer:
    scene computer  # Показываем фон улицы
    "Вы Подошли к компьютеру"
    call screen location_menu  # Снова вызываем меню