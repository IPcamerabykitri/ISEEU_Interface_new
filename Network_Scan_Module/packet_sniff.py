import pyshark
import numpy
from . import entropy

def packet_sniff(time):

    max_ent_rate : 5
    min_ent_rate : 1

    cap=pyshark.LiveCapture(interface='eth0',only_summaries="IP" "protocol")
    cap.sniff(timeout=time)
    pkts = [str(pkt).split(" ")[2:5] for pkt in cap._packets]
    cap.close()
    analytical_resource = numpy.transpose(pkts)
    victim_entropy = entropy.calculate_entropy(analytical_resource[0])
    attack_entropy = entropy.calculate_entropy(analytical_resource[1])
    
    print("---------- Victim_Status ----------")
    symbol = victim_entropy["values_symbol"]
    max_symbol = max(symbol,key=symbol.get)
    ent = victim_entropy["entropy"]
    print("total_symbol_count = {count}\n"
          "The number of IPs that were found the most = {IP} : {IP_count}"
          "\nEntropy rate = {ent}".format(
        count=victim_entropy["total_symbol_count"],
        IP = max_symbol,
        IP_count = symbol[max_symbol],
        ent = ent))

    if ent <= min_ent_rate or ent >= max_ent_rate:
        print("You are Victim!")
    else :
        print("You are not Victim")

    print("---------- Attack_Status ----------")
    symbol = attack_entropy["values_symbol"]
    max_symbol = max(symbol,key=symbol.get)
    ent = attack_entropy["entropy"]
    print("total_symbol_count = {count}\n"
          "The number of IPs that were found the most = {IP} : {IP_count}"
          "\nEntropy rate = {ent}".format(
        count=attack_entropy["total_symbol_count"],
        IP = max_symbol,
        IP_count = symbol[max_symbol],
        ent = ent))

    if ent <= min_ent_rate or ent >= max_ent_rate:
        print("You are Attacker!")
    else :
        print("You are not Attacker")

    print("\nPacket Test ends....")