#텍스트마이닝 = 형태소 분석
#파이썬 형태소 사전 KoNLP 및 필요 모듈 설치 -konlp.org

# community 버젼 선택하고 설치 visual studio
#파이참의 터미널 창을 띄오고 다음명령 실행
#JPype1-0.6.3-cp36-cp36m-win_amd64.whl
#python -m pip install c:\Java\JPype1-0.6.3-cp36-cp36m-win_amd64.whl
#pip install konlpy


#pip install konlpy
#pip install Twitter # 추천
#pip install Kkma
#pip install Hannanum

from konlpy.tag import Okt
from collections import Counter

import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

twitter = Okt()
# txt1 = '아버지가 방에 들어가신다'
# txt2 = '나는 보리밥을 먹었다'
# txt3 = '롯데마트가 판매하고 있는 흑마늘 양념 치킨이 논란이 되고 있다'
#
# print(twitter.nouns(txt1))
# print(twitter.nouns(txt2))
# print(twitter.nouns(txt3))
#
# print(twitter.pos(txt1))
# print(twitter.morphs(txt1))
# f = open(r'c:/Java/data/speech.txt')
# docs = f.read()
#
# #트위터 형태소 사전을 이용해서 명사 추출
#
# nouns = twitter.nouns(docs)
#
# wc= Counter(nouns)
# print(wc)
# print(wc['여러분'])
#
# #빈도수 최상우 20개 출력
# wclist = wc.most_common(20)
# print(wclist)
# print(wclist[0][0],wclist[0][1]) #최고빈도수 단어와 빈도
#
# #단어수 2자이상만 추출
# df_word = []
# df_freq = []
# for i in range(0,len(wclist)):
#     #만일 단어가 2자이상이면
#     #dfword df freq 에 각각 저장
#     if(len(wclist[i][0])>=2):
#         df_word.append(wclist[i][0])
#         df_freq.append(wclist[i][1])
# print(df_word,df_freq)

#우드 클라우드 패키지 설치
#github.com.amueller/word_cloud
#pip install WordCloud
#pip install matplotlib

#
# f = open('c:/Java/data/worldcup2018-07-04.txt',encoding='utf-8')
# doc = f.read()
# nouns = twitter.nouns(doc)
#
# #금칙어 광고문자제거
#
#
# wdlist = []
# stopword = '비아그라|시알리스'
# for i in range(0,len(nouns)):
#     nouns[i] = re.sub(stopword,'',nouns[i])#불용어 제거
#     if(len(nouns[i]) >= 2):
#         wdlist.append(nouns[i])
#
# wc = Counter(wdlist)
# # wcimg = WordCloud(font_path=r'c/Windows/Fonts/malgun.ttf',background_color='white',width=800,height=600)\
# #     .generate_from_frequencies(wc)
# # plt.imshow(wcimg,interpolation='bilinear')
# # plt.axis('off')
# # plt.show()
#
# #마스크를 이용한 워드 클라우드
# #pip intall PIL
# mask_path='c:/Java/data/bh.jpg' #투명성 없는 파일로
# mask=np.array(Image.open(mask_path))
# wcimg = WordCloud(font_path=r'c/Windows/Fonts/malgun.ttf',background_color='white',mask=mask)\
#     .generate_from_frequencies(wc)
# plt.imshow(wcimg,interpolation='bilinear')
# plt.axis('off')
# plt.show()


#블랙프라이데이 데이터파일을 이용해서 워드클라우드로 시각화
f = open('c:/Java/data/bf2018-11-29.txt',encoding='utf-8')
doc = f.read()
nouns = twitter.nouns(doc)

#금칙어 광고문자제거
import re

wdlist = []
stopword = '비아그라|시알리스'
for i in range(0,len(nouns)):
    nouns[i] = re.sub(stopword,'',nouns[i])#불용어 제거
    if(len(nouns[i]) >= 2):
        wdlist.append(nouns[i])

wc = Counter(wdlist)
mask_path='c:/Java/data/bh.jpg' #투명성 없는 파일로
mask=np.array(Image.open(mask_path))
wcimg = WordCloud(font_path=r'c/Windows/Fonts/malgun.ttf',background_color='white',mask=mask)\
    .generate_from_frequencies(wc)
plt.imshow(wcimg,interpolation='bilinear')
plt.axis('off')
plt.show()

# 워드 클라우드 색상 바꾸기
palettable, colorbrewer 패키지 설치

jiffyclub.github.io/palettable
여러가지 배색을 도와주는 패키지 - 자동 색상 추천

import random
from palettable.colorbrewer.sequential import Reds_9
from palettable.colorbrewer.diverging import RdYlBu_11
from palettable.colorbrewer.qualitative import Pastel2_8

# 워드클라우드 문자출력에 사용할 색상팔레트를 함수로 정의
def color_func(word, font_size, position, orientation,
               random_state=None, **kwargs) :
    # return tuple(Reds_9.colors[random.randint(0,8)])   # range의 경우 ()안은 뒤에가 -1이지만 그외에는 -1이 안됨
    return tuple(RdYlBu_11.colors[random.randint(0,10)])
    # return tuple(Pastel2_8.colors[random.randint(0,7)])

# 색상팔레트 유형
# sequential : 순차적, 수치 or 순서 데이터 표기
# diverging : 수치/범주 데이터 표기
# qualitative : 범주형 데이터



wcimg = WordCloud(font_path=r'c:/Windows/Fonts/malgun.ttf',
                  background_color='white')\
    .generate_from_frequencies(wc)\
    .recolor(color_func=color_func, random_state=3)
plt.imshow(wcimg, interpolation='bilinear')   # bilinear : 글자 부드럽게
plt.axis('off')
plt.show()
