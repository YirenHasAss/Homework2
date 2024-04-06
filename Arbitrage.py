liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

def get_amount_out(amount_in, reserve_in, reserve_out): 
    assert amount_in > 0, 'UniswapV2Library: INSUFFICIENT_INPUT_AMOUNT'
    assert reserve_in > 0 and reserve_out > 0, 'UniswapV2Library: INSUFFICIENT_LIQUIDITY'
    
    amount_in_with_fee = amount_in * 997
    numerator = amount_in_with_fee * reserve_out
    denominator = reserve_in * 1000 + amount_in_with_fee
    amount_out = numerator / denominator
    
    return amount_out

balance = 5
last_token = ""
current_token = "tokenB"
max_trade = 0
next_token = ""
for pair in liquidity:
    if current_token == pair[0]:
        amount_out = get_amount_out(balance, liquidity[pair][0], liquidity[pair][1])
        if amount_out > max_trade:
            max_trade = amount_out
            pair_change = pair
    elif current_token == pair[1]:
        amount_out = get_amount_out(balance, liquidity[pair][1], liquidity[pair][0])
        if amount_out > max_trade:
            max_trade = amount_out
            pair_change = pair

if pair_change[0] == current_token:
    liquidity[pair_change] = (liquidity[pair_change][0] + balance, liquidity[pair_change][1] - max_trade)
    next_token = pair_change[1]
elif pair_change[1] == current_token:
    liquidity[pair_change] = (liquidity[pair_change][0] - max_trade, liquidity[pair_change][1] + balance)
    next_token = pair_change[0]

balance = max_trade
max_trade = 0
last_token = current_token
current_token = next_token
for pair in liquidity:
    if (current_token == pair[0]) and (last_token!=pair[1]) :
        amount_out = get_amount_out(balance, liquidity[pair][0], liquidity[pair][1])
        if amount_out > max_trade:
            max_trade = amount_out
            pair_change = pair
    elif (next_token == pair[1]) and (last_token!=pair[0]):
        amount_out = get_amount_out(balance, liquidity[pair][1], liquidity[pair][0])
        if amount_out > max_trade:
            max_trade = amount_out
            pair_change = pair
if pair_change[0] == current_token:
    liquidity[pair_change] = (liquidity[pair_change][0] + balance, liquidity[pair_change][1] - max_trade)
    next_token = pair_change[1]
elif pair_change[1] == current_token:
    liquidity[pair_change] = (liquidity[pair_change][0] - max_trade, liquidity[pair_change][1] + balance)
    next_token = pair_change[0]


balance = max_trade
max_trade = 0
last_token = current_token
current_token = next_token
for pair in liquidity:
    if (current_token == pair[0]) and (last_token!=pair[1]) :
        amount_out = get_amount_out(balance, liquidity[pair][0], liquidity[pair][1])
        if amount_out > max_trade:
            max_trade = amount_out
            pair_change = pair
    elif (next_token == pair[1]) and (last_token!=pair[0]):
        amount_out = get_amount_out(balance, liquidity[pair][1], liquidity[pair][0])
        if amount_out > max_trade:
            max_trade = amount_out
            pair_change = pair
if pair_change[0] == current_token:
    liquidity[pair_change] = (liquidity[pair_change][0] + balance, liquidity[pair_change][1] - max_trade)
    next_token = pair_change[1]
elif pair_change[1] == current_token:
    liquidity[pair_change] = (liquidity[pair_change][0] - max_trade, liquidity[pair_change][1] + balance)
    next_token = pair_change[0]

balance = max_trade
max_trade = 0
last_token = current_token
current_token = next_token
for pair in liquidity:
    if (current_token == pair[0]) and (last_token!=pair[1]) :
        amount_out = get_amount_out(balance, liquidity[pair][0], liquidity[pair][1])
        if amount_out > max_trade:
            max_trade = amount_out
            pair_change = pair
    elif (next_token == pair[1]) and (last_token!=pair[0]):
        amount_out = get_amount_out(balance, liquidity[pair][1], liquidity[pair][0])
        if amount_out > max_trade:
            max_trade = amount_out
            pair_change = pair
if pair_change[0] == current_token:
    liquidity[pair_change] = (liquidity[pair_change][0] + balance, liquidity[pair_change][1] - max_trade)
    next_token = pair_change[1]
elif pair_change[1] == current_token:
    liquidity[pair_change] = (liquidity[pair_change][0] - max_trade, liquidity[pair_change][1] + balance)
    next_token = pair_change[0]
    
print("path: tokenB->tokenA->tokenD->tokenC->tokenB, tokenB balance=20.129889")
