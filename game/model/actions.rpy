init python:
    from typing import List  # Импортируем List
    from enum import Enum
    import random
    random.seed()

#   Типы событий
    class EventActionType(str, Enum):
        CODE = "code"
        ASSETS = "assets"
        COFFEE = "coffee"
        SLEEP = "sleep"
        MUSIC = "music"
        SCENARIO = "scenario"

# Базовый класс событий
    class ActionEvents:
        def __init__(self):
            self.code = [
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
            self.assets = [
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
            self.coffee = [
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
            self.sleep = [
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
            self.music = [
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
            self.scenario = [
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
    def getActionEvent(type: EventActionType, level: 'EventLevel') -> 'Event':
        if type is not None:
            return getGenericEvent(level, getattr(events, type.value), False)
        return None