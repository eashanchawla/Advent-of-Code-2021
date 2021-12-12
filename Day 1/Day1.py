
import sys

def import_text_file(filename):
    with open(filename, 'r') as file:
        data = list(map(int,file.readlines()))
    return data

def part_1(data):
    # n is the count of measurements that are larger than the previous measurement
    n = 0 
    for i in range(1, len(data)):
        if data[i-1] < data[i]:
            n+=1
    return f'Answer:{n}'
    

def part_2(data):
    empty_list = list()
    for i in range(0, len(data), 1):
        if i+2 == len(data):
            break
        empty_list.append(sum(data[i:i+3]))
    return part_1(empty_list)

if __name__ == '__main__':
    data = import_text_file(sys.argv[2])
    answer = part_1(data) if sys.argv[1] == 'part_1' else part_2(data)
    print(answer)  