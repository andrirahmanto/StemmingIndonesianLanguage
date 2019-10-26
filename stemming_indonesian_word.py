import pandas as pd

def readkamus(namafile):
    text_file = open(namafile, "r")
    lines = text_file.readlines()
    lines2 = []
    for i in lines:
        i = i.replace('\n', '')
        lines2.append(i)
    return lines2

def cekkamus(kata,kamus):
    for i in kamus:
        if i == kata:
            return True
    return False

def pemisahan_prefix(kata,prefix):
    for i in prefix:
        if kata.startswith(i):
            kata = kata[len(i):len(kata)]
            return kata ,i
    return kata, ''

def pemisahan_infix(kata,infix):
    for i in infix:
        if i in kata:
            kata = kata.replace(i,"")
            return kata,i
    return kata, ''

def pemisahan_suffix(kata, suffix):
    for i in suffix:
        if kata.endswith(i):
            kata = kata[0:(len(kata)-len(i))]
            return kata,i
    return kata, ''
def penemuan_kata_dasar(kata,kamus):
    kata = kata.lower()
    simpankatatidakbaku = kata
    ada = cekkamus(kata,kamus)
    if not ada:
        kata, imbuhan = pemisahan_prefix(kata, prefix)
        #print('imbuhannya adalah :', imbuhan)
    else:
        return kata
    ada = cekkamus(kata, kamus)
    if not ada:
        kata,akhiran = pemisahan_suffix(kata,suffix)
        #print('akhirannya adalah :',akhiran)
    else:
        return kata
    ada = cekkamus(kata, kamus)
    if not ada:
        kata, tengahan = pemisahan_infix(kata,infix)
        #print('tengahannya adalah :',tengahan)
    else:
        return kata
    ada = cekkamus(kata, kamus)
    if not ada:
        #print('kata tidak baku')
        return simpankatatidakbaku
    return kata



prefix = ['meng','per','ber','ter','di','ke','se','peng']
suffix = ['kan','an','i']
infix = ['el','er','em']
kamus = readkamus('kata-dasar.txt')
'''
kata  = input()
kata = penemuan_kata_dasar(kata,kamus)
print('kata bakunya adalah :',kata)
'''
kalimat = input().lower()
listkalimat = [str(i) for i in kalimat.split()]
kalimatdasar = []
strkalimatdasar = ''
for i in listkalimat:
    i = penemuan_kata_dasar(i,kamus)
    kalimatdasar.append(i)
    strkalimatdasar = strkalimatdasar + ' ' + i
print(strkalimatdasar)








