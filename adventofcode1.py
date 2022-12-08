all_elves = []
calories = input()
while calories != '':
    all_elves.append([int(s) for s in calories.split()])
    calories = input()
print(all_elves)
