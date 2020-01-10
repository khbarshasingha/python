def swap_case(s):
    newstring=""
    for letter in s:
        if letter.islower():
            newstring+=letter.upper()
        else:
            newstring+=letter.lower()
    return newstring

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
