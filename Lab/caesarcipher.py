import string

alphabet = string.ascii_letters


def decipher(sentence, param):
    result = ""
    # sentence, param = eval(input("please input the code and key (code in"") :"))
    letter_list = [t for t in sentence]
    for old_letter in letter_list:
        if old_letter in alphabet:
            org_param = alphabet.find(old_letter)
            new_param = (org_param - param) % 26
            new_letter = alphabet[new_param]
            result += new_letter
        else:
            result += old_letter
    return result


print(decipher("Aopz pz h zljyla", 7))
print(decipher("Jupxarcqv jwm Yaxpajvvrwp", 9))
print(decipher("Bzdrzq Bhogdq", 25))
print(decipher("Qrpelcgvat Pnrfne Pvcure", 13))
print(decipher("Mjqqt Btwqi", 5))