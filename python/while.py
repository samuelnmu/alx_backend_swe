outer_count = 5

while outer_count > 0:
  # Outer loop controls the number of times the inner loop runs
  inner_count = 1
  while inner_count <= outer_count:
    # Inner loop repeats for each outer loop iteration
    print(inner_count, end=" ")
    inner_count += 1
  print()  # Move to a new line after each outer loop iteration
  outer_count -= 1