import socket
import struct
import csv
import sys

def find_map(intt):
    say=1
    with open('IpToCountry.csv') as csv_file:
        for line in csv_file:
            if say <=329:
                say = say+1
            else:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if intt<=int(row[1]) and intt>=int(row[0]):
                        return (row[4],row[5],row[6])
                        break
                    else:
                        pass



def ip2int(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]


def main():
    host = str(sys.argv[1])
    print(f"IP : {host}")
    int_ip=ip2int(host)
    try:
        [kisaltma,kisaltma2,ulke]=find_map(int_ip)
        print(f"Ülke : {kisaltma},{ulke}")
    except:
        print("Lütfen Geçerli Bir IP Giriniz.")

if __name__ == '__main__':
    main()

