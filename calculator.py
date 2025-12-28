import random
from fastmcp import FastMCP

mcp = FastMCP("CalculatorServer")

@mcp.tool()
def add(a: float, b: float) -> float:
    '''Add two floats and return the result.'''
    return a + b

@mcp.tool()
def dice_roll(sides: int) -> int:
    '''Roll a dice with the given number of sides and return the result.'''
    return random.randint(1, sides)

if __name__ == "__main__":
    mcp.run()
    