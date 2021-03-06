from collections import namedtuple


# mean standard deviation
normal = namedtuple("normal", "N mean standard_deviation")
# lambda
poisson = namedtuple("poisson", "N mean")
# n bernouli trials p probability(0,1)
binomial = namedtuple("binomial", "N n p")
# r number of failures before a success >0, p probability of success (0,1)
nbinomial = namedtuple("nbinomial", "N r p")
# df degrees of freedom >0
student = namedtuple("student", "N df")
# a min, b max
uniform = namedtuple("uniform", "N a b")
# a shape >0, b shape>0
beta = namedtuple("beta", "N a b")
# df degrees of freedom >0
chisq = namedtuple("chisq", "N k")
# lambda > 0, mean=1/lambda
exponential = namedtuple("exponential", "N lambda_")
# df_1, df_2 of two chi square distributions
f = namedtuple("f", "N df_1 df_2")
# k shape > 0, theta scale > 0
gamma = namedtuple("gamma", "N k theta")
# mean, beta: scale > 0
gumbel = namedtuple("gumbel", "N mean beta")
lognormal = namedtuple("lognormal", "N mean standard_deviation")
cauchy = namedtuple("cauchy", "N")
# mean, kappa > 0
vonmises = namedtuple("vonmises", "N mean kappa")
# mean > 0 ,lambda (shape)> 0
wald = namedtuple("wald", "N mean lambda_")
# lambda scale > 0 kappa shape > 0
weibull = namedtuple("weibull", "N lambda_")

