tokens = ["tokenA", "tokenB", "tokenC", "tokenD", "tokenE"]
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

dist = { }
edges = { }
paths = { }
balances = { }

for token in tokens:
    dist[token] = 0
    paths[token] = []
    balances[token] = []



for((u, v), (amount1, amount2)) in liquidity.items(): 
    edges[(u, v)] = amount2/amount1
    edges[(v, u)] = amount1/amount2

def find_arbitrage(startToken = "tokenB", amountIn = 5):
    dist[startToken] = 0
    paths[startToken].append(startToken)
    balances[startToken].append(amountIn)
    dist[startToken] = amountIn

    for _ in range(len(tokens)):
        for (u, v) in edges:
            if v in paths[u]: 
                continue
            if dist[u] * edges[(u, v)] > dist[v]:
                dist[v] = dist[u] * edges[(u, v)]
                paths[v] = paths[u] + [v]
                balances[v] = balances[u] + [dist[v]]
    for token in tokens:
        if(token == startToken): continue
        if(dist[token] * edges[(token, startToken)] > dist[startToken]):
            dist[startToken] = dist[token] * edges[(token, startToken)]
            paths[startToken] = paths[token] + [startToken]
            balances[startToken] = balances[token] + [dist[startToken]]
    amountOut = dist[startToken]
    return (amountOut, paths[startToken], balances[startToken])

(amountOut, profitPath, balances) = find_arbitrage("tokenB", 5)
print(f"path: {'->'.join(profitPath)}, tokenB balance={amountOut}")
