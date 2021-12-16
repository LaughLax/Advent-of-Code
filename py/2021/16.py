import numpy as np

b_map = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}


def process_packet(string):
    result = None
    ver_total = 0
    i = 0

    ver_total += int(string[i:i+3], base=2)
    typ = int(string[i+3:i+6], base=2)
    i += 6
    if typ == 4:
        num_bits = string[i+1:i+5]
        while i+5 < len(string) and string[i] == '1':
            i += 5
            num_bits += string[i+1:i+5]
        i += 5
        num = np.longlong(int(num_bits, base=2))
        result = num
    else:
        len_typ = string[i]
        i += 1
        subs = []
        if len_typ == '0':
            packet_len = int(string[i:i+15], base=2)
            i += 15
            sub_i = 0
            while sub_i < packet_len:
                incr, ver, res = process_packet(string[i:i+packet_len-sub_i])
                i += incr
                sub_i += incr
                ver_total += ver
                subs.append(res)
        else:
            packet_num = int(string[i:i+11], base=2)
            i += 11
            for _ in range(packet_num):
                incr, ver, res = process_packet(string[i:])
                i += incr
                ver_total += ver
                subs.append(res)

        if typ == 0:
            result = np.sum(subs)
        elif typ == 1:
            result = np.prod(subs)
        elif typ == 2:
            result = np.min(subs)
        elif typ == 3:
            result = np.max(subs)
        elif typ == 5:
            assert len(subs) == 2
            result = 1 if subs[0] > subs[1] else 0
        elif typ == 6:
            assert len(subs) == 2
            result = 1 if subs[0] < subs[1] else 0
        elif typ == 7:
            assert len(subs) == 2
            result = 1 if subs[0] == subs[1] else 0

    return i, ver_total, result


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().strip()
        self.input = ''.join(b_map[ch] for ch in self.input)

    def part1(self):
        _, ver, _ = process_packet(self.input)
        return ver

    def part2(self):
        _, _, res = process_packet(self.input)
        return res
