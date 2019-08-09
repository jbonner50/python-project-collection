def get_input():
    rotors = list(map(int, input("Rotors:").split(",")))
    positions = input("Positions:").split(",")
    word = input("Word:")
    return rotors, positions, word


def start(rotors, positions, word):
    base_rotors = [
        "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "BDFHJLCPRTXVZNYEIWGAKMUSQO",
        "ESOVPZJAYQUIRHXLNFTGKDCMWB",
        "VZBRGITYUPSDNHLXAWMJQOFECK",
    ]
    reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    notches = ["Q", "E", "V", "J", "Z"]
    converted_positions = list(map(to_int, positions))
    converted_notches = [base_rotors[i-1][to_int(notches[i-1])] for i in rotors]
    chosen_rotors = [base_rotors[i-1] for i in rotors]
    rotated_rotors = [rotor[position:]+rotor[:position]
                      for rotor, position in zip(chosen_rotors, converted_positions)]
    return enigma(word, rotated_rotors, reflector, converted_notches)


def to_int(char):
    return ord(char)-ord("A")


def to_char(i):
    return chr(i+ord("A"))


def rotor_substitute(char, rotor):
    return rotor[ord(char)-ord("A")]


def rotor_reverse_substitute(char, rotor):
    return chr(rotor.index(char)+ord("A"))


def substitute(char, rotors, reflector):
    for rotor in rotors:
        char = rotor_substitute(char, rotor)
    char = rotor_substitute(char, reflector)
    for rotor in reversed(rotors):
        char = rotor_reverse_substitute(char, rotor)
    return char


def rotate(rotor):
    return rotor[1:]+rotor[:1]


def rotate_all(rotors, notches):
    if rotors[0][0] == notches[0]:
        rotors[1] = rotate(rotors[1])
    elif rotors[1][0] == notches[1]:
        rotors[1] = rotate(rotors[1])
        rotors[2] = rotate(rotors[2])
    rotors[0] = rotate(rotors[0])


def enigma(word, rotors, reflector, notches):
    new_word = ""
    for char in word:
        rotate_all(rotors, notches)
        new_word += substitute(char, rotors, reflector)
    return new_word

if __name__ == "__main__":
    while True:
        print(start(*get_input()))