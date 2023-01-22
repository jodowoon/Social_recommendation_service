import pandas as pd
import operator
from sklearn.metrics import mean_squared_error 
from pandas.core.indexes.base import Index

user = pd.read_csv('FavoriteMovies/movies_info_new_genres31.csv')

personal=user['user']

personal=personal.drop_duplicates()  # 중복된 열 제거하기

personal.index # 동일인물이 본 영화 

moviestitle = []
moviesaverage = []

count=0
cnt=0
average=0
for i in personal:  # 각각의 사용자별 평균 평점 구하는 코드
    try:
        cnt=cnt+1

        average=(user.loc[personal.index[cnt-1]:personal.index[cnt],['rating']].sum())/(personal.index[cnt]-personal.index[cnt-1])

        moviesaverage.append(average['rating'])
    except Exception:
        continue
# print(moviesaverage[0])

pred_m = pd.DataFrame(index=['재윤'])  #추천대상이 되는 사용자를 행으로하는 데이터 프레임 만들기

recommend_movie_contents = ['타오르는 여인의 초상','학생 로망스 젊은 날','나이브스 아웃','네트워크']

# test=user[user['title']=="쏘우"]  #특정영화를 본 모든 사용자 test에 저장 
# print(user)

# print(user['title'].drop_duplicates().iloc[1])  # 예측평점 만들 영화들 : user 데이터프레임에서 title 열을 가져와서 중복제거 

for j in range(2500):  #len(user['title'].drop_duplicates())
    test=user[user['title']==user['title'].drop_duplicates().iloc[j]] #예측평점을 만들고자 하는 영화를 차례대로 넣기

    sum=0
    for i in range(len(test)):
        test2=user[user['user']==test.iloc[i]['user']] #특정영화를 본 사용자가 본 전체 영화 저장 

        test3=test2[test2['new_genres']==test.iloc[i]['new_genres']]  #특정사용자가 본 전체 영화중에 특정 영화장르인 모든 영화
        test3['rating'].mean() - test.iloc[i]['rating']  # 특정영화를 본 사용자가 특정영화의 장르에 준 평균평점 - 특정영화에 준 평점

        sum = sum + (test.iloc[i]['rating'] - test3['rating'].mean())
    
    sum = sum/len(test)
    print(j)
    #print(user['title'].drop_duplicates().iloc[j] , moviesaverage[0] + sum)  # 추천대상이 되는 사용자가 전체영화에 준 평균평점 + (추천영화를 본사람들이 추천 영화장르에 준 평균평점 - 추천영화에 준 평점)
    pred_m[user['title'].drop_duplicates().iloc[j]]=moviesaverage[0] + sum  #데이터 프레임 열에 영화넣고 예측평점을 값으로 저장 


print(pred_m.sort_values(by='재윤', axis=1, ascending=False))

print(pred_m.transpose().sort_index().head(5)) # 데이터 10개 추출 


# print(pred_m.sort_values(by='날휘', axis=1, ascending = False))

pred_n = pd.DataFrame(index=['재윤'])

for i in range(len(recommend_movie_contents)):

    pred_n.insert(i,recommend_movie_contents[i],pred_m[recommend_movie_contents[i]],True)

print(pred_n.sort_values(by='재윤', axis=1, ascending=False))


# mean_squared_error(y_test[:2], y_pred[:2])





