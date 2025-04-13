init python:
    from typing import List
    from enum import Enum
    import random

    # Базовый класс характеристик
    class State:
        def __init__(self, despair, energy, readiness, probability_of_bugs, team_cohesion):
            self.despair = despair
            self.energy = energy
            self.readiness = readiness
            self.probability_of_bugs = probability_of_bugs
            self.team_cohesion = team_cohesion

        def apply(self, increment: 'State'):
            self.despair += increment.despair
            self.energy += increment.energy
            self.readiness += increment.readiness
            self.probability_of_bugs += increment.probability_of_bugs
            self.team_cohesion += increment.team_cohesion

    # Объект ответа на любое действие
    class Action:
        def __init__(self, name, effect, increment: State):
            self.name = name
            self.effect = effect
            self.increment = increment

    # Событие
    class Event:
        def __init__(self, event_name, actions: List[Action]):
            self.event_name = event_name
            self.actions = actions

    # Функция для вычисления вероятности
    def percent_chance(percent: int) -> bool:
        """Возвращает True с вероятностью percent% (1-100)"""
        return random.randint(1, 100) <= percent

    # Функция для получения события по типу
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

    # Достать из списка generic c флагом удаления после получения события
    def getGenericEvent(collection: List, remove: bool):
        if collection:
            return collection.pop(0) if remove else collection[0]
        return None
