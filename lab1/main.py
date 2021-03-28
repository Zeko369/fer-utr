from sys import stdin


def add_rec(changes, key, prev=set(), seen=set()):
    if key in seen:
        return prev
    prev.add(key)
    seen.add(key)

    if key != '#' and '$' in changes[key].keys():
        prev.update(changes[key]['$'])
        for a in changes[key]['$']:
            prev.update(add_rec(changes, a, prev, seen))
    return prev


def main():
    cases = list(map(lambda x: x.split(','), input().split('|')))
    changes = {key: {'$': ['#']} for key in input().strip().split(',')}

    _ = input() + input()
    start = input()
    for line in stdin:
        before, after = line.split('->')
        state, key = before.split(',')
        changes[state][key] = after.strip().split(',')

    for case in cases:
        output = [add_rec(changes, start, set(), set())]
        for option in case:
            output.append(set())

            for o in output[-2]:
                if o != '#' and option in changes[o].keys():
                    output[-1].update(changes[o][option])
                    for t in changes[o][option]:
                        output[-1].update(add_rec(changes, t, set(), set()))

        output = map(lambda y: set(filter(lambda x: x != '#', y)), output)
        output = map(lambda x: ','.join(sorted(x) or ['#']), output)
        print('|'.join(output))


if __name__ == '__main__':
    main()
