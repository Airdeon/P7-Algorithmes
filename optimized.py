from datetime import datetime
from operator import itemgetter
import csv

ACTIONS_LIST = [
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


def invest_dynamique_less_precision(max_price, actions_list):
    # calcul action gain ((value * pourcentage) / 100)
    delete_list = []
    for index in range(len(actions_list)):
        if actions_list[index][1] <= 0 or actions_list[index][2] <= 0:
            delete_list.append(index)
        else:
            actions_list[index][2] = (actions_list[index][2] * actions_list[index][1]) / 100
            # price in Integer
            actions_list[index][1] = round(actions_list[index][1])
    # deletion of unnecessary actions
    for index in sorted(delete_list, reverse=True):
        del actions_list[index]

    # build matrix
    matrix = [[0 for x in range(max_price + 1)] for x in range(len(actions_list) + 1)]

    # populate matrix
    for action in range(1, len(actions_list) + 1):
        for price in range(1, max_price + 1):
            if actions_list[action - 1][1] <= price:
                matrix[action][price] = max(actions_list[action - 1][2] + matrix[action - 1][price - actions_list[action - 1][1]], matrix[action - 1][price])
            else:
                matrix[action][price] = matrix[action - 1][price]

        action_number = len(actions_list)
        action_buy = []
        total_price = 0

    # find best combo
    while max_price >= 0 and action_number >= 0:
        e = actions_list[action_number - 1]
        if matrix[action_number][max_price] == matrix[action_number - 1][max_price - e[1]] + e[2]:
            action_buy.append(e[0])
            total_price += e[1]
            max_price -= e[1]
        action_number -= 1

    return [action_buy, (total_price), matrix[-1][-1]]


def invest_dynamique(max_price, actions_list):
    # calcul action gain ((value * pourcentage) / 100)
    delete_list = []
    for index in range(len(actions_list)):
        if actions_list[index][1] <= 0 or actions_list[index][2] <= 0:
            delete_list.append(index)
        else:
            actions_list[index][2] = (actions_list[index][2] * actions_list[index][1]) / 100
            # price in Integer
            actions_list[index][1] = int(actions_list[index][1] * 100)
    # deletion of unnecessary actions
    for index in sorted(delete_list, reverse=True):
        del actions_list[index]
    max_price *= 100

    # build matrix
    matrix = [[0 for x in range(max_price + 1)] for x in range(len(actions_list) + 1)]

    # populate matrix
    for action in range(1, len(actions_list) + 1):
        for price in range(1, max_price + 1):
            if actions_list[action - 1][1] <= price:
                matrix[action][price] = max(actions_list[action - 1][2] + matrix[action - 1][price - actions_list[action - 1][1]], matrix[action - 1][price])
            else:
                matrix[action][price] = matrix[action - 1][price]

        action_number = len(actions_list)
        action_buy = []
        total_price = 0

    # find best combo
    while max_price >= 0 and action_number >= 0:
        e = actions_list[action_number - 1]
        if matrix[action_number][max_price] == matrix[action_number - 1][max_price - e[1]] + e[2]:
            action_buy.append(e[0])
            total_price += e[1]
            max_price -= e[1]
        action_number -= 1

    return [action_buy, (total_price / 100), matrix[-1][-1]]


def glouton(actions_list):
    # deletion of unnecessary actions
    delete_list = []
    for index in range(len(actions_list)):
        if actions_list[index][1] <= 0 or actions_list[index][2] <= 0:
            delete_list.append(index)
    for index in sorted(delete_list, reverse=True):
        del actions_list[index]

    # sort by gain ratio
    gain_price = []
    index = 0
    buy_action = [[], 0, 0]
    for action in actions_list:
        gain_price.append([index, (action[2] * action[1] / 100) / action[1]])
        index += 1
    action_list_sorted_by_gain_ratio = sorted(gain_price, key=itemgetter(1), reverse=True)

    # Buy the best actions until max price
    for action_index in action_list_sorted_by_gain_ratio:
        if buy_action[1] + actions_list[action_index[0]][1] < 500:
            buy_action[0].append(actions_list[action_index[0]][0])
            buy_action[1] += actions_list[action_index[0]][1]
            buy_action[2] += (actions_list[action_index[0]][1] * actions_list[action_index[0]][2]) / 100

    return buy_action


best = [[], 0, 0]


def read_csv(file):
    """ Read CSV File and make list with float number """
    with open(file, newline="") as csvfile:
        csv_read = csv.reader(csvfile)
        actions_list = list(csv_read)
        del actions_list[0]
        for index in range(len(actions_list)):
            actions_list[index][1] = float(actions_list[index][1])
            actions_list[index][2] = float(actions_list[index][2])
        return actions_list


def main():
    action_list = read_csv("dataset2_Python+P7.csv")
    start = datetime.now()  # start time counter

    # Lancement de l'algorithme Glouton
    # result = glouton(action_list)

    # Lancement de l'algorithme Programmation dynamique
    result = invest_dynamique(500, action_list)

    # Lancement de l'algorithme Programmation dynamique avec une précision reduite
    # result = invest_dynamique_less_precision(500, action_list)

    end = datetime.now()  # end time counter
    temps = end - start
    print("Nom des actions à acheter : " + str(result[0]))
    print("Montant total des actions : " + str(result[1]))
    print("Gain total des actions apres 2 ans : " + str(round(result[2], 2)))
    print("duré du calcule : " + str(round(temps.total_seconds(), 2) * 1000) + "ms")


if __name__ == "__main__":
    main()
