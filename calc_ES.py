import numpy as np
import scipy.stats as ss

# Input rank of zscore profile, and positions of up and down regulated genes to calculate ES score

def calc_ES(zscorerank,qup,qdown):  
    n = len(zscorerank)
    nu = len(qup)
    nd = len(qdown)

    uptemp = np.array(sorted(zscorerank[qup]))
    downtemp = np.array(sorted(zscorerank[qdown]))
    upmax = max(np.array(range(1, nu+1))/nu - uptemp/n)
    upmin = min(np.array(range(0, nu))/nu - (uptemp - 1)/n)
    downmax = max(np.array(range(1, nd+1))/nd - downtemp/n)
    downmin = min(np.array(range(0, nd))/nd - (downtemp - 1)/n)

    upscore = (upmax if abs(upmax) > abs(upmin) else upmin)
    downscore = (downmax if abs(downmax) > abs(downmin) else downmin)
  
    ES= ((downscore - upscore)/2 if(upscore*downscore < 0) else 0)
    
    return ES

# test example
test_zscore=[0.903729, 0.5598, 1.72308, 1.35341, 1.26883, 1.99957, 1.34154, \
0.78105, 2.20953, 2.7222]
## real zscore profiles from L1000 contains 978 genes
test_zscorerank=ss.rankdata(test_zscore)
test_up=[0,1,4]
test_down=[2,3]

print(calc_ES(test_zscorerank,test_up,test_down))
# -0.55


