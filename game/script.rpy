# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# init python:
#     from model.state import State

define e = Character("Eileen")

default state = State(0, 100, 0, 0, 50)
default player_name = ""
default difficulty_multiplier = 1
default hours_to_deadline = 48
default events = Events()
default actions = ActionEvents()


# Начало игры
label start:
    jump room_event  # Начинаем в комнате

# Первый этап - случайные события
label room_event:
    scene room  # Показываем фон комнаты

    """Вы в своей комнате у вас отчаяние [state.despair]\n
    Бодрость [state.energy]\n
    Степень готовности проекта [state.readiness]\n
    Вероятность бага [state.probability_of_bugs]\n
    Сплоченность команды [state.team_cohesion]
    """

    # Начинается событие
    python:
        buffAppears = percent_chance(state.team_cohesion)
        debuffAppears = percent_chance(state.probability_of_bugs)
        eventType = getEventType(buffAppears, debuffAppears)

# TODO REMOVE DEBUG
    """
    У вас появилось событие [eventType]\n
    Информация buffAppears = [buffAppears], debuffAppears = [debuffAppears]
    """

    python:
        if eventType is not None:
            level = EventLevel.getByValue(state.team_cohesion if eventType == EventType.BUFF else state.probability_of_bugs)
            event = getEvent(eventType, level)

# TODO REMOVE DEBUG
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
# TODO REMOVE DEBUG
        if eventType is None:
            "События не произошло"
        else:
            "События этого типа закончились в списке"

    if (state.despair >= 100):
        "Вы не выдержали и застрелились."
        return
    else:
        jump room_action

# Второй этап - действия
label room_action:
    scene room  # Показываем фон комнаты
    "Настало время действовать. Покажи свою мощь!!!"
    call screen location_menu  # Снова вызываем меню

# Писать код
label code:
    scene room  # Показываем фон комнаты
    python:
        level = EventLevel.getByValue((state.probability_of_bugs + state.readiness) * 0.5)
        event = getActionEvent(EventActionType.CODE, level)

# TODO REMOVE DEBUG
    if eventType is not None and event is not None:
        """
        Уровень события [level]\n
        Cамо событие [event.event_name]
        """

    if eventType is not None and event is not None:
        call screen action_menu(event.actions)
        "[result.effect]"
        $ state.apply(result.increment)
# TODO REMOVE DEBUG
    else:
        "Ничего не происходит..."
        if eventType is None:
            "События не произошло"
        else:
            "События этого типа закончились в списке"
    jump room_team # Переходим на этап общения с командой

# Создавать ассеты
label assets:
    scene room  # Показываем фон комнаты
    python:
        level = EventLevel.getByValue(state.readiness)
        event = getActionEvent(EventActionType.ASSETS, level)

# TODO REMOVE DEBUG
    if eventType is not None and event is not None:
        """
        Уровень события [level]\n
        Cамо событие [event.event_name]
        """

    if eventType is not None and event is not None:
        call screen action_menu(event.actions)
        "[result.effect]"
        $ state.apply(result.increment)
# TODO REMOVE DEBUG
    else:
        "Ничего не происходит..."
        if eventType is None:
            "События не произошло"
        else:
            "События этого типа закончились в списке"
    jump room_team # Переходим на этап общения с командой

# Пить кофе
label coffee:
    scene room  # Показываем фон комнаты
    python:
        level = EventLevel.getByValue(state.energy)
        event = getActionEvent(EventActionType.COFFEE, level)

# TODO REMOVE DEBUG
    if eventType is not None and event is not None:
        """
        Уровень события [level]\n
        Cамо событие [event.event_name]
        """

    if eventType is not None and event is not None:
        call screen action_menu(event.actions)
        "[result.effect]"
        $ state.apply(result.increment)
# TODO REMOVE DEBUG
    else:
        "Ничего не происходит..."
        if eventType is None:
            "События не произошло"
        else:
            "События этого типа закончились в списке"
    jump room_team # Переходим на этап общения с командой

# Спать
label sleep:
    scene room  # Показываем фон комнаты
    python:
        level = EventLevel.getByValue(state.despair)
        event = getActionEvent(EventActionType.SLEEP, level)

# TODO REMOVE DEBUG
    if eventType is not None and event is not None:
        """
        Уровень события [level]\n
        Cамо событие [event.event_name]
        """

    if eventType is not None and event is not None:
        call screen action_menu(event.actions)
        "[result.effect]"
        $ state.apply(result.increment)
# TODO REMOVE DEBUG
    else:
        "Ничего не происходит..."
        if eventType is None:
            "События не произошло"
        else:
            "События этого типа закончились в списке"
    jump room_team # Переходим на этап общения с командой

# Писать музыку
label music:
    scene room  # Показываем фон комнаты
    python:
        level = EventLevel.getByValue(state.readiness)
        event = getActionEvent(EventActionType.MUSIC, level)

# TODO REMOVE DEBUG
    if eventType is not None and event is not None:
        """
        Уровень события [level]\n
        Cамо событие [event.event_name]
        """

    if eventType is not None and event is not None:
        call screen action_menu(event.actions)
        "[result.effect]"
        $ state.apply(result.increment)
# TODO REMOVE DEBUG
    else:
        "Ничего не происходит..."
        if eventType is None:
            "События не произошло"
        else:
            "События этого типа закончились в списке"
    jump room_team # Переходим на этап общения с командой

# Писать сценарий
label scenario:
    scene room  # Показываем фон комнаты
    python:
        level = EventLevel.getByValue(state.team_cohesion)
        event = getActionEvent(EventActionType.SCENARIO, level)

# TODO REMOVE DEBUG
    if eventType is not None and event is not None:
        """
        Уровень события [level]\n
        Cамо событие [event.event_name]
        """

    if eventType is not None and event is not None:
        call screen action_menu(event.actions)
        "[result.effect]"
        $ state.apply(result.increment)
# TODO REMOVE DEBUG
    else:
        "Ничего не происходит..."
        if eventType is None:
            "События не произошло"
        else:
            "События этого типа закончились в списке"
    jump room_team # Переходим на этап общения с командой

# Третий этап - общение с командой
label room_team:
     scene computer  # Показываем фон компьютера

