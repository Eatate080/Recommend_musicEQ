# ヒント：これを実行して出力結果を見てみろ！
import numpy as np

# delimiter=',' は「カンマで区切って配列にしてね」という指示
y = np.loadtxt('practice_EQdate.csv', delimiter=',')

print(y)
print(type(y))
print(y.shape)