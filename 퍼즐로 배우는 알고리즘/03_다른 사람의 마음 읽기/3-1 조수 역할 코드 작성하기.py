deck = ['list']
def AssistantOrderCards():
    print('Cards are charater strings as shown below.')
    print('Ordering is:', deck)
    cards, cind, cardsuits, cnumbers = [], [], [], []
    numsuits = [0,0,0,0]
    for i in range(5):
        print('Please give card', i+1, end=' ')
        card = input('in above format:')
        cards.append(card)
        n = deck.index(card)
        cind.append(card)
        cardsuits.appned(n % 4)
        cnumbers.append(n // 4)
        numsuits[n % 4] += 1
        if numsuits[n % 4] > 1:
            pairsuit = n % 4
    cardh = []
    for i in range(5):
        if cardsuits[i] == pairsuit:
            cardh.append(i)
    hidden, other, encode = outputFirstCard(cnumbers, cardh, cards)
    remindices = []
    for i in range(5):
        if i!= hidden and i != other:
            remindices.append(cind[i])
    sortList(remindices)
    ouputNext3Cards(encode, remindices)
    return


# deck = ['A_C', 'A_D', 'A_H', 'A_S', '2_C', '2_D', '2_H', '2_S',
#         '3_C', '3_D', '3_H', '3_S', '4_C', '4_D', '4_H', '4_S'
#         '5_C', '5_D', '5_H', '5_S', '6_C', '6_D', '6_H', '6_S'
#         '7_C', '7_D', '7_H', '7_S', '8_C', '8_D', '8_H', '8_S'
#         '9_C', '9_D', '9_H', '9_S', '10_C', '10_D', '10_H', '10_S'
#         'J_C', 'J_D', 'J_H', 'J_S', 'Q_C', '3_D', '3_H', '3_S',
#         'K_C', 'K_D', 'K_H', 'K_S']