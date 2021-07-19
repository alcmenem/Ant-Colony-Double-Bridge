#double bridge experiment - Ant Colony
#output prob_s after T iterations
#i consider teleporting my nodes back


def proba_s(t,pher_as,pher_al):
    result = (pher_as[t])/(pher_as[t] + pher_al[t]);
    return result;

def probb_s(t,pher_bs,pher_bl):
    result = (pher_bs[t])/(pher_bs[t] + pher_bl[t]);
    return result;

def prob_l(t,prob):
    result = 1- prob[t];
    return result;
def get_m_start(t,r,ps,mb,pl):
    if t<r:
        result = ps[t-1]*mb[t-1];
    else:
        result = ps[t-1]*mb[t-1] + pl[t-r]*mb[t-r]
    return result;

def get_m_end(t,r,ps,ma,pl):
    if t<r:
        result = pl[t-1]*ma[t-1];
    else:
        result = pl[t-1]*ma[t-1] + pl[t-r]*ma[t-r];
    return result;
def calculate_pher_short_a(t,pher_as,ps_a,ps_b,ma,mb):
    result = pher_as[t-1] + ps_a[t-1]*ma[t-1] + ps_b[t-1]*mb[t-1];
    return result;
def calculate_pher_short_b(t,pher_bs,ps_a,ps_b,ma,mb):
    result = pher_bs[t-1] + ps_b[t-1]*mb[t-1] + ps_a[t-1]*ma[t-1];
    return result;
def calculate_pher_long_a(t,pher_al,pl_a,pl_b,ma,mb,r):
    if t<r:
        #result = pher_al[t-1] + pl_a[t-1]*ma[t-1];
        result = pher_al[t-1];
    else:
        result = pher_al[t-1] + pl_a[t-1]*ma[t-1] + pl_b[t-1]*mb[t-r];
    return result;
def calculate_pher_long_b(t,pher_bl,pl_a,pl_b,ma,mb,r):
    if t<r:
        #result = pher_bl[t-1] + pl_b[t-1]*mb[t-1]
        result =pher_bl[t-1];
    else:
        result = pher_bl[t-1] + pl_b[t-1]*mb[t-1] + pl_a[t-r]*ma[t-r];
    return result;




def bridge_experiment(T,N):
    #initialization
    #iterations
    #ants should have the same initial number, s: short path, l : long path, t =0
    r = 2
    ma = [];
    mb = [];
    ma.append(N/2);
    mb.append(N/2);
    #parameter
    a = 1;
    #Initial probabilities, t =0
    ps_a = [];
    pl_a =[];
    ps_b = [];
    pl_b =[];
    ps_a.append(0.5);
    ps_b.append(0.5);
    pl_a.append(0.5);
    pl_b.append(0.5);
    #Initial Pheromones on trails, I initialize as 1.
    pher_as =[];
    pher_bs =[];
    pher_al =[];
    pher_bl =[];
    pher_as.append(1);
    pher_bs.append(1);
    pher_al.append(1);
    pher_bl.append(1);
    print('Initiating the experiment with',N, 'artificial ants and', T,' iterations');
    for t in range(1,T):
        #calculate numbers
        ma.append(get_m_start(t,r,ps_a,mb,pl_a));
        mb.append(get_m_end(t,r,ps_b,mb,pl_b))
        #calculate pheromones
        pher_as.append(calculate_pher_short_a(t,pher_as,ps_a,ps_b,ma,mb));
        pher_bs.append(calculate_pher_short_b(t,pher_bs,ps_a,ps_b,ma,mb));
        pher_al.append(calculate_pher_long_a(t,pher_al,pl_a,pl_b,ma,mb,r));
        pher_bl.append(calculate_pher_long_b(t,pher_bl,pl_b,pl_b,ma,mb,r));
        #calculate the two possibilities
        ps_a.append(proba_s(t,pher_as,pher_al));
        ps_b.append(probb_s(t,pher_bs,pher_bl));
        pl_a.append(prob_l(t,ps_a));
        pl_b.append(prob_l(t,ps_b));
        #print('short probs',ps_a,ps_b);
        #print('numbers',ma,mb);
    print('My results:');
    print('Long path probability:', pl_a[T-1]);
    print('Short path probability:', ps_a[T-1]);

bridge_experiment(10000,10000);
