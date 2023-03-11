# Тестовые данные.
TEST_DATA = [
    (44, 'success', True),
    (16, 'failure', True),
    (4, 'success', False),
    (21, 'failure', False),
]

BONUS = 1.1
ANTIBONUS = 0.8

def add_rep(current_rep, rep_points, buf_effect):
    current_rep += rep_points
    if buf_effect:
        return current_rep * BONUS
    return current_rep

def remove_rep(current_rep, rep_points, debuf_effect):
    current_rep -= rep_points
    if debuf_effect:
        return current_rep * ANTIBONUS
    return current_rep

def main(duel_res):
    current_rep = 0.0
    for rep, result, effect in duel_res:
        if result == 'success':
            current_rep = add_rep(current_rep, rep, effect)
        if result == 'failure':
            current_rep = remove_rep(current_rep, rep, effect)
    return f'После {len(duel_res)} поединков, репутация персонажа — {current_rep:.3f} очков.'


# Тестовый вызов функции main.
print(main(TEST_DATA))