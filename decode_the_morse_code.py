#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Decode the Morse code
#Problem level: 6 kyu

def decodeMorse(morseCode):
    return ' '.join([''.join([MORSE_CODE[y] for y in x.split() if y]) for x in morseCode.split('   ') if x])
