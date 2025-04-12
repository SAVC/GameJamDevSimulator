# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# init python:
#     from model.state import State

define e = Character("Eileen")

default state = State(0, 100, 0, 0, 50)
default player_name = ""
default difficulty_multiplier = 1
default events = Events()


# The game starts here.

label start:
    jump room_event  # Начинаем в комнате

label room_event:
    scene room  # Показываем фон комнаты

    """Вы в своей комнате у вас отчаяние [state.despair]\n
    Бордрость [state.energy]\n
    Степень готовности проекта [state.readiness]\n
    Вероятность бага [state.probability_of_bugs]\n
    Сплоченность команды [state.team_cohesion]
    """


    # Начинается событие
    python:
        buffAppears = percent_chance(state.team_cohesion)
        debuffAppears = percent_chance(state.probability_of_bugs)
        eventType = getEventType(buffAppears, debuffAppears)

    """
    У вас появилось событие [eventType]\n
    Информация buffAppears = [buffAppears], debuffAppears = [debuffAppears]
    """

    python:
        if eventType is not None:
            level = EventLevel.getByValue(state.team_cohesion if eventType == EventType.BUFF else state.probability_of_bugs)
            event = getEvent(eventType, level)

    if eventType is not None and event is not None:
        """
        Уровень события [level]\n
        Cамо событие [event.event_name]
        """

    if eventType is not None and event is not None:
        call screen action_menu(event.actions)
        "[result.effect]"
        $ state.apply(result.increment)
    else:
        "Ничего не происходит..."
        if eventType is None:
            "События не произошло"
        else:
            "События этого типа закончились в списке"

    if (state.despair >= 100):
        "Вы не выдержали и застрелились."
        return
    else:
        jump room_event # TODO переходим к room_action

label room_action:
    scene room  # Показываем фон комнаты
    "Настало время действовать. Покажи свою мощь!!!"
    call screen location_menu  # Снова вызываем меню

label room_team:
     scene computer  # Показываем фон компьютера