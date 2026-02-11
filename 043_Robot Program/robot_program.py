def Robot_program():
    t = int(input())

    for _ in range(t):
        n, x, k = map(int, input().split())
        command = input().strip()

        pos = x
        steps = 0
        first_hit = -1

        # ---- Find first time robot reaches 0 ----
        for i in range(min(k, n)):
            if command[i] == 'L':
                pos -= 1
            else:
                pos += 1

            steps += 1

            if pos == 0:
                first_hit = steps
                break

        if first_hit == -1:
            print(0)
            continue

        count = 1
        remaining = k - first_hit

        # ---- Find cycle length starting from 0 ----
        pos = 0
        cycle = -1

        for i in range(n):
            if command[i] == 'L':
                pos -= 1
            else:
                pos += 1

            if pos == 0:
                cycle = i + 1
                break

        # If no cycle → cannot return again
        if cycle == -1:
            print(count)
        else:
            count += remaining // cycle
            print(count)

Robot_program()
