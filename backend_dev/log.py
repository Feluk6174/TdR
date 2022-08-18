from tabnanny import verbose
import time
import threading

class Logger():
    def __init__(self, log_file, vervose = False):
        self.log_file_name = log_file+str(int(time.time()))+".log"
        self.queue = []
        self.vervose = vervose
        thread = threading.Thread(target=self.proces_queue)
        thread.start()

    def log(self, *messages):
        text = f"[{threading.current_thread().name}]({time.asctime()}) "
        for message in messages:
            text += str(message) + " "
        self.queue.append(text)

    def proces_queue(self):
        self.queue.append("[STARTED LOGGER]")
        while True:
            if not len(self.queue) == 0:
                with open(self.log_file_name, "a") as f:
                    f.write(str(self.queue[0])+"\n")
                if self.vervose:
                    print(self.queue[0])
                self.queue.pop(0)
