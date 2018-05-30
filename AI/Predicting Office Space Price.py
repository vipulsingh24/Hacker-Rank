import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

F, N = [int(x) for x in input().split()]
train_features = []; target = []

for _ in range(N):
    row = list(map(float, input().split()))
    train_features.append(row[:-1])
    target.append(row[-1])

poly = PolynomialFeatures(degree=3)
lr = LinearRegression()
lr.fit(poly.fit_transform(np.array(train_features)), target)

T = int(input())
test_feat = []
for _ in range(T):
    features = list(map(float, input().split()))
    test_feat.append(features)

result = lr.predict(poly.fit_transform(np.array(test_feat)))
for i in range(len(result)):
    print(round(result[i],2))
