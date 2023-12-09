from collections import Counter
lines = []
with open("input.txt", "r") as file:
    while line := file.readline():
        lines.append(line.strip().split(" "))

card_order = "AKQJT98765432"

# create a list of tuples containing the hand and the bid
# create a function classify_hand that will assign the hand a rank of five of a kind, four of a kind, full house, etc

def classify_hand(lines):
    five_of_a_kind = []
    four_of_a_kind = []
    full_house = []
    three_of_a_kind = []
    two_pair = []
    one_pair = []
    high_card = []

    for i in range(len(lines)):
        hand = sorted(Counter(lines[i][0]).values(), reverse = True)

        if hand[0] == 5:
            five_of_a_kind.append(lines[i])
        elif hand[0] == 4:
            four_of_a_kind.append(lines[i])
        elif hand[0] == 3 and hand[1] == 2:
            full_house.append(lines[i])
        elif hand[0] == 3 and hand[1] == 1:
            three_of_a_kind.append(lines[i])
        elif hand[0] == 2 and hand[1] == 2:
            two_pair.append(lines[i])
        elif hand[0] == 2 and hand[1] == 1:
            one_pair.append(lines[i])
        elif hand[0] == 1:
            high_card.append(lines[i])

    return five_of_a_kind, four_of_a_kind, full_house, three_of_a_kind, two_pair, one_pair, high_card


#[['32T3K', '765'], ['T55J5', '684'], ['KK677', '28'], ['KTJJT', '220'], ['QQQJA', '483']]
five_of_a_kind, four_of_a_kind, full_house, three_of_a_kind, two_pair, one_pair, high_card = classify_hand(lines)

def sort_hands_by_card_order(hands, card_order):
    def hand_key(hand):
        return tuple(card_order.index(card) for card in hand[0])
    return sorted(hands, key=hand_key)

five_of_a_kind = sort_hands_by_card_order(five_of_a_kind, card_order)
four_of_a_kind = sort_hands_by_card_order(four_of_a_kind, card_order)
full_house = sort_hands_by_card_order(full_house, card_order)
three_of_a_kind = sort_hands_by_card_order(three_of_a_kind, card_order)
two_pair = sort_hands_by_card_order(two_pair, card_order)
one_pair = sort_hands_by_card_order(one_pair, card_order)
high_card = sort_hands_by_card_order(high_card, card_order)

cards = five_of_a_kind + four_of_a_kind + full_house + three_of_a_kind + two_pair + one_pair + high_card
cards = cards[::-1]
print(four_of_a_kind)

total = 0
for i, hand in enumerate(cards):
    total = total + (i + 1) * int(hand[1])

print(total)
