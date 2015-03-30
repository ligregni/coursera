# Jobs scheduling

def compute(a):
    t = 0
    r = 0
    for w,l in a:
        t += l
        r += (w * t)
    return r

def compare(job1, job2):
    if job1[0]-job1[1] < job2[0] - job2[1]:
        return -1
    if job1[0]-job1[1] > job2[0] - job2[1]:
        return 1
    if job1[0] < job2[0]:
        return -1
    if job1[0] > job2[0]:
        return 1
    return 0

n = int(raw_input())
a = list()

for i in xrange(n):
    w,l = map(int, raw_input().split())
    a.append((w,l))

a.sort(cmp=compare, reverse=True)
print compute(a)

a.sort(key=lambda job: job[0]/float(job[1]), reverse=True)
print compute(a)
