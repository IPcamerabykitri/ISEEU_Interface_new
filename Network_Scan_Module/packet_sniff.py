import pyshark
import numpy
from . import entropy

def packet_sniff(time):
    cap=pyshark.LiveCapture(interface='eth0',only_summaries="IP" "protocol")
    cap.sniff(timeout=time)
    pkts = [str(pkt).split(" ")[2:5] for pkt in cap._packets]
    cap.close()
    analytical_resource = numpy.transpose(pkts)
    victim_entropy = entropy.calculate_entropy(analytical_resource[0])
    attack_entropy = entropy.calculate_entropy(analytical_resource[1])

    print("victim_rate = {0}, attack_rate = {1}".format(victim_entropy,attack_entropy))
