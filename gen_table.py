from prettytable import PrettyTable

def main():
    generate_table()


def generate_table():

    x = PrettyTable()

    #x.field_names = ["Allowlist Method", "Required by mid-October"]
    #x.add_row(["Open Internet / No Allowlisting ","No Updates Required"])
    #x.add_row(["Domain Allowlisting","Allow *.goto.com - found in the *Universally Required Allowlisting section - if not previously allowed "])
    #x.add_row(["IP-Range Allowlisting","All IP-range blocks in the bottom section called:   server / Data Center IP addresses for use in firewall configurations - please note: the IP range blocks are not new and if all were previously allowed, no further changes are needed"])
    #x.add_row(["Domain and IP-Range Allowlisting","1. Allow *.goto.com - found in the *Universally Required Allowlisting section- if not previously allowed and 2. All IP-range blocks in the bottom section called: server / Data Center IP addresses for use in firewall configurations - please note: the IP range blocks are not new and if all were previously allowed, no further changes are needed "])

    #print(x)

    x.field_names = ["Allowlisting Method ", "Required by mid-October"]

    x.add_row(["Open Internet\n No Allowlisting ", "No Updates Required"])

    print(x)



if __name__ == '__main__':
    main()


    