# from events import EventListener
from concurrent.futures import ThreadPoolExecutor
import pygame
from pygame.mixer import Sound
import time


class AudioManager:
    def __init__(self, max_workers: int = 4) -> None:
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
        self._sound_cache: dict[str, Sound] = {}
        self._pool: ThreadPoolExecutor = ThreadPoolExecutor(
            max_workers=max_workers, thread_name_prefix="AudioWorker"
        )

    def _play_effect_worker(self, sound_name: str, volume: float, loops: int) -> None:
        filepath = f"sound_effects/{sound_name}.mp3"
        try:
            if filepath not in self._sound_cache:
                print(f"[Thread] Loading file into RAM: {filepath}")
                self._sound_cache[filepath] = Sound(filepath)

            sound: Sound = self._sound_cache[filepath]
            sound.set_volume(volume)
            sound.play(loops=loops)

        except Exception as e:
            print(f"[Audio Error] Failed to play sound effect {filepath}: {e}")

    def play_sound(self, sound_name: str, volume: float = 1.0, loops: int = 0) -> None:
        self._pool.submit(self._play_effect_worker, sound_name, volume, loops)

    def shutdown(self) -> None:
        self._pool.shutdown(wait=True)
        pygame.mixer.quit()


audio = AudioManager()

audio.play_sound("blunderbuss", volume=0.1)
time.sleep(10)
audio.shutdown()
