def encode(self, strs: List[str]) -> str:
    encoded_str = ''
    for word in strs:
        encoded_str += str(len(word)) + '-' + word
    return encoded_str

def decode(self, s: str) -> List[str]:
    decoded_words = []
    begin = 0 # tracker
    while begin < len(s):
        end = begin
        while s[end] != '-':
            end += 1 # we are searching for our delimiter...
        length = int(s[begin:end]) # get length of an encoded word
        begin = end + 1 # shift the rightmost pointer to start of word
        end = begin + length # shift leftmost pointer to the end of that word
        decoded_words.append(s[begin:end]) # add word
        begin = end # set them two trackers to the same position
    return decoded_words



