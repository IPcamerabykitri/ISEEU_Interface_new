import pyshark

def packet_sniff(time):
    cap=pyshark.LiveCapture(interface='eth0',only_summaries="IP" "protocol")
    cap.sniff(timeout=time)
    pkts = [str(pkt).split(" ")[2:5] for pkt in cap._packets]
    cap.close()
    for packet in pkts:
        print(packet)
