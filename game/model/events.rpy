init python:
    from typing import List  # Импортируем List
    from enum import Enum
    import random
    random.seed()

#   Типы событий
    class EventType(str, Enum):
        BUFF = "buff"
        DEBUFF = "debuff"

#   Выбрать тип события по итогу
    def getEventType(buffAppears, debuffAppears) -> EventType:
        event = None
        if(buffAppears and not debuffAppears):
            event = EventType.BUFF
        if(debuffAppears and not buffAppears):
            event = EventType.DEBUFF
        if(buffAppears and debuffAppears):
            if(state,team_cohesion >= state.probability_of_bugs):
                event = EventType.BUFF
            else:
                event = EventType.DEBUFF
        return event

# Базовый класс событий
    class Events:
        def __init__(self):
            self.buff = [
              Event("Test", EventLevel.EASY, [
                    Action("Начать работать", "Вы сломали 1", State(10, -10, 5, 5, -5)),
                    Action("Предложить писать новеллу",  "У команды нервный срыв", State(20, -10, 0, 0, -15))
                ]),
                Event("Test 2", EventLevel.NORMAL, [
                    Action("Начать работать 2", "Вы сломали 2", State(10, -10, 5, 5, -5)),
                    Action("Предложить писать новеллу 2", "У команды нервный срыв", State(20, -10, 0, 0, -15))
                ]),
                Event("Test 2", EventLevel.MAJOR, [
                    Action("Начать работать 2", "Вы сломали 2", State(10, -10, 5, 5, -5)),
                    Action("Предложить писать новеллу 2", "У команды нервный срыв", State(20, -10, 0, 0, -15))
                ]),
                Event("Test 2", EventLevel.CRITICAL, [
                    Action("Начать работать 2", "Вы сломали 2", State(10, -10, 5, 5, -5)),
                    Action("Предложить писать новеллу 2", "У команды нервный срыв", State(20, -10, 0, 0, -15))
                ]),
            ]
            self.debuff = [
                Event("Test", EventLevel.EASY, [
                    Action("Начать работать", "Вы сломали 1", State(10, -10, 5, 5, -5)),
                    Action("Предложить писать новеллу", "У команды нервный срыв", State(20, -10, 0, 0, -15))
                ]),
                Event("Test 2", EventLevel.NORMAL, [
                    Action("Начать работать 2", "Вы сломали 2", State(10, -10, 5, 5, -5)),
                    Action("Предложить писать новеллу 2", "У команды нервный срыв", State(20, -10, 0, 0, -15))
                ]),
                Event("Test 2", EventLevel.MAJOR, [
                    Action("Начать работать 2", "Вы сломали 2",  State(10, -10, 5, 5, -5)),
                    Action("Предложить писать новеллу 2", "У команды нервный срыв", State(20, -10, 0, 0, -15))
                ]),
                Event("Test 2", EventLevel.CRITICAL, [
                    Action("Начать работать 2", "Вы сломали 2", State(10, -10, 5, 5, -5)),
                    Action("Предложить писать новеллу 2", "У команды нервный срыв", State(20, -10, 0, 0, -15))
                ]),
            ]

#   Достать событие из списка
    def getEvent(type: EventType, level: 'EventLevel') -> 'Event':
        if type is not None:
            return getGenericEvent(level, getattr(events, type.value), True)
        return None