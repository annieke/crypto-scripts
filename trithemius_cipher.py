# Tests out ways to decode a Trithemius Cipher (in all capital letters)
# returns str shifted by i letters
# params: int, string
def test_by_index(shift, str):
    abc_to_num = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
        'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
        'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
        'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
        'Z': 25
    }

    num_to_abc = [
        'A', 'B', 'C', 'D', 'E',
        'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O',
        'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y',
        'Z'
    ]

    res = []

    i = 0
    while i < len(str):
        orig_idx = abc_to_num[str[i]]
        shifted_idx = (orig_idx + shift - i) % 26
        res.append(num_to_abc[shifted_idx])
        i += 1

    return ''.join(res)

for i in range(26):
    print i
    print test_by_index(i, 'CPPJVFZBTJDTAARGYECLIHAYCDR')