from typing import Literal


class Packet:
    def __init__(self, version, binaries):
        self.version = version
        self.binaries = binaries

    def get_leftovers(self):
        return self.binaries


class LiteralPacket(Packet):
    def __init__(self, version, binaries):
        super().__init__(version, binaries)
        literal_bin = ""
        self.literal = 0
        while self.binaries:
            if self.binaries[0] == "1":
                literal_bin += self.binaries[1:5]
                self.binaries = self.binaries[5:]
            else:
                literal_bin += self.binaries[1:5]
                self.literal = int(literal_bin, 2)
                self.binaries = self.binaries[5:]
                break


class OperatorPacket(Packet):
    def __init__(self, version, binaries):
        super().__init__(version, binaries)
        if self.binaries[0] == "1":
            self.length_type_id = 11
        else:
            self.length_type_id = 15
        self.binaries = self.binaries[1:]
        self.literal_packets = []
        self.operatr_packets = []
        if self.length_type_id == 11:
            self.num_packets = int(self.binaries[: self.length_type_id], 2)
            self.binaries = self.binaries[self.length_type_id :]
            for _ in range(self.num_packets):
                vers = int(self.binaries[:3], 2)
                type_id = int(self.binaries[3:6], 2)
                leftovers = self.binaries[6:]
                if type_id == 4:
                    self.literal_packets.append(LiteralPacket(vers, leftovers))
                    self.binaries = self.literal_packets[-1].get_leftovers()
                else:
                    self.operatr_packets.append(OperatorPacket(vers, leftovers))
                    self.binaries = self.operatr_packets[-1].get_leftovers()
        else:
            self.len_packets = int(self.binaries[: self.length_type_id], 2)
            self.binaries = self.binaries[self.length_type_id :]
            loop_binaries = self.binaries[: self.len_packets]
            self.binaries = self.binaries[self.len_packets :]
            while loop_binaries:
                vers = int(loop_binaries[:3], 2)
                type_id = int(loop_binaries[3:6], 2)
                leftovers = loop_binaries[6:]
                if type_id == 4:
                    self.literal_packets.append(LiteralPacket(vers, leftovers))
                    loop_binaries = self.literal_packets[-1].get_leftovers()
                else:
                    self.operatr_packets.append(OperatorPacket(vers, leftovers))
                    loop_binaries = self.operatr_packets[-1].get_leftovers()

    def all_packets(self):
        all_packs = self.literal_packets
        for packet in self.operatr_packets:
            all_packs.extend(packet.all_packets())
        return all_packs

    def all_versions(self):
        versions = 0
        versions += self.version
        for packet in self.literal_packets:
            versions += packet.version
        for packet in self.operatr_packets:
            versions += packet.all_versions()
        return versions


def parse_packet(binaries):
    version = int(binaries[:3], 2)
    type_id = int(binaries[3:6], 2)
    leftovers = binaries[6:]
    if type_id == 4:
        return LiteralPacket(version, leftovers)
    else:
        return OperatorPacket(version, leftovers)


with open("day16/input", mode="r") as f:
    hexas = f.read().strip()

binaries = bin(int(hexas, 16))[2:].zfill(len(hexas) * 4)

base_packet = parse_packet(binaries)
print(base_packet.all_versions())
