from sys import stdin 

def main():
    a = input().split('|')
    b = input().split(',')
    c = input().split(',')

    d = input()
    e = input()

    lines = []
    for line in stdin:
        lines.append(line.strip())

    print(d)

if __name__ == '__main__':
    main()
