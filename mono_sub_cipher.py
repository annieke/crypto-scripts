import operator
# returns a dictionary mapping character to its frequency in the string
# params: string
def count_freqs(str):
    char_counts = {}
    for char in str:
        if char_counts.has_key(char):
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

# returns str after changing each letter to the letter it's mapped to in map
# params: string, dictionary<character, character>
def exchange_letters(str, char_map):
    str_list = list(str)

    for i in range(len(str_list)):
        if char_map.has_key(str_list[i]):
            str_list[i] = char_map[str_list[i]]

    return ''.join(str_list)

encoded_str = """RHINT TLHYF EIXQF AXTNK AFYFV QTRNF EHFEI XQFAD 
                 TXXTE ZAFBA IRRHI NTLQR IAIMT EQNIA ITEFR HINTM 
                 IASGI NXSET EIACR HINTX EIARH FEXRT EOQNT RNFMH 
                 IAUKT ICWSI EXTET CQAKI BXKFE ATNIY QGFEA QISAQ 
                 XTCRX IXTRQ XBIRG FSACT CQADU XTRYI MFXFE RNTFI 
                 ACGFE MTEHI UHIYT AXETH ETATS ETYFA MSRZB QXKXK 
                 TVFIY FGNET IXQAV XKTXT NKAFY FVQTR XFETC SNTRH 
                 INTXE IARHF EXIXQ FANFR XRIAC TAIDY TXKTN FYFAQ 
                 JIXQF AFGMI ERQXK IRCTO TYFHT CXKTG IYNFA QIACG 
                 IYNFA QLYIS ANKOT KQNYT RDFXK CTRQV ATCXF DTETS 
                 RIDYT IACXK TCEIV FARHI NTNEI GXBKQ NKQRG YFBAQ 
                 AXFFE DQXDU XKTGI YNFAQ LYISA NKOTK QNYTX FRSHH 
                 YUXKT QAXTE AIXQF AIYRH INTRX IXQFA QRRBQ XKNIE 
                 VFIMI AATCO TERQF AFGCE IVFAQ RQACT OTYFH MTAXR 
                 HINTL QRGSA CTCDU VFOTE AMTAX RSDRQ CQTRI ACNFA 
                 XEINX RBQXK MSYXQ HYTTA XQXQT RRHIN TLRIN KQTOT 
                 MTAXR QANYS CTXKT GQERX HEQOI XTYUG SACTC YQWSQ 
                 CHEFH TYYIA XEFNZ TXGIY NFAXF ETINK FEDQX XKTGQ 
                 ERXHE QOIXT YUGSA CTCNF MHIAU XFRSN NTRRG SYYUY 
                 ISANK FEDQX IACET NFOTE IRHIN TNEIG XCEIV FAIAC 
                 XKTGQ ERXHE QOIXT NFMHI AUXFR TACIR HINTN EIGXC 
                 EIVFA XFXKT QRRXK TYISA NKFGR TROQQ QBIRX KTGQE 
                 RXRHI NTLCT YQOTE UQAXF VTFRU ANKEF AFSRF EDQXB 
                 KQYTX KTYIS ANKFG XKTCT THRHI NTNYQ MIXTF DRTEO 
                 IXFEU CRNFO EBIRX KTNFM HIAUR GQERX CTYQO TEUDT 
                 UFACT IEXKF EDQXQ ARTHX TMDTE RHINT LRNTF TYFAM 
                 SRZSA OTQYT CXKTQ AXTEH YIATX IEUXE IARHF EXRUR 
                 XTMHE FVEIM IAIMD QXQFS RHEQO IXTYU GSACT CQAQX 
                 QIXQO TXFCT OTYFH RHINT OTKQN YTRGF ESRTQ AQAXT 
                 EHYIA TXIEU NFYFA QJIXQ FAGYI VHETH IETUF SENFH 
                 UFGKQ XNKKQ ZTERV SQCTX FXKTV IYILU"""

# Letter freqs in order: ETAOINSRHLDCUMFPGWYBVKXJQZ

char_map_test = {
    'T': 'E', 'I': 'A', 'X': 't', 'F': 'o', 'A': 'i',
    'Q': 'n', 'R': 'S', 'E': 'r', 'N': 'C', 'Y': 'l',
    'H': 'P', 'K': 'C', 'C': 'u', 'S': 'm', 'G': 'f',
    'U': 'd', 'O': 'g', 'M': 'w', 'D': 'y', 'V': 'b',
    'B': 'v', 'L': 'k', 'Z': 'x', 'W': 'j', 'J': 'q'
}

# print a representation of the dictionary sorted by keys
print sorted(count_freqs(encoded_str).items(), key=operator.itemgetter(1))
print exchange_letters(encoded_str, char_map_test)