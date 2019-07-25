from collections import defaultdict, Count
from itertools import groupby

num_str = '112233445556784756222346587'

res = defaultdict(Count)
for dig,seq in groupby(num_str):
    res[dig][len(list(seq))] += 1

print res['5'].most_common()