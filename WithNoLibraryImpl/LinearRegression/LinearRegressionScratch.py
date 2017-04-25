from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

xs=np.array([1,2,3,4,5,6], dtype=np.float64)
ys=np.array([5,4,6,5,6,7],dtype=np.float64)

def bestFitSlopeAndIntercept(xs,ys):
    m=((mean(xs)*mean(ys))-mean(xs*ys))/((mean(xs)*mean(xs))-mean(xs**2))
    b=mean(ys)-m*mean(xs)
    return m,b


def squaredError(y_orig,ys_line):
    return sum((ys_line-y_orig)**2)

def coefficientOfDetermination(y_orig,ys_line):
    y_mean_line=[mean(y_orig) for y in y_orig]
    squaredErrorRegre=squaredError(y_orig,ys_line)
    squaredErrorMean=squaredError(y_orig,y_mean_line)
    return 1-(squaredErrorRegre/squaredErrorMean)





m,b=bestFitSlopeAndIntercept(xs,ys)
print(m,b)
regressionLine=[m*x+b for x in xs]

#co-efficient of determination
rSquare=coefficientOfDetermination(ys,regressionLine)

print(rSquare)

predict_x=8
predict_y=(m*predict_x+b)

plt.scatter(xs,ys)
plt.scatter(predict_x,predict_y)
plt.plot(xs,regressionLine)
plt.show()