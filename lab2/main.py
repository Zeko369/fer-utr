from sys import stdin


def find_if_same(a, b, methods, data):
    for m in methods:
        for k in data:
            if((a[m] in k and b[m] not in k) or (a[m] not in k and b[m] in k)):
                return False
    return True


def run(data, machine, methods):
    output = []
    for arr in data:
        stay, kick = set(), set()
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                a = machine[arr[i]]
                b = machine[arr[j]]

                stay.add(arr[i])
                if find_if_same(a, b, methods, data):
                    stay.add(arr[j])
                    continue

                kick.add(arr[j])

        stay = [x for x in stay if x not in kick]
        output.extend([sorted(stay), sorted(kick)])

    return [x for x in output if len(x) > 0]


def main():
    states = input().split(',')
    methods = input().split(',')
    valid = input().split(',')
    init = input()

    machine = {key: {} for key in states}
    for line in [raw.strip() for raw in stdin]:
        src_all, dist = line.split('->')
        src, method = src_all.split(',')
        machine[src][method] = dist

    reachable = set([init])
    last_reachable = set()

    while reachable != last_reachable:
        last_reachable = set(list(reachable))
        for a in last_reachable:
            for m in methods:
                reachable.add(machine[a][m])

    not_reachable = list(set(states) - reachable)
    states = [x for x in states if x not in not_reachable]
    valid = [x for x in valid if x in states]

    for i in not_reachable:
        machine.pop(i)

    out = run([[x for x in states if x not in valid], valid], machine, methods)
    lastout = []
    while out != lastout:
        lastout = [i for i in out]
        out = run(lastout, machine, methods)

    for a in out:
        if init in a[1:]:
            init = a[0]

        for i in a[1:]:
            machine.pop(i)

        for k in machine.keys():
            for m in methods:
                if machine[k][m] in a[1:]:
                    machine[k][m] = a[0]

    states = sorted(machine.keys())
    valid = [x for x in valid if x in states]

    print(','.join(states))
    print(','.join(methods))
    print(','.join(valid))
    print(init)

    for k in states:
        for m in methods:
            print(f'{k},{m}->{machine[k][m]}')


if __name__ == '__main__':
    main()
