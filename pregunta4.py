import threading
class contador():
    def __init__(self, inicio=0):
        self.inicio = inicio
        self.lock = threading.Lock()

    def funcion(self):
        self.lock.acquire()
        try:
            for i in range(1000000):
                self.inicio += 1
        finally:
            self.lock.release()

contador1 = contador()

for i in range(3):
  iniciar = threading.Thread(target=contador1.funcion)
  iniciar.start()
  iniciar.join()

print(contador1.inicio)