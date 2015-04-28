# a good example of multi threading is Sending and Receiving Messages
import threading

class AndreMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())
            
x = AndreMessenger(name = 'Send Thread')
y = AndreMessenger(name = 'Recieve Thread')

x.start()
y.start()
