from random import choice
from datetime import datetime

GAME_CHOICES = {'r': 'Rock', 'p': "Paper", 's': "Scissors"}
overall_results = {'user': 0, 'system': 0}
POLICY = {('p', 'r'): 'p', ('p', 's'): 's', ('r', 's'): 'r'}
result = {'user': 0, 'system': 0}


def find_winner(user, system):
    if user == system:
        print('Equal')
        return None
    winner = POLICY[ tuple(sorted([user, system])) ]
    return 'user' if winner == user else 'system'


def update_results(winner):
    if winner is None:
        return
    result[winner] += 1
    print('user:{} \t system:{} \t {} won!'.format(result['user'], result['system'], winner))


def rps():
    global count
    users_choice = input('Enter your choice \n (r or p or s):')
    if users_choice == '0':
        return
    if users_choice not in GAME_CHOICES.keys():
        print('Please enter a valid choice!')
        return rps()
    count += 1
    systems_choice = choice(list(GAME_CHOICES.keys()))
    winner = find_winner(users_choice, systems_choice)
    update_results(winner)
    if count < 3:
        rps()
    elif count == 3:
        if result['user'] > result['system']:
            overall_results['user'] += 1
        elif result['system'] > result['user']:
            overall_results['system'] += 1
        result['user'] = 0
        result['system'] = 0
        print('overall results up to now \n user:{} \t system:{}'.format(overall_results['user'], overall_results['system']))
        cntinue = input('Game finished. Wanna play again? (y/n) :')
        if cntinue == 'y':
            count = 0
            rps()
        else:
            return


begin_time = datetime.now()
print('-> Enter 0 in case you want to exit')
count = 0
rps()
delta = str(datetime.now() - begin_time)
print('You played for :', delta.split(':')[1] + ':' + delta.split(':')[2].split('.')[0])
