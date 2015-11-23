# -*- encoding: utf-8 -*-


ALPHABET_COUNT = ord('z') - ord('a') + 1


# Call this function to get a function that rotates the alphabet by the given number
def mk_ceasar(rot):
    def map_fun(instr):
        char_map = {}
        char_map.update({chr(ord('a') + idx): chr((idx + rot) % ALPHABET_COUNT + ord('a')) for idx in xrange(ALPHABET_COUNT)})
        char_map.update({chr(ord('A') + idx): chr((idx + rot) % ALPHABET_COUNT + ord('A')) for idx in xrange(ALPHABET_COUNT)})
        return ''.join(char_map[char] if (char in char_map) else char for char in instr)
    return map_fun


if __name__ == "__main__":
    rot13 = mk_ceasar(13)
    while True:
        line = raw_input().strip()
        print rot13(line)


