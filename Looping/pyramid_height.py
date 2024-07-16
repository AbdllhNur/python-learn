# Read the number of blocks
blocks = int(input("Enter the number of blocks: "))

height = 0  # Initialize the height of the pyramid
used_blocks = 0  # Initialize the number of used blocks

# Loop to build the pyramid layer by layer
while used_blocks + (height + 1) <= blocks:
    height += 1
    used_blocks += height

# Output the height of the pyramid
print("The height of the pyramid is:", height)
