import os


def runner(filedir, filename):
    os.system(f'cmd /c "cd {filedir} & python {filename}"')

# m = {
#         'R': 'F'
# }
#
# charen = {
#         'a': 'ƣ',
#         'b': 'ᵹ',
#         'c': 'ʚ',
#         'd': 'ƕ',
#         "e": 'ⱶ',
#         'f': 'ʞ',
#         'g': 'ꬸ',
#         'h': 'ʎ',
#         'i': 'ꬼ',
#         'j': 'ꟿ',
#         'k': 'ꭌ',
#         'l': 'Ƨ',
#         'm': 'Ʊ',
#         'n': 'Ȝ',
#         "o": 'ʘ',
#         'p': 'Ꞝ',
#         'q': 'Ꞟ',
#         'r': 'À',
#         's': 'Ƃ',
#         't': 'अ',
#         'u': 'ब',
#         'v': 'ल',
#         'w': 'त',
#         "x": 'र',
#         'y': '다',
#         'z': '콩',
#         'A': '새',
#         'B': 'ㆅ',
#         'C': 'غ',
#         'D': 'ش',
#         'E': 'ن',
#         'F': 'ض',
#         'G': 'و',
#         'H': 'Д',
#         "I": 'Ж',
#         'J': 'П',
#         'K': 'Ф',
#         'L': 'Ч',
#         'M': 'Э',
#         'N': 'Ю',
#         'O': 'Ѱ',
#         'P': 'Ѫ',
#         'Q': '私',
#         'R': 'Ꞷ',
#         'S': '金',
#         'T': '古',
#         "U": '言',
#         'V': 'ರ',
#         'W': 'ಅ',
#         'X': 'ಜ',
#         'Y': 'ತ',
#         'Z': '೯',
#         "(": 'ಔ',
#         ')': '಄',
#         ':': 'þ',
#         '.': 'ట',
#         ',': 'ణ',
#         '/': 'భ',
#         "\\": '言',
#         '*': '字',
#         '+': '字',
#         '-': 'て',
#         '=': '平',
#         '[': 'た',
#         ']': '見',
#         '{': 'ャ',
#         "}": '암',
#         '"': '햇',
#         "'": '문',
#         '&': '기',
#         '%': '지',
#         '#': '응',
#     }


def encrypt(msg):
        emessage = msg
        alphabets = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
!@#$%^&*()_+}{:"<>?/.,\\=-`~ """
        key = 8
        encrypted = ''
        for i in emessage:
                enc_pos = alphabets.find(i)
                encplus_pos = (enc_pos + key) % len(alphabets)
                encrypted += alphabets[encplus_pos]
        return encrypted


def decrypt(msg):
        dmessage = msg
        alphabets = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
!@#$%^&*()_+}{:"<>?/.,\\=-`~ """
        key = 8
        decrypted = ''
        for i in dmessage:
                dec_pos = alphabets.find(i)
                decplus_pos = (dec_pos - key) % len(alphabets)
                decrypted += alphabets[decplus_pos]
        return decrypted



