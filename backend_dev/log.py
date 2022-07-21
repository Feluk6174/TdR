from tabnanny import verbose
import time
import threading

class Logger():
    def __init__(self, log_file, vervose = False):
        self.log_file = open(log_file+time.time()+".log", "w")
        self.queue = []
        self.vervose = vervose
        thread = threading.Thread(target=self.proces_queue)
        thread.start()

    def log(self, message):
        self.queue.append(f"[{threading.current_thread().name}]({time.asctime})", message)

    def proces_queue(self):
        if not len(self.queue) == 0:
            self.log_file.write(str(self.queue[0]))
            if verbose:
                print(self.queue[0])
            self.queue.pop(0)
