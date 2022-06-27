def find_short_word(array):
    short_array = []
    array.append("invalided_stub_loop")
    count_char = 0
    for count_word in range(len(array)):
        if 0 < count_char < 4:
            short_array.append(array[count_word - 1])
        count_char = 0
        for loop_char in array[count_word]:
            count_char += 1
            if count_char > 3:
                count_char = 0
                break
    print(short_array)


find_short_word(["gg", "hhhh", "kkkk", "g", "ff", "kkkkkk", "hhh", "kk", "l", "h"])
