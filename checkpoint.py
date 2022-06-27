def find_short_word(array):
    short_array = []
    array.append("invalided_stub_loop")
    q = 0
    for i in range(len(array)):
        if 0 < q < 4:
            short_array.append(array[i - 1])
        q = 0
        for k in array[i]:
            q += 1
            if q > 3:
                q = 0
                break
    print(short_array)


find_short_word(["gg", "hhhh", "kkkk", "g", "ff", "kkkkkk", "hhh", "kk", "l", "h"])
