# team.rpy
init python:
    from typing import List  # Импортируем List

    # Персонаж
    class Character:
        def __init__(self, name, events: List[Event]):
            self.name = name
            self.events = events

    # Создание персонажей и их событий
    characters = [
        Character("Alice", [
            Event("Alice needs help with a bug", [
                Action("Offer to help", "Alice is grateful for your help. Team cohesion increases.", State(0, -5, 0, 0, 10)),
                Action("Say you're busy", "Alice understands but is a bit disappointed. Team cohesion decreases.", State(0, 0, 0, 0, -5))
            ]),
            Event("Alice wants to discuss the project", [
                Action("Engage in discussion", "You have a productive discussion. Readiness increases.", State(0, -5, 10, 0, 0)),
                Action("Avoid the discussion", "Alice feels ignored. Team cohesion decreases.", State(0, 0, 0, 0, -5))
            ])
        ]),
        Character("Bob", [
            Event("Bob has a new idea", [
                Action("Listen to his idea", "Bob is excited to share. Team cohesion increases.", State(0, -5, 0, 0, 10)),
                Action("Dismiss his idea", "Bob feels rejected. Team cohesion decreases.", State(0, 0, 0, 0, -5))
            ]),
            Event("Bob needs a break", [
                Action("Suggest a short break", "Bob appreciates the suggestion. Energy increases.", State(0, 10, 0, 0, 0)),
                Action("Tell him to keep working", "Bob feels stressed. Despair increases.", State(10, 0, 0, 0, 0))
            ])
        ]),
        # Добавьте еще персонажей и их событий по аналогии
    ]

    # Функция для получения случайного персонажа и события
    def get_random_character_event() -> (Character, Event):
        character = random.choice(characters)
        event = random.choice(character.events)
        return character, event
