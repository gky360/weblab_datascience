import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %% 3.2.2 ローレンツ曲線とジニ係数 (1)

# 1 school - 学校(binary: "GP" - Gabriel Pereira or "MS" - Mousinho da Silveira)<br>
# 2 sex - 性 (binary: "F" - female or "M" - male)<br>
# 3 age - 年齢 (numeric: from 15 to 22)<br>
# 4 address - 住所のタイプ (binary: "U" - urban or "R" - rural)<br>
# 5 famsize - 家族の人数 (binary: "LE3" - less or equal to 3 or "GT3" - greater than 3)<br>
# 6 Pstatus - 両親と同居しているかどうか (binary: "T" - living together or "A" - apart)<br>
# 7 Medu - 母親の学歴 (numeric: 0 - none,  1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)<br>
# 8 Fedu - 父親の学歴 (numeric: 0 - none,  1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)<br>
# 9 Mjob - 母親の仕事 (nominal: "teacher", "health" care related, civil "services" (e.g. administrative or police), "at_home" or "other")<br>
# 10 Fjob - 父親の仕事 (nominal: "teacher", "health" care related, civil "services" (e.g. administrative or police), "at_home" or "other")<br>
# 11 reason - 学校を選んだ理由 (nominal: close to "home", school "reputation", "course" preference or "other")<br>
# 12 guardian - 生徒の保護者 (nominal: "mother", "father" or "other")<br>
# 13 traveltime - 通学時間 (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)<br>
# 14 studytime - 週の勉強時間(numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)<br>
# 15 failures - 過去のnumber of past class failures (numeric: n if 1<=n<3, else 4)<br>
# 16 schoolsup - 追加の教育サポート (binary: yes or no)<br>
# 17 famsup - 家族の教育サポート (binary: yes or no)<br>
# 18 paid - 追加の有料クラス(Math or Portuguese) (binary: yes or no)<br>
# 19 activities - 学校外の活動 (binary: yes or no)<br>
# 20 nursery - 保育園に通ったことがあるかどうか (binary: yes or no)<br>
# 21 higher - 高い教育を受けたいかどうか(binary: yes or no)<br>
# 22 internet - 家でインターネットのアクセスができるかどうか(binary: yes or no)<br>
# 23 romantic - 恋愛関係 (binary: yes or no)<br>
# 24 famrel - 家族との関係性 (numeric: from 1 - very bad to 5 - excellent)<br>
# 25 freetime - 学校後の自由時間 (numeric: from 1 - very low to 5 - very high)<br>
# 26 goout - 友人と遊ぶかどうか (numeric: from 1 - very low to 5 - very high)<br>
# 27 Dalc - 平日のアルコール摂取量 (numeric: from 1 - very low to 5 - very high)<br>
# 28 Walc - 週末のアルコール摂取量 (numeric: from 1 - very low to 5 - very high)<br>
# 29 health - 現在の健康状態 (numeric: from 1 - very bad to 5 - very good)<br>
# 30 absences - 学校の欠席数 (numeric: from 0 to 93)<br>
# 31 G1 - 一期の成績 (numeric: from 0 to 20)<br>
# 31 G2 - 二期の成績 (numeric: from 0 to 20)<br>

df = pd.read_csv("data/chap2/student-mat.csv", sep=';')
g1_male = df[df['sex'] == 'M'].sort_values('G1')['G1'].values
g1_female = df[df['sex'] == 'F'].sort_values('G1')['G1'].values
y_male = g1_male.cumsum() / g1_male.sum()
y_female = g1_female.cumsum() / g1_female.sum()
n_male, n_female = len(y_male), len(y_female)
x_male = np.linspace(1, n_male, n_male) / n_male
x_female = np.linspace(1, n_female, n_female) / n_female

plt.plot(x_male, y_male, label='male')
plt.plot(x_female, y_female, label='female')
plt.legend()
plt.savefig('ans/3_lorenz_curve.pdf')

# %% 3.2.2 ローレンツ曲線とジニ係数 (2)

gini_male = np.abs(np.subtract.outer(g1_male, g1_male)).sum()\
    / (2 * n_male * g1_male.sum())
gini_female = np.abs(np.subtract.outer(g1_female, g1_female)).sum()\
    / (2 * n_female * g1_female.sum())
print(gini_male, gini_female)
