# the simple interest formula is Simple_Interest = ((p * t * r) / 100)
# where p is the principal amount, t is the time period (in years)
# and r is the interest per year (%)

def simple_interest(*, p, t, r):
    return (p * t * r) / 100


print(simple_interest(p=1000, t=2, r=3))
