# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution

Profitable path: TokenB -> TokenA -> TokenD -> TokenC -> TokenB. 

The amount in and out for each swap are as follows (Stored in `balances` in my python script):
- TokenB(5) -> TokenA(5.65) 
- TokenA(5.65) -> TokenD(2.45)
- TokenD(2.45) -> TokenC(5.08)
- TokenC(5.08) -> TokenB(20.12)

The final TokenB balance is 20.12988894407744.

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution

Slippage refers to the difference between the expected price of a token swap and the actual price achieved in an AMM protocol due to market fluctuations.

Uniswap V2 addresses the issue through a mechanism called *tolerance for price impact*. When a swap is submitted, users can specify a maximum acceptable deviation from the initial quoted price. If the actual slippage exceeds the tolerance limit, the transaction fails to prevent excessive price swings.

Here's an example function structure in Solidity in the `src` directory:

```solidity
function swapExactTokensForTokens(
    uint256 amountIn,
    uint256 amountOutMin, // the minimum amount of tokens that must be received for the transaction to proceed
    address[] calldata path,
    address to,
    uint256 deadline // a timestamp to prevent the transaction from being mined after a certain time
) external returns (uint256[] memory amounts);
```

Where `amountOutMin` and `deadline` are used to control slippage in the swap, which will revert the transaction if exceeds tolerance.



## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

Mint function is used to add liquidity to the Uniswap V2 pair contract. 

The minimum liquidity is subtracted to prevent users from providing an insufficient amount of liquidity that could lead to impermanent loss. Since the attacker could manipulate the price of the tokens in the pair, it is essential to ensure that the liquidity provided is sufficient to withstand price fluctuations.


## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

Uniswap V2 relies on a constant product formula. Liquidity hence can only be obtained by maintaining the formula carefully. That is, depositing both assets in equal proportion of value. This is to ensure that the price of the tokens in the pair remains constant, which is the core principle of the constant product formula.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution

A sandwich attack is a malicious technique used by bots to exploit weaknesses in decentralized exchange (DEX) protocols.

The attacker will identify your trade, then front-run your transaction to make the price higher. After your transaction is executed, the attacker will immediately execute another transaction to sell at the higher price, profiting from the price difference. Sandwich your trade between two transactions to maximize their profits.

If you fall victim to a sandwich attack, you'll end up receiving fewer tokens than expected for your swap.
