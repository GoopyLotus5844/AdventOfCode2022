import math

data = open("input.txt", "r").read().split('\n')

char_to_value = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}
char_order = ['0', '1', '2', '=', '-']

def parse_snafu(str):
    total = 0
    for i in range(len(str)):
        base = 5 ** (len(str) - i - 1)
        total += base * char_to_value[str[i]]
    return total

def get_snafu(num):
    log_5 = math.ceil(math.log(num) / math.log(5))
    if num <= (5 ** log_5) // 2: log_5 -= 1

    result = char_order[num % 5]
    for i in range(1, log_5 + 1):
        offset = (5 ** i) // 2
        result = char_order[((num + offset) // (5 ** i)) % 5] + result
    return result

total = 0
for line in data:
    total += parse_snafu(line)

print(total)
print(get_snafu(total))
print(parse_snafu('2--1=0=-210-1=00=-=1'))