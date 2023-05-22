count = 0

def increment_count():
    global count
    count += 1
    print(count)

increment_count() # Output: 1
increment_count() # Output: 2
increment_count() # Output: 3
print(count)
