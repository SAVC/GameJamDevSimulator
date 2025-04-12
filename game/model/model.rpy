init python:
    from typing import List  # Импортируем List
    from enum import Enum

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

#   Объект ответа на любое действие
    class Action:
        def __init__(self, name, effect, increment: State):
            self.name = name
            self.effect = effect
            self.increment = increment

#   Уровень события
    class EventLevel(Enum):
        EASY = 25
        NORMAL = 50
        MAJOR = 75
        CRITICAL = 100

        @staticmethod
        def getByValue(value) -> 'EventLevel':
            if value <= 25:
                return EventLevel.EASY
            if value <= 50:
                return EventLevel.NORMAL
            if value <= 75:
                return EventLevel.MAJOR
            if value >= 75:
                return EventLevel.CRITICAL

#   Событие
    class Event:
        def __init__(self, event_name, event_level: EventLevel, actions: List[Action]):
            self.event_name = event_name
            self.event_level = event_level
            self.actions = actions

#   Событие по вероятности
    def percent_chance(percent: int) -> bool:
        """Возвращает True с вероятностью percent% (1-100)"""
        return random.randint(1, 100) <= percent

# Достать из списка generic c флагом удаления после получения события
    def getGenericEvent(level: EventLevel, collection: List, remove: bool):
        for i, item in enumerate(collection):
            if getattr(item, "event_level") == level:
                return collection.pop(i) if remove else item
        return None