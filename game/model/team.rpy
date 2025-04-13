init python:
    from typing import List  # Импортируем List

#   Типы событий
    class EventTeamType(str, Enum):
        BRAINSTORM = "brainstorm"
        TEAM_COHESION = "team_cohesion"
        COMMUNICATION = "communication"

# Базовый класс событий
    class TeamEvents:
        def __init__(self):
            self.brainstorm = [
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
            self.team_cohesion = [
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
            self.communication = [
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