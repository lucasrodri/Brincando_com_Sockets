from r2a.ir2a import IR2A
from player.parser import *
import time
import sys
from statistics import mean


class R2ATeste(IR2A):

    def __init__(self, id):
        IR2A.__init__(self, id)
        self.throughputs = []
        self.qi = []
        self.time_request = 0

    def handle_xml_request(self, msg):
        self.send_down(msg)

    def handle_xml_response(self, msg):
        parsed_mpd = parse_mpd(msg.get_payload())
        self.qi = parsed_mpd.get_qi()
        self.send_up(msg)

    def handle_segment_size_request(self, msg):

        if len(self.whiteboard.get_playback_buffer_size()) > 0:
            buffer_size = self.whiteboard.get_playback_buffer_size()[-1][1]
        else:
            buffer_size = 0

        print(">>>>>>>>>>>>>>>Buffer SIZE:", buffer_size)

        div = 2
        if buffer_size > 25:
            div = 1
        elif buffer_size < 5:
            div = 3
        else:
            div = 2

        avg = get_media(self.throughputs)

        print("")
        print(">>>>>>>>>>>>>>>>>>")
        print(f"Vazoes = {self.throughputs}")
        print(f"Média = {avg}")
        print(f"Média/2 = {avg/2}")
        print(">>>>>>>>>>>>>>>>>>")
        print("")

        self.time_request = time.perf_counter()

        selected_qi = self.qi[0]
        for i in self.qi:
            if avg/div > i:
                selected_qi = i

        print("")
        print(">>>>>>>>>>>>>>>>>>")
        print(f"Selecionado = {selected_qi}")
        print(">>>>>>>>>>>>>>>>>>")
        print("")

        msg.add_quality_id(selected_qi)

        self.send_down(msg)

    def handle_segment_size_response(self, msg):

        print(msg.get_url())

        tempo = time.perf_counter() - self.time_request
        tamanho_bits = msg.get_bit_length()
        vazao = tamanho_bits/tempo

        append_throughputs(self, vazao)

        print("")
        print(f">>>>>>>>>>>>>>>>>> Tempo = {tempo}")
        print(f">>>>>>>>>>>>>>>>>> Tamanho em bits = {tamanho_bits}")
        print(f">>>>>>>>>>>>>>>>>> Vazao = {vazao}")
        print("")

        self.send_up(msg)

    def initialize(self):
        pass

    def finalization(self):
        pass


def get_media(throughputs):
    if len(throughputs) == 0:
        return 0
    else:
        return mean(throughputs)


def append_throughputs(self, vazao):
    self.throughputs.append(vazao)
    if len(self.throughputs) > 3:
        self.throughputs.pop(0)
