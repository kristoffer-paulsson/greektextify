from greektextify.alphabet import GreekAlphabet

if __name__ == '__main__':
    print("Lower greek alphabet paired with the phonetic alphabet:")
    for key, value in GreekAlphabet.SOUNDS.items():
        print(key, value)