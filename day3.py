s = [int(raw_input().strip().split()[0]) for _ in xrange(int(raw_input().strip()))]
print ' '.join(str(a) for a in [len([b for b in s if b<=c]) for c in xrange(100)])