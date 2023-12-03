# Open, Read and Strip the input file
with open("./input.txt") as file:
    input_data = file.read().strip()

# Initialize the sums for part 1 and part 2
sum_part1 = 0
sum_part2 = 0

# Iterate over each line in the input data
for line in input_data.split('\n'):
  # Initialize lists to store the digits for part 1 and part 2
  part1_digits = []
  part2_digits = []

  # Iterate over each character in the line
  for i, char in enumerate(line):
    # If the character is a digit, add it to the lists for part 1 and part 2
    if char.isdigit():
      part1_digits.append(char)
      part2_digits.append(char)

    # Check if the current substring matches a spelled-out digit
    for digit, value in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
      if line[i:].startswith(value):
        # If it does, add the corresponding digit to the list for part 2
        part2_digits.append(str(digit+1))

  # Add the first and last digit of the current line to the sums for part 1 and part 2
  sum_part1 += int(part1_digits[0] + part1_digits[-1])
  sum_part2 += int(part2_digits[0] + part2_digits[-1])

# Print the sums for part 1 and part 2
print(sum_part1)
print(sum_part2)