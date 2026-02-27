from collections import Counter

t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    colors = list(map(int, input().split()))

    left_counts = Counter(colors[:l])
    right_counts = Counter(colors[l:])

    # Remove matching pairs
    for c in list(left_counts.keys()):
        if c in right_counts:
            matched = min(left_counts[c], right_counts[c])
            left_counts[c] -= matched
            right_counts[c] -= matched
            l -= matched
            r -= matched
            if left_counts[c] == 0:
                del left_counts[c]
            if right_counts.get(c, 0) == 0:
                right_counts.pop(c, None)

    # Ensure left side is larger
    if l < r:
        left_counts, right_counts = right_counts, left_counts
        l, r = r, l

    cost = 0
    diff = (l - r) // 2  # imbalance to fix

    # Use same-color pairs on larger side to fix imbalance cheaply
    for c in list(left_counts.keys()):
        pairs = left_counts[c] // 2
        use = min(pairs, diff)
        cost += use
        left_counts[c] -= 2 * use
        l -= 2 * use
        r += 2 * use
        diff -= use
        if diff == 0:
            break

    # Remaining imbalance flips
    cost += diff
    l -= diff
    r += diff

    # Recolor remaining unmatched socks
    cost += l  # now l == r

    print(cost)
