index = 1
counter_before = 4
counter_after = 0
while index < 6:
    print((str(".")*counter_before) + str(index) + (str(".")*counter_after))
    index = index + 1
    counter_before = counter_before - 1
    counter_after = counter_after + 1
    