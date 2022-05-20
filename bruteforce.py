from copy import deepcopy
from datetime import datetime

ACTIONS_LIST2 = [
    ["action 1", 20, 5],
    ["action 2", 30, 10],
    ["action 3", 50, 15],
    ["action 4", 70, 20],
    ["action 5", 60, 17],
    ["action 6", 80, 25],
    ["action 7", 22, 7],
    ["action 8", 26, 11],
    ["action 9", 48, 13],
    ["action 10", 34, 27],
    ["action 11", 42, 17],
    ["action 12", 110, 9],
    ["action 13", 38, 23],
    ["action 14", 14, 1],
    ["action 15", 18, 3],
    ["action 16", 8, 8],
    ["action 17", 4, 12],
    ["action 18", 10, 14],
    ["action 19", 24, 21],
    ["action 20", 114, 18],
]

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


def invest2(action_list, actual_value):
    global best
    if len(actual_value[0]) == 0:
        last = 0
    else:
        last = int(actual_value[0][-1][7:]) - 1
    for action_index in range(last, len(action_list)):

        if action_list[action_index][0] not in actual_value[0]:
            if actual_value[1] + action_list[action_index][1] < 500:
                actual_value[0].append(action_list[action_index][0])
                actual_value[1] += action_list[action_index][1]
                actual_value[2] += (action_list[action_index][2] * action_list[action_index][1]) / 100

                if actual_value[2] > best[2]:
                    best = deepcopy(actual_value)

                invest2(action_list, actual_value)

                del actual_value[0][-1]

                actual_value[1] -= action_list[action_index][1]
                actual_value[2] -= (action_list[action_index][2] * action_list[action_index][1]) / 100
    return best


def invest(action_list, actual_value):
    global best
    if len(actual_value[0]) == 0:
        last = 0
    else:
        last = actual_value[0][-1]
    for action_index in range(last, len(action_list)):
        if action_index not in actual_value[0]:
            if actual_value[1] + action_list[action_index][0] < 500:
                actual_value[0].append(action_index)
                actual_value[1] += action_list[action_index][0]
                actual_value[2] += (action_list[action_index][1] * action_list[action_index][0]) / 100
                if actual_value[2] > best[2]:
                    best = deepcopy(actual_value)
                invest(action_list, actual_value)
                del actual_value[0][-1]
                actual_value[1] -= action_list[action_index][0]
                actual_value[2] -= (action_list[action_index][1] * action_list[action_index][0]) / 100
    return best


best = [[], 0, 0]


def main():
    start = datetime.now()  # start time counter
    actual = [[], 0, 0]
    """result = invest(ACTIONS_LIST, actual)
    for index in range(len(result[0])):
        best[0][index] += 1"""
    result = invest2(ACTIONS_LIST2, actual)
    end = datetime.now()
    temps = end - start
    print("Numero des actions à acheter : " + str(result[0]))
    print("Montant total des actions : " + str(result[1]))
    print("Gain total des actions apres 2 ans : " + str(round(result[2], 2)))
    print("duré du calcule : " + str(round(temps.total_seconds() * 1000)) + "ms")


if __name__ == "__main__":
    main()
