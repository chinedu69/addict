# packing and unpacking  functions

# packing

def add_no(f1, f2, f3, f4, f5, f6):
    return f1 + f2 + f3 + f4 + f5 + f6


list = [5, 6 , 8 , 7 , 9 , 4]
sum = add_no(*list)
print(sum)

# unpacking

def unpack(*figs):
        for num in figs:
              print(num)

unpack(3, 3, 5, 6, 8, 10, 67, 8)




def unpack(*figs):
        for words in figs:
              print(words)

greetings = ('ohayo', 'gozaimasu', 'magna senpai', 'daijobu?')
unpack(*greetings)


# spreading

line1 = [1, 2, 3, 4, 5, 6, 7, 8, 10]
line2 = [0, 9, 8, 7, 6,]
all_lines = [*line1, *line2]

print('index', 'linez')
for index, all in enumerate(all_lines):
    print(' ',index, '------', all)