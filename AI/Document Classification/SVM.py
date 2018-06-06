from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import HashingVectorizer
transformer=HashingVectorizer(stop_words='english')

data = []; target = []
l = [line.rstrip('\n') for line in open('trainingdata.txt')]
for i in range(len(l)):
    data.append(l[i][2:])
    target.append(l[i][0])
target = list(map(int, target))
data = transformer.fit_transform(data)
svm=LinearSVC()
svm.fit(data, target)

test_data=[input().rstrip() for i in range(int(input()))]
test_data_trans = transformer.transform(test_data)
pred=svm.predict(test_data_trans)
for i in pred:
    print(i)
