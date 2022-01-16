from math import log10

from tools import binary_to_text, single_byte_xor, xor2_crack
from tools_substitution import substitution_crack
from source import BITS, XOR1, XOR2, SUBSTITUTION


if __name__ == '__main__':
    res1 = binary_to_text(BITS)
    for line in res1:
        print(line)

    res2 = single_byte_xor(XOR1, 23)
    print(res2)

    res3 = xor2_crack(XOR2)
    print(res3)

    ngr4 = {}
    with open('ngrams4.txt') as file:
        for line in file.readlines():
            key, val = line.split()
            ngr4[key] = int(val)
        s = sum(ngr4.values())
        for key, val in ngr4.items():
            ngr4[key] = log10(val / s)
        miss = log10(0.01/s)

    res4 = substitution_crack(SUBSTITUTION, ngr4, miss)

    # ADDTHEALILITOTEDETISHERANORINDENSELOALSHALETITSILSTITITIENTISHERSTHEENEISEDINTHETISHERTEYTSHEREHASTWENTOSIYINDESENDENTRANDERLOTHESENRENEALSHALETITSILSTITITIENSATTERNSNEREATHLETTERNRERENGLISHALSHALETITISTLEARTHATOEITANNELENGERRELOENTHESARESIRSLEREITINEENGIESSINGTHEREOLOEYHAISTIMESEARTHWHITHOEISRELALLOISEDTEDETISHERTHESREMIEISSARAGRASHWILLTHEINDEYENTEINTIDENTESTILLWERRASASIGGESTIENOEITANTROTEDIMIDETHERESSAGEINSARTSLOTHENIRLERENTHARATTERSINAREOANDASSLONREZIENTOANALOSISTEEATHENTHERTANOEININDAWAOTEISEHIGHERERDERNREZIENTOSTATISTITSWITHTHISTOSEENTISHERTHENEYTRAGITALWERDWILLTARETETHENEYTLALENUEOLITLOSLASHTWETASITALOTASITALUTASITALLLTASITALOTASITALL

    # TODO https://gist.github.com/hrickards/7142534
    # опробовать утром, вроде понятно
