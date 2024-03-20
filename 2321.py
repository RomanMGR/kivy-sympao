data = hex(int(25 * 100))
if len(data) % 2 == 1:
    data = data[:-1] + '0' + data[-1]
print(data)
print(bytearray.fromhex(data))