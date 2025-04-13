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

    # Обновленная функция getEvent
    def getEvent(type: EventType) -> 'Event':
        if type is not None:
            return getGenericEvent(getattr(events, type.value), True)
        return None
