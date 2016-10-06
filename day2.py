n = input()
nums = map(int, raw_input().split())
import collections
counter = collections.Counter(nums)
for i in xrange(0, 100):
    for j in xrange(counter[i]):
        print i,     