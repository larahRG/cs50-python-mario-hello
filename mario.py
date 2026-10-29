
# Ask for a height between 1 and 8
while True:
    try:
        height = int(input("Height: "))
        if 1 <= height <= 8:
            break
    except ValueError:
        pass

# Print the pyramid
for row in range(1, height + 1):
    print(" " * (height - row) + "#" * row)


