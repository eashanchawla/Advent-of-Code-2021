import sys

# X and Y co-ordinates
X = 0
Y = 0
AIM = 0

def open_file(filename):
    global X, Y, AIM
    with open(filename, 'r') as file:
        for row in file.readlines():
            if row.split()[0] == 'forward':
                X += int(row.split()[1])
                Y += AIM * int(row.split()[1])
            elif row.split()[0] == 'down':
                AIM += int(row.split()[1])
            elif row.split()[0] == 'up':
                AIM -= int(row.split()[1])
    print(X*Y) 

if __name__ == '__main__':
    open_file(sys.argv[1])
