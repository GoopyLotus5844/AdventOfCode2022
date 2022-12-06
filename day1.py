from puzzle_input import read
print(max([(sum(elf) if isinstance(elf, list) else int(elf)) for elf in read("input.txt", ['\n\n', '\n'])]))
print(sum(sorted([(sum(elf) if isinstance(elf, list) else int(elf)) for elf in read("input.txt", ['\n\n', '\n'])])[-3:]))