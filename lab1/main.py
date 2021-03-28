from sys import stdin
from pprint import pprint


def add_rec(changes, key, prev=set()):
    prev.add(key)
    if key != '#' and '$' in changes[key].keys():
        prev.update(changes[key]['$'])
        for a in changes[key]['$']:
            if key not in changes[key]['$']:
                prev.update(add_rec(changes, a, prev))
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
        output = [add_rec(changes, start)]
        for option in case:
            output.append(set())

            for o in output[-2]:
                if o == '#' or option not in changes[o].keys():
                    continue  # o == '#' is same as o not in keys

                tmp = changes[o][option]
                for t in tmp:
                    if t != '#' and '$' in changes[t].keys():
                        output[-1].update(changes[t]['$'])

                output[-1].update(tmp)

        output = map(lambda y: set(filter(lambda x: x != '#', y)), output)
        output = map(lambda x: ','.join(sorted(x) or ['#']), output)
        print('|'.join(output))


if __name__ == '__main__':
    main()
