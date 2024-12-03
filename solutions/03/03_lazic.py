import re
import argparse
from textwrap import dedent
import os

def process_memory(memory):
    # Find valid mul instructions and conditional statements
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    con_pattern = r"(do\(\)|don't\(\))"
    
    
    # Find all  conditional statements and mul instructions in order
    instructions = re.findall(f"{con_pattern}|{mul_pattern}", memory)
    
    # Process the instructions
    mul_enabled = True  
    total = 0
    for inst in instructions:
        if inst[0] == "do()":
            mul_enabled = True
        elif inst[0] == "don't()":
            mul_enabled = False
        elif mul_enabled: 
            x, y = inst[1], inst[2]
            if x and y:  
                total += int(x) * int(y)

    return total

# # Example corrupted memory input
# memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# # Process the memory and get the result
# result = process_memory(memory)

# print(f"The sum of all valid multiplications is: {result}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=dedent(
            """
            Sepcify a path to a text file containing the memory.
            """
        )
    )

    parser.add_argument(
        "--path", 
        type=str,
        help="Pass corrupted memory."
    )

    args = parser.parse_args()
    with open(args.path, "r") as file:
            mem = file.read()
            
    result = process_memory(mem)

    print(f"The sum of all valid multiplications is: {result}")