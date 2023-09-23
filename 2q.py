def fcfs(ar_t, br_t):

    order = list(range(len(at)))  
    wtd = {}
    tat = []
    wt = []
    d = {}
    for i in range(len(ar_t)):
        d[ar_t[i]] = br_t[i]
    
    atsort = sorted(ar_t)
    btsort = []
    for i in atsort:
        btsort.append(d[i])
    
    current = 0
    for i in range(len(atsort)):
        current = current + btsort[i]
        wtd[atsort[i]] = current - atsort[i] - btsort[i]
    
    for i in ar_t:
        wt.append(wtd[i])
    for i in range(len(wt)):
        tat.append(wt[i] + br_t[i])
    
    return sum(wt)/len(wt),sum(tat)/len(tat) , order


def sjf(at, bt):
    order = []
    wt = [0] * len(at)
    tat = [0] * len(at)
    n = len(at)
    done = [False] * n
    tot_t = 0
    remaining_bt = bt.copy()

    while True:
        min_bt = float('inf')
        short = -1

        for i in range(n):
            if not done[i] and at[i] <= tot_t and remaining_bt[i] < min_bt:
                min_bt = remaining_bt[i]
                short = i

        if short == -1:
            break

        done[short] = True
        tot_t += bt[short]
        wt[short] = tot_t - at[short] - bt[short]
        tat[short] = wt[short] + bt[short]
        order.append(short)

    return sum(wt)/len(wt),sum(tat)/len(tat) , order

def ps(ar_t, br_t, priority):
    order = [] 
    n = len(ar_t)
    wt = [0] * n
    tat = [0] * n
    processes = [(i, ar_t[i], br_t[i], priority[i]) for i in range(n)]
    processes.sort(key=lambda x: x[3])
    total_time = 0
    for i in range(n):
        p_id, arr_time, br_time, _ = processes[i]
        if arr_time > total_time:
            total_time = arr_time
        wt[p_id] = total_time - arr_time
        total_time += br_time
        tat[p_id] = wt[p_id] + br_time
        order.append(p_id) 
    return sum(wt)/len(wt),sum(tat)/len(tat) , order

def rr(ar_t, br_t, quant):
    order = []
    n = len(ar_t)
    wt = [0] * n
    tat = [0] * n
    rest_bt = bt.copy()
    time = 0
    while any(rest_bt):
        for i in range(n):
            if rest_bt[i] > 0:
                if rest_bt[i] <= quant:
                    time += rest_bt[i]
                    wt[i] = time - ar_t[i] - br_t[i]
                    rest_bt[i] = 0
                else:
                    time += quant
                    rest_bt[i] -= quant
                tat[i] = wt[i] + br_t[i]
                order.append(i) 
    return sum(wt)/len(wt),sum(tat)/len(tat) , order

def avgwt(wt):
    return sum(wt)/len(wt)

def avgtat(tat):
    return sum(tat)/len(tat)

at = [0,10,15,20]
bt = [30,20,40,15]
p = [3,5,2,4]

# fcfs
wt_fcfs,tat_fcfs,order_fcfs = fcfs(at,bt)

# sjf
wt_sjf,tat_sjf,order_sjf = sjf(at,bt)

# ps
wt_ps,tat_ps,order_ps = ps(at,bt,p)


# rr
wt_rr,tat_rr,order_rr = rr(at,bt,4)


print([wt_fcfs,wt_sjf,wt_ps,wt_rr])
print([tat_fcfs,tat_sjf,tat_ps,tat_rr])

print(order_fcfs, order_sjf)
