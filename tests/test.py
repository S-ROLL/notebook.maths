var = 5
maxm, maxn = 1000, 1000
# a = [[0 for i in range(maxm)] for j in range(maxn)]

def job_amount(a):
    return len(a)

def jobscale(a, job_amount):
    sum = 0
    for i in range(job_amount):
        for j in range(1):
            sum += a[i][1]
    return sum

def process(i, a, plan_time, job_scale):
    p = (a[i][1] * plan_time)/job_scale
    return p

def p_factor_nonprec(i, a, p):
    p_factor_nonprec = a[i][4]/p
    return p_factor_nonprec

def p_factor_prec_tu(i, a, p):
    if i < 0:
        return 0
    return a[i][4] + p_factor_prec_tu(i-1,a,p)

def p_factor_prec(i, a, job_amount, job_scale, p, sum):
    return p_factor_prec_tu(i,a,p)/sum

def list_gen(rows, cols):
    a = [[0 for j in range(cols)] for i in range(rows)]
    return a


"""
x = [[1, 2, 3],
     [2, 4, 8], 
     [1, 2, 3],
     [2, 4, 8]]

print(list_gen(5, 3))
"""



import tilearn

x = [[1, 2, 3, 6, 3],[2, 4, 8, 4, 2],[2, 4, 8, 6, 7],[2, 4, 8, 4, 2],[2, 4, 8, 4, 2]]
"""
var = 5
maxm, maxn = 1000, 1000
# a = [[0 for i in range(5)] for j in range(5)]
"""

def calculate(a, plan_time):
    list = tl.list_gen(tl.job_amount(a), 1)
    for i in range(tl.job_amount(a)):
        list[i][0] = tl.process(i, a, plan_time,tl.jobscale(a, tl.job_amount(a)))
    return list

def process_data(a, plan_time):
    for i in range(tl.job_amount(a)):
        a[i].extend(calculate(a, plan_time)[i])
    return a

print(process_data(x, 3))




import tilearn as tl
from tilearn import process as pc

x = [[1, 2, 3, 6, 3],[2, 4, 8, 4, 2],[2, 4, 8, 6, 7],[2, 4, 8, 4, 2],[2, 4, 8, 4, 2]]

def calculate(a, plan_time):
    list = tl.list_gen(tl.job_amount(a), 1)
    for i in range(tl.job_amount(a)):
        list[i][0] = tl.p_factor_nonprec(i, a,tl.process(i, a, plan_time,tl.jobscale(a, tl.job_amount(a))))
    return list

def factor_data(a, plan_time):
    result = pc.process_data(a, plan_time)
    for i in range(tl.job_amount(a)):
        result[i].extend(calculate(a, plan_time)[i])
    return result

print(factor_data(x, 10))