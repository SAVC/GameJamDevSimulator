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
            if(state.team_cohesion >= state.probability_of_bugs):
                event = EventType.BUFF
            else:
                event = EventType.DEBUFF
        return event

# Базовый класс событий
    class Events:
        def __init__(self):
            self.buff = [
                Event("Хорошее настроение", [
                    Action("Начать работать", "У тебя получилось воссоздать то, что было в голове и даже ничего не сломалось", State(10, 10, 5, 5, 5)),
                    Action("Предложить писать новеллу", "Команда задумалась над твоим решением, но все равно считает, что ты тронулся", State(20, 10, 0, 0, 15))
                ]),
                Event("Слишком много кофе", [
                    Action("Попробовать поработать", "Вы написали код, который работает, но никто не понимает как.", State(10, -10, 5, 5, -5)),
                    Action("Может быть еще раз новеллу?", "Команда решила, что вы писатель, но не программист.", State(20, -10, 0, 0, -15))
                ])
            ]
            self.debuff = [
                Event("Сломался интернет", [
                    Action("Попробовать поработать", "Вы написали код, который работает, но никто не понимает как.", State(10, -10, 5, 5, -5)),
                    Action("Предложить написать новеллу", "Команда решила, что вы писатель, но не программист.", State(20, -10, 0, 0, -15))
                ]),
                Event("Команда ушла на обед", [
                    Action("Попробовать поработать", "Вы написали код, который работает, но никто не понимает как.", State(10, -10, 5, 5, -5)),
                    Action("Предложить написать новеллу", "Команда решила, что вы писатель, но не программист.", State(20, -10, 0, 0, -15))
                ])
            ]


#   Достать событие из списка
    def getEvent(type: EventType) -> 'Event':
        if type is not None:
            return getGenericEvent(getattr(events, type.value), True)
        return None
