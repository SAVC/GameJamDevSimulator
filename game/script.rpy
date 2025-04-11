# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:
    jump room  # Начинаем в комнате

label room:
    scene room  # Показываем фон комнаты
    "Вы в своей комнате"

    # Меню действий в комнате
    menu:
        "Осмотреть стол":
            "На столе лежит книга и кружка."
        "Подойти к окну":
            "За окном светит солнце."
        "Подойти к компьютеру":
            jump computer  # Переход к компьютеру
    # После выбора возвращаемся в комнату
    jump room

label computer:
    scene computer  # Показываем фон улицы
    "Вы Подошли к компьютеру"
    call screen location_menu  # Снова вызываем меню