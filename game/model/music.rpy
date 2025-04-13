init python:
    from enum import Enum

    class DespairLevel(str, Enum):
        LIGHT = "audio/music/jaysmitty - time sequence.mp3"
        HARD = "audio/music/jaysmitty - whisper of the time.mp3"
        CRAZY = "audio/music/jaysmitty - feeling (demo).mp3"

    class AudioPlayer:
        def __init__(self, state: State):
            self.state = state
            self.despair_level = None

        def getDespairLevel(self) -> DespairLevel:
            if state.despair < 40:
                return DespairLevel.LIGHT
            elif state.despair < 80:
                return DespairLevel.HARD
            else:
                return DespairLevel.CRAZY

        def play(self):
            new_level = self.getDespairLevel()
            if(self.despair_level != new_level):
                self.despair_level = new_level
                renpy.music.stop(fadeout=1.5)
                renpy.music.play(self.despair_level.value, loop=True, fadein=2.0, relative_volume=0.8)
