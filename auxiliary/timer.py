import time

from auxiliary.logger import log


class TimerCM:
    _start = None

    def __enter__(self):
        self._start = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        log(f'Done in {time.perf_counter() - self._start} s')
