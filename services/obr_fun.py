

def obr(read_ch):
    if len(read_ch) > 2:
        read_ch = int(read_ch[1:], 16)
    else:
        read_ch = int(read_ch)
    return read_ch