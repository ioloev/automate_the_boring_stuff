# https://stackoverflow.com/questions/60658830/automate-the-boring-stuff-coin-flip-streaks
import random

number_of_streaks = 0
number_of_experiments = 10000
DEBUG = 0  # print out coins list, match-highlighted list and position where first streak occurs

# convert first streak occurrence to upper
def highlight(lst, position):
    modified_list = lst[:position]
    for i in range(6):
        modified_list.append(lst[position + i].upper())
    modified_list.extend(lst[position + 6:])
    return modified_list


for experiment_number in range(number_of_experiments):
    coin_flips = []
    for i in range(100):  # fill list with random Heads and Tails
        coin = random.randint(0, 1)
        if coin == 1:
            coin_flips.append("t")
        else:
            coin_flips.append("h")

    if DEBUG == 1:
        print()
        print(coin_flips)
    in_a_row = 1
    for i in range(len(coin_flips)-1):
        if coin_flips[i] == coin_flips[i+1]:
            in_a_row += 1
            if in_a_row == 6:
                number_of_streaks += 1
                if DEBUG == 1:
                    found_position = i - 4  # we find out that 6 in a row at list[4] position, at fact 5th position
                    print(highlight(coin_flips, found_position))
                    print("Streak at {} position\n".format(found_position))
                break  # found first streak, no need to check more, go to next coins list
        else:
            in_a_row = 1

print("Streaks: "+str(number_of_streaks))
print('Chance of streak: {}%%'.format(number_of_streaks / number_of_experiments * 100))
