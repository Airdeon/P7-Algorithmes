from copy import deepcopy
from time import time

ACTIONS = {
    "action1": [20, 5],
    "action2": [30, 10],
    "action3": [50, 15],
    "action4": [70, 20],
    "action5": [60, 17],
    "action6": [80, 25],
    "action7": [22, 7],
    "action8": [26, 11],
    "action9": [48, 13],
    "action10": [34, 27],
    "action11": [42, 17],
    "action12": [110, 9],
    "action13": [38, 23],
    "action14": [14, 1],
    "action15": [18, 3],
    "action16": [8, 8],
    "action17": [4, 12],
    "action18": [10, 14],
    "action19": [24, 21],
    "action20": [114, 18],
}
ACTIONS_LIST = [
    [20, 5],
    [30, 10],
    [50, 15],
    [70, 20],
    [60, 17],
    [80, 25],
    [22, 7],
    [26, 11],
    [48, 13],
    [34, 27],
    [42, 17],
    [110, 9],
    [38, 23],
    [14, 1],
    [18, 3],
    [8, 8],
    [4, 12],
    [10, 14],
    [24, 21],
    [114, 18],
]
TRY_LIST = [
    [30, 10],
    [50, 15],
    [70, 20],
    [60, 17],
    [80, 25],
    [26, 11],
    [48, 13],
    [34, 27],
    [42, 17],
    [110, 9],
    [38, 23],
    [4, 12],
    [10, 14],
    [24, 21],
    [114, 18],
]


"""def invest2(action_list, actual_value):
    global best
    global action_test
    old_actual_value = deepcopy(actual_value)
    for action_index in range(len(action_list)):
        action_test += 1
        print(action_test)
        new_actual_value = old_actual_value
        if action_index not in new_actual_value[0]:
            if new_actual_value[1] + action_list[action_index][0] < 500:
                new_actual_value[1] += action_list[action_index][0]
                new_actual_value[0].append(action_index)
                new_actual_value[2] += (action_list[action_index][1] * action_list[action_index][0]) / 100
                if new_actual_value[2] > best[2]:
                    best = new_actual_value
                invest(action_list, new_actual_value)

                del new_actual_value[0][-1]
                new_actual_value[1] -= action_list[action_index][0]
                new_actual_value[2] -= (action_list[action_index][1] * action_list[action_index][0]) / 100"""


def invest(action_list, actual_value, best):
    global action_test
    if len(actual_value[0]) == 0:
        last = 0
    else:
        last = actual_value[0][-1]
    for action_index in range(last, len(action_list)):
        if action_index not in actual_value[0]:
            if actual_value[1] + action_list[action_index][0] < 500:
                action_test += 1
                print(action_test)
                actual_value[1] += action_list[action_index][0]
                actual_value[0].append(action_index)
                actual_value[2] += (action_list[action_index][1] * action_list[action_index][0]) / 100
                print(actual_value[2])
                print(best[2])
                if actual_value[2] > best[2]:
                    print("best beford")
                    print(best)
                    best = actual_value
                    print("best")
                    print(best)
                print("actual")
                print(actual_value)
                invest(action_list, actual_value, best)

                del actual_value[0][-1]
                actual_value[1] -= action_list[action_index][0]
                actual_value[2] -= (action_list[action_index][1] * action_list[action_index][0]) / 100

    return best


action_test = 0
actual = [[], 0, 0]


def main():
    best = [[], 0, 0]
    start = time()  # start time counter
    print(invest(TRY_LIST, actual, best))
    end = time()
    temps = int(end - start)
    print("duré du calcule : " + str(temps) + "s")


if __name__ == "__main__":
    main()
