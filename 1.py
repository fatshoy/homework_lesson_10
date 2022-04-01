with open('file1', 'w') as f:
    f.write('Any string')

with open('file1', 'r') as f:
    print(f.readline())