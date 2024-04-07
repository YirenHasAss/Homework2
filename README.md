# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

tokenB : 5 -> tokenA : 5.655321988655322
tokenA : 5.655321988655322 -> tokenD : 2.4587813170979333
tokenD : 2.4587813170979333 -> tokenC : 5.0889272933015155
tokenC : 5.0889272933015155 -> tokenB : 20.129888944077443


## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

It is the difference between the expected price and the actual price of trade due to volatility and other factors like the size of the trade and the speed of the chain. To deal with the problem, we could set up the slippage tolerance range. There are two example functions that greatly illustrate how to do it.

    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);

For the function, swapExactTokensForTokens, we set up two parameters, amountIn and amountOutMin. The amountIn is the number of tokens that I put into the pool, and the amountOutMin is the minimum number of tokens I expected to get from the pool depending on my amountIn. Therefore, once the number of tokens I could get from this trade is less than amountOutMin, the trade will revert, which avoids the loss due to slippage.

    function swapTokensForExactTokens(
        uint256 amountOut,
        uint256 amountInMax,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);

Similarly, the two parameters named amoutOut and amountInMax of  the function swapTokensForExactTokens allow us to set up the tolerance range. For instance, amoutOut represents the number of tokens we expected to receive after the trade, and amountInMax means the maximum number of tokens we could afford to put into the pool to reach our target. Once the number of tokens required to put into the pool is greater than amountInMax, the trade will revert.


## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

The rationale behind this design is to maintain market efficiency, by enforcing a minimum liquidity requirement, the platform ensures that liquidity providers contribute a sufficient amount of funds to maintain market depth and efficiency. Moreover, the design also prevent
market manipulation from inflation attack.


## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

The intention is to maintain the ratio of tokenA to tokenB in order to keep the pool stable.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

Attackers exploit the transparency of pending transactions on the blockchain to manipulate prices and profit at the expense of other traders. The attacker quickly places two transactions around the target transaction. The first transaction is placed ahead of the target transaction with the intention of influencing the price, while the second transaction is placed immediately after the target transaction to capitalize on the price movement caused by the targeted transaction. When there is a sandwich attack on my trade, the slippage of my trade is gonna happen. 


