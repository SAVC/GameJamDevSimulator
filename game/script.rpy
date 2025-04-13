default state = State(0, 100, 0, 0, 50)
default player_name = ""
default difficulty_multiplier = 1
default hours_to_deadline = 48
default events = Events()
default actions = ActionEvents()
default audio_player = AudioPlayer(state)

# Начало игры
label start:
    jump room_event  # Начинаем в комнате

# Первый этап - случайные события
label room_event:
    $ audio_player.play()
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

    python:
        if eventType is not None:
            event = getEvent(eventType)

    if eventType is not None and event is not None:
        """
        Событие: "[event.event_name]"
        """

    if eventType is not None and event is not None:
        call screen action_menu(event.actions)
        "[result.effect]"
        $ state.apply(result.increment)
    else:
        "Ничего не интересного не произошло..."
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
    $ audio_player.play()
    scene room  # Показываем фон комнаты
    "Настало время действовать!"
    call screen location_menu  # Снова вызываем меню

# Писать код
label code:
    $ audio_player.play()
    scene room  # Показываем фон комнаты
    python:
        event = getActionEvent(EventActionType.CODE)

    if event is not None:
        """
        Событие: "[event.event_name]"
        """

    if event is not None:
        call screen action_menu(event.actions)
        "[result.effect]"
        $ state.apply(result.increment)
    else:
        "Ничего не происходит..."
        "События этого типа закончились в списке"
    jump room_team # Переходим на этап общения с командой

# Создавать ассеты
label assets:
    $ audio_player.play()
    scene room  # Показываем фон комнаты
    python:
        event = getActionEvent(EventActionType.ASSETS)

    if event is not None:
        """
        Событие: "[event.event_name]"
        """

    if event is not None:
        call screen action_menu(event.actions)
        "[result.effect]"
        $ state.apply(result.increment)
    else:
        "Ничего не происходит..."
        "События этого типа закончились в списке"
    jump room_team # Переходим на этап общения с командой

# Пить кофе
label coffee:
    $ audio_player.play()
    scene room  # Показываем фон комнаты
    python:
        event = getActionEvent(EventActionType.COFFEE)

    if event is not None:
        """
        Событие: "[event.event_name]"
        """

    if event is not None:
        call screen action_menu(event.actions)
        "[result.effect]"
        $ state.apply(result.increment)
    else:
        "Ничего не происходит..."
        "События этого типа закончились в списке"
    jump room_team # Переходим на этап общения с командой

# Спать
label sleep:
    $ audio_player.play()
    scene room  # Показываем фон комнаты
    python:
        event = getActionEvent(EventActionType.SLEEP)

    if event is not None:
        """
        Событие: "[event.event_name]"
        """

    if event is not None:
        call screen action_menu(event.actions)
        "[result.effect]"
        $ state.apply(result.increment)
    else:
        "Ничего не происходит..."
        "События этого типа закончились в списке"
    jump room_team # Переходим на этап общения с командой

# Писать музыку
label music:
    $ audio_player.play()
    scene room  # Показываем фон комнаты
    python:
        event = getActionEvent(EventActionType.MUSIC)

    if event is not None:
        """
        Событие: "[event.event_name]"
        """

    if event is not None:
        call screen action_menu(event.actions)
        "[result.effect]"
        $ state.apply(result.increment)
    else:
        "Ничего не происходит..."
        "События этого типа закончились в списке"
    jump room_team # Переходим на этап общения с командой

# Писать сценарий
label scenario:
    $ audio_player.play()
    scene room  # Показываем фон комнаты
    python:
        event = getActionEvent(EventActionType.SCENARIO)

    if event is not None:
        """
        Событие: "[event.event_name]"
        """

    if event is not None:
        call screen action_menu(event.actions)
        "[result.effect]"
        $ state.apply(result.increment)
    else:
        "Ничего не происходит..."
        "События этого типа закончились в списке"
    jump room_team # Переходим на этап общения с командой


# Третий этап - общение с командой
label room_team:
    $ audio_player.play()
    scene computer  # Показываем фон компьютера
    "Очередная планерка с командой"
    $ hours_to_deadline -= 1  # Уменьшаем время до дедлайна

    python:
        character, event = get_random_character_event()

    if character is not None and event is not None:
        """
        [character.name]: "[event.event_name]"
        """

    if character is not None and event is not None:
        call screen action_menu(event.actions)
        "[result.effect]"
        $ state.apply(result.increment)

    if hours_to_deadline <= 0:
        jump ending
    jump room_event  # Возвращаемся в основной цикл


# Добавляем переход на эту метку когда время вышло
label ending:
    # Здесь логика завершения игры
    "Дедлайн наступил! Ваш результат..."
    return