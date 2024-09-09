#!/usr/bin/env python

import scapy.all as scapy
import optparse

def dapetargumen_nuz():
    parser = optparse.OptionParser()
    parser.add_option("--kepo", dest="target", help="alamat IP doi/jangkauannya")
    (optns, argmnts) = parser.parse_args()
    if not optns.target:
        parser.error("Masukkan Alamat IP doi/jangkauannya yang ingin dikepoin! misal: --kepo 192.168.78.1/24")
    return optns

def pindai_nuz(ip):
    minta_arp = scapy.ARP(pdst=ip)
    penyiaran = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    minta_arp_penyiaran = penyiaran/minta_arp
    daftar_terjawab = scapy.srp(minta_arp_penyiaran, timeout=1, verbose=False)[0]


    daftarklien = []
    for elemen in daftar_terjawab:
        kamusklien = {"IP": elemen[1].psrc, "MAC": elemen[1].hwsrc}
        daftarklien.append(kamusklien)
    return daftarklien

def tampilhasil_nuz(hasildaftar):
    print("\n\nHASIL KEPO NETWORK\n________________________________________\n\nAlamat IP\t\tAlamat MAC\n________________________________________\n")
    for klien in hasildaftar:
        print(klien["IP"] + "\t\t" + klien["MAC"])

optns = dapetargumen_nuz()
hasilpindai = pindai_nuz(optns.target)
tampilhasil_nuz(hasilpindai)

penutupan = '''
    dibuat dengan niat oleh 
     ______   _ _   _ _   _ _______________
    |__  / | | | \ | | | | |__  /__  /__  /
      / /| | | |  \| | | | | / /  / /  / / 
     / /_| |_| | |\  | |_| |/ /_ / /_ / /_ 
    /____|\___/|_| \_|\___//____/____/____|

    https://steamcommunity.com/id/zunuzzz/
    
    =========GUNAKAN DENGAN BIJAK=========
    '''

print(penutupan)

