"""External sorting (Lecture 2 code)

The datasets must already exist in the working directory.
"""

import os, sys, csv, time, json
from xsorted import xsorted, xsorter


def xsort_bench(exp=1):

    timings = []
    for i in range(exp):
        tstart = time.time()
        cpu_start = time.process_time()
        fname = 'dataset_exp_' + str(i+1) + '.csv'
        xsorted_custom = xsorter(partition_size=100000)
        with open(fname, 'r') as unsorted_f, open(('sorted_' + fname), 'w') as sorted_f:
            # wrapped in a generator so that, once the file is exhausted, xsorted's partitioning
            # (toolz.partition_all) does not keep re-reading the file for every remaining slot
            reader = (row for row in csv.reader(unsorted_f))
            items = xsorted_custom(reader, key=lambda x: int(x[1]))
            writer = csv.writer(sorted_f)
            for item in items:
                writer.writerow(item)
        tend = time.time()
        cpu_time = time.process_time() - cpu_start
        timings.append(((i+1), tend-tstart, cpu_time))
        
    return timings


if __name__ == "__main__":
    exp = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    timings = xsort_bench(exp)
    print(json.dumps({"timings": timings}))
