from sys import stdin
from pprint import pprint


def add_rec(changes, key, prev=set()):
    prev.add(key)
    if key in changes.keys() and '$' in changes[key].keys():
        prev.update(changes[key]['$'])
        for a in changes[key]['$']:
            if key not in changes[key]['$']:
                prev.update(add_rec(changes, a, prev))
    return prev


def main():
    cases = list(map(lambda x: x.split(','), input().split('|')))
    _states = input().split(',')
    _symbols = input().split(',')
    _ok_states = input().split(',')
    start = input()

    changes = {}
    for line in stdin:
        before, after = line.split('->')
        state, key = before.split(',')

        if state not in changes.keys():
            changes[state] = {}
        changes[state][key] = after.strip().split(',')

    for case in cases:
        output = [add_rec(changes, start)]
        for option in case:
            output.append(set())

            for o in output[-2]:
                if o not in changes.keys() or option not in changes[o].keys():
                    continue

                tmp = changes[o][option]
                for t in tmp:
                    if t in changes.keys() and '$' in changes[t].keys():
                        output[-1].update(changes[t]['$'])

                output[-1].update(tmp)

            output[-1] = set(filter(lambda x: x != '#', output[-1]))

        output = map(lambda x: ','.join(sorted(x) or ['#']), output)
        print('|'.join(output))


if __name__ == '__main__':
    main()
