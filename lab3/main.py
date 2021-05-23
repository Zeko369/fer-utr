from sys import stdin
from dataclasses import dataclass
from typing import List


@dataclass
class StateObject:
    s: str
    q: str
    t: str = None

    done: bool = None
    err: str = None


def format_state(state: List[StateObject]):
    out = []
    for item in state:
        if item.err:
            out.append('fail')
        elif item.done is not None:
            if item.done:
                out.append('1')
            else:
                out.append('0')
        else:
            out.append(f'{item.s}#{item.q}')

    return "|".join(out)


def main():
    tests = list(map(lambda x: x.split(','), input().split('|')))
    input() + input() + input()

    final_state = input()
    first_state = input()
    first_queue = input()

    state_machine = {}

    for line in stdin:
        before, after = line.strip().split('->')
        src, on, q = before.split(',')
        to, newq = after.split(',')

        if src not in state_machine:
            state_machine[src] = {}
        if on not in state_machine[src]:
            state_machine[src][on] = {}

        state_machine[src][on][q] = {"to": to, "q": newq}

    for test in tests:
        state = [StateObject(first_state, first_queue)]

        i = 0
        while i < len(test):
            on = test[i]
            last = state[-1]
            if last.done is not None or last.err is not None:
                break

            if state_machine.get(last.s):
                if state_machine[last.s].get(on) or state_machine[last.s].get('$'):
                    curr = state_machine[last.s].get(on)
                    if curr is None:
                        curr = state_machine[last.s].get('$')

                    if state_machine[last.s].get(on) and state_machine[last.s].get('$'):
                        if not state_machine[last.s][on].get(last.q[0]) and state_machine[last.s]['$'].get(last.q[0]):
                            curr = state_machine[last.s]['$']
                            i -= 1
                    elif not state_machine[last.s].get(on) and state_machine[last.s].get('$'):
                        i -= 1

                    tmp = curr.get(last.q[0])
                    if tmp:
                        newQ = tmp['q'] + last.q[1:]

                        if tmp['q'] == '$' and len(newQ) > 1:
                            newQ = newQ[1:]

                        state.append(StateObject(tmp['to'], newQ))
                        i += 1
                        continue

            state.append(StateObject(None, None, err='ERROR'))
            break

        i = 0
        while state_machine.get(state[-1].s) and state_machine.get(state[-1].s).get('$') and i < 20:
            last = state[-1]
            if last.s == final_state:
                break

            tmp = state_machine.get(last.s).get('$').get(last.q[0])
            if tmp:
                newQ = tmp['q'] + last.q[1:]

                if tmp['q'] == '$' and len(newQ) > 1:
                    newQ = newQ[1:]

                state.append(StateObject(tmp['to'], newQ))

            i += 1

        state.append(StateObject(None, None, done=state[-1].s == final_state))
        print(format_state(state))


if __name__ == '__main__':
    main()
