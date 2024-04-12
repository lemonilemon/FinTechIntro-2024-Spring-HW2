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
tokens = ["tokenA", "tokenB", "tokenC", "tokenD", "tokenE"]

dist = { }
exchanges = { }
paths = { }
balances = { }

for token in tokens:
    dist[token] = 0
    paths[token] = []
    balances[token] = []

for ((u, v), (amount1, amount2)) in liquidity.items():
    exchanges[(u, v)] = (amount1, amount2)
    exchanges[(v, u)] = (amount2, amount1)

def find_arbitrage(startToken = "tokenB", amountIn = 5):
    paths[startToken].append(startToken)
    balances[startToken].append(amountIn)
    dist[startToken] = amountIn

    for _ in range(len(tokens)):
        for u in tokens: 
            for v in tokens:
                if u == v: 
                    continue
                if v in paths[u]: 
                    continue

                newbalance = 997 * dist[u] * exchanges[(u, v)][1] / (1000 * exchanges[(u, v)][0] + 997 * dist[u])

                if newbalance > dist[v]:
                    dist[v] = newbalance
                    paths[v] = paths[u] + [v]
                    balances[v] = balances[u] + [dist[v]]
    for token in tokens:
        if(token == startToken): continue
        (u, v) = (token, startToken)
        newbalance = 997 * dist[u] * exchanges[(u, v)][1] / (1000 * exchanges[(u, v)][0] + 997 * dist[u])
        if newbalance > dist[v]:
            dist[v] = newbalance
            paths[v] = paths[u] + [v]
            balances[v] = balances[u] + [dist[v]]

    amountOut = dist[startToken]
    return (amountOut, paths[startToken], balances[startToken])

(amountOut, profitPath, balances) = find_arbitrage("tokenB", 5)

print(f"path: {'->'.join(profitPath)}, tokenB balance={amountOut}")

print(f"Amount along the paths: {balances}")
