from scipy.stats import poisson
from scipy.stats import norm

def dark_count_spectrum(rate=1, ptime=250, time=1, smear=0.2, height=0.15):
    '''
    rate:  dark count rate;            unit:MHz
    ptime: time length of pulse;      unit: ns
    time:  total time to record dark count unit: second
    smear: smear of height of single pulse
    '''
    ec = rate/1000*ptime # expect count number in pulse time window
    Npulses = int(rate*time*1e6)
    counts = 1+poisson.rvs(ec, size=Npulses)
    counts = counts+norm.rvs(0,smear, size=Npulses) # smear of pulse height
    pulses = counts*height
    return pulses
