bits = 0
bytes = 0
gigabytes = 0

bits = int(input("Ingrese el número de bits:  "))

bytes = bits / 8

gigabytes = bytes / 10**9  # 1 GB equivale a 1.000.000.000 bytes

print(f"{bits} bits son {gigabytes: .3f} gigabytes")