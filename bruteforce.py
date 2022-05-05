from copy import deepcopy

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


def invest2(action_list, action_price, actual_value, action_buy):
    global best
    for action_index in range(len(action_list)):
        if action_index not in action_buy:
            if action_price + action_list[action_index][0] < 500:
                action_price += action_list[action_index][0]
                action_buy.append(action_index)
                actual_value[0].append(action_index)
                actual_value[1] = action_price
                actual_value[2] += (action_list[action_index][1] * action_list[action_index][0]) / 100
                if actual_value[2] > best[2]:
                    best = actual_value
                invest2(action_list, action_price, actual_value, action_buy)


def invest(action_list, action_price, actual_value, action_buy, iter):
    global best
    iter += 1
    action_list = deepcopy(action_list)
    action_price = deepcopy(action_price)
    actual_value = deepcopy(actual_value)
    action_buy = deepcopy(action_buy)
    iter = deepcopy(iter)

    old_value = deepcopy(actual_value)
    old_action_buy = deepcopy(action_buy)
    old_action_price = deepcopy(action_price)

    print("                                   " + str(iter))
    b = 0
    for action_index in range(len(action_list)):
        print("actual_value" + str(actual_value))
        actual_value = old_value
        print("actual_value" + str(actual_value))
        action_buy = old_action_buy
        action_price = old_action_price
        b += 1
        print("boucle" + str(b))
        if action_index not in action_buy:
            if action_price + action_list[action_index][0] < 500:
                action_price += action_list[action_index][0]
                print(action_price)
                actual_value[1] = action_price
                actual_value[2] += (action_list[action_index][1] * action_list[action_index][0]) / 100
                actual_value[0].append(action_index)
                print(actual_value)
                if actual_value[2] > best[2]:
                    best = actual_value
                action_buy.append(action_index)
                invest(action_list, action_price, actual_value, action_buy, iter)

    print("best")
    print(best)
    print("actual_value")
    print(actual_value)
    return best


actual = [[], 0, 0]
best = [[], 0, 0]

print(invest(ACTIONS_LIST, 0, actual, [], 0))
print(best)
