import streamlit as st
from natsort import natsorted
import os
from PIL import Image
import re
import random
import img2pdf
import time



def only_dir(path):
    return [i for i in os.listdir(path)if os.path.isdir(os.path.join(path,i))if not i.startswith('.')]
def only_file(path):
    return [i for i in os.listdir(path)if os.path.isfile(os.path.join(path,i))if not i.startswith('.')]
def specific_get_ext(_list,extension):
        return [i for i in _list if i.endswith(f'.{extension}') ]
def get_key(my_dict,val):
    for key, value in my_dict.items():
         if val == value:
                return key
 
    return "There is no such Key"
def in_search(txtfile,bunya):
    f = open(txtfile, 'r')
    txt=f.read()
    if any(x in txt for x in iden[bunya]):
        return txtfile
def from_search_tolist(path,bunya):
    A=[]
    for pref in only_dir(path):
        c1=os.path.join(path,pref)
        for year in only_dir(c1):
            c2=os.path.join(c1,year)
            if sum(os.path.isfile(os.path.join(c2,name))for name in os.listdir(c2) if not name.startswith('.')if name.endswith('.txt'))>=1:
                for tfile in natsorted(specific_get_ext(only_file(c2),'txt')):
                    if not in_search(os.path.join(c2,tfile),bunya)==None:
                        A.append(in_search(os.path.join(c2,tfile),bunya))
    return A
def key_from_search_tolist(path,keywoard):
    A=[]
    for pref in only_dir(path):
        c1=os.path.join(path,pref)
        for year in only_dir(c1):
            c2=os.path.join(c1,year)
            if sum(os.path.isfile(os.path.join(c2,name))for name in os.listdir(c2) if not name.startswith('.')if name.endswith('.txt'))>=1:
                for tfile in natsorted(specific_get_ext(only_file(c2),'txt')):
                    f = open(os.path.join(c2,tfile), 'r')
                    txt=f.read()
                    if keywoard in txt:
                        A.append(os.path.join(c2,tfile))
    return A
def key_list_from_search_tolist(path,_list):
    A=[]
    for pref in only_dir(path):
        c1=os.path.join(path,pref)
        for year in only_dir(c1):
            c2=os.path.join(c1,year)
            if sum(os.path.isfile(os.path.join(c2,name))for name in os.listdir(c2) if not name.startswith('.')if name.endswith('.txt'))>=1:
                for tfile in natsorted(specific_get_ext(only_file(c2),'txt')):
                    f = open(os.path.join(c2,tfile), 'r')
                    txt=f.read()
                    if all(x in txt for x in b):
                        A.append(os.path.join(c2,tfile))
    return A
def any_from_search_tolist(path,_list):
    A=[]
    for pref in only_dir(path):
        c1=os.path.join(path,pref)
        for year in only_dir(c1):
            c2=os.path.join(c1,year)
            if sum(os.path.isfile(os.path.join(c2,name))for name in os.listdir(c2) if not name.startswith('.')if name.endswith('.txt'))>=1:
                for tfile in natsorted(specific_get_ext(only_file(c2),'txt')):
                    f = open(os.path.join(c2,tfile), 'r')
                    txt=f.read()
                    if any(x in txt for x in _list):
                        A.append(os.path.join(c2,tfile))
    return A
                        
def re_search(p,source):
    m = re.search(p, source)
    return m.group(1)
DATA='''北海道
青森県
岩手県
宮城県
秋田県
山形県
福島県
茨城県
栃木県
群馬県
埼玉県
千葉県
東京都
神奈川県
新潟県
富山県
石川県
福井県
山梨県
長野県
岐阜県
静岡県
愛知県
三重県
滋賀県
京都府
大阪府
兵庫県
奈良県
和歌山県
鳥取県
島根県
岡山県
広島県
山口県
徳島県
香川県
愛媛県
高知県
福岡県
佐賀県
長崎県
熊本県
大分県
宮崎県
鹿児島県
沖縄県
'''
data='''hokkaido
aomori
iwate
miyagi
akita
yamagata
fukushima
ibaraki
tochigi
gunma
saitama
chiba
tokyo
kanagawa
niigata
toyama
ishikawa
fukui
yamanashi
nagano
gifu
shizuoka
aichi
mie
shiga
kyoto
osaka
hyogo
nara
wakayama
tottori
shimane
okayama
hiroshima
yamaguchi
tokushima
kagawa
ehime
kochi
fukuoka
saga
nagasaki
kumamoto
oita
miyazaki
kagoshima
okinawa
'''


prefecture = re.findall(r'(\w+)\n',DATA)
_prefecture=re.findall(r'(\w+)\n',data)
A=[]
pre_dict={}
for i,k in zip(prefecture,_prefecture):
    pre_dict[k]=i
    

biology=['裸子植物と被子植物','植物の分類','動物の分類','細胞','光合成・蒸散・呼吸','根・茎','消化','呼吸','血液・排出','感覚と運動','細胞分裂','生殖','遺伝']
iden={'遺伝':['遺伝','メンデル','優性','丸い種子','しわのある種子','純系'],'細胞分裂':['細胞分裂','胚','根の先端','精細胞','減数','体細胞'],'消化':['消化酵素','だ液','消化','アミノ酸','タンパク質','ベネジクト液',' リパーゼ','アミラーゼ','細胞の呼吸','ブドウ','モノグリ','毛細','肝臓','細胞の'],'生殖':['精細胞','栄養生殖','無性生殖','有性生殖','ジャガイモ','生殖方法'],'感覚と運動':['運動器官','せきずい','感覚器官','刺激と反応','骨と筋肉','中枢','手をつない'],'血液・排出':['血しょう','白血','赤血','静脈','動脈','血小板','腎臓','じん臓','体外へ排出','体外に排出','心室','心房'],'呼吸':['肺胞','気管支','横隔膜','ろっ骨','肺胞','横隔','気管'],'光合成・蒸散・呼吸':['光合成','暗室','葉緑体','寒天','オオカナ','オオカ','蒸散','気孔','ワセリン'],'根・茎':['道菅','師管'],'細胞':['細胞質','細胞壁','細胞膜','液胞','カーミン','単細胞','上皮','アメーバ','ゾウリムシ','植物の細胞'],'動物の分類':['ハチュウ類','えら呼','セキツイ','無セキツイ','うろこ','恒温','変温','ヤモリ','イモリ','イカ','軟体','マイマイ','鳥類','両生類','魚類','クジラ','卵生','胎生','肺呼','外とう','節足'],'植物の分類':['合弁','離弁','シダ','コケ','胞子','仮根','胚珠'],'裸子植物と被子植物':['被子','道菅','師管','ひげ根','主根','双子','単子','葉類']}
geo=['火山','地震','地層','気象','湿度','雲のでき方','前線','大気の動きと日本の四季','太陽','日周運動・年周運動','太陽系','金星','月']
geo_n={'火山':['火成','深成','花こう','せん緑','はんれい','流紋','安山','玄武','班晶','石基','マグマ','火山に','噴火','溶岩','火山ガス','桜島'],'地震':['地震','プレート','初期微動','主要動','P波','S波','震源','震央'],'地層':['地層','ボーリング','グ調査','堆積','しゅう曲','泥岩','れき岩','砂岩','地形図','リング試料','地質'],'気象':['天気記号','乾湿','風向','降水量','天気図','アネロ','大気圧'],'湿度':['湿度','露点','飽和水','蒸気量'],'雲のでき方':['雲'],'前線':['前線','寒冷','温暖','閉塞','停滞'],'大気の動きと日本の四季':['気団','偏西','西高','季節風','海風','陸風','気圧配置','シベリア','小笠原','オホー'],'太陽':['透明半球','黒点','プロミネンス','プロミネ','ペンの先端'],'日周運動・年周運動':['うお座','日周','星','オリオン','カシオぺ','天球'],'太陽系':['太陽系','惑星','木星','水星','衛星'],'金星':['金星'],'月':['満ち欠け','満月','新月','上弦','下弦','月の形']}

chemistry=['いろいろな物質','水溶液','気体','状態変化','原子分子','化学反応式','分解、化合','酸化と還元,エネルギー','化学変化と質量','イオン','電気分解','電池','酸とアルカリ','中和']
chemistry_n={'いろいろな物質':['有機物','無機物','伝導性','光沢','延性','PET','プラスチック','石油'],'水溶液':['水溶液'],'気体':['置換'],'状態変化':['エタノール'],'原子分子':['原子'],'化学反応式':['化学反応式'],'分解、化合':['酸化銀','炭酸'],'酸化と還元,エネルギー':['酸化','還元'],'化学変化と質量':['質量'],'イオン':['イオン'],'電気分解':['電気分解','電気分'],'電池':['電池'],'酸とアルカリ':['酸'],'中和':['中和']}
physical=['光の進め方','凸レンズ','音','力','圧力','電子','電流と電圧','オームの法則','電流による発熱','磁界','力の釣り合い、合成分解','物体の運動','仕事','エネルギー']
physical_n={'光の進め方':['光'],'凸レンズ':['焦点'],'音':['音'],'力':['力'],'圧力':['圧力'],'電子':['電子'],'電流と電圧':['電圧'],'オームの法則':['アンペア'],'電流による発熱':['発熱'],'磁界':['磁界'],'力の釣り合い、合成分解':['分解'],'物体の運動':['運動'],'仕事':['仕事'],'エネルギー':['エネルギー']}



st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
d_num = st.slider('希望のpage数を入力してください', 0, 130, 25)
genre = st.radio(
     "",
     ('分野検索','キーワード検索'))

if genre=='分野検索':
    genre_science=st.radio(label='',options=['生物','地学','化学','物理'])
    if genre_science=='生物':
        fourgenre=biology
    if genre_science=='地学':
        fourgenre=geo
        iden=geo_n
    if genre_science=='化学':
        fourgenre=chemistry
        iden=chemistry_n

    if genre_science=='物理':
        fourgenre=physical
    
# st.write('<style>div.row-widget.stRadio > div{flex-direction:column;}</style>', unsafe_allow_html=True)
path='./intan'
b=[]
if genre == 'キーワード検索':
    orand=st.radio(
'',('and検索','or検索'))
    keywoard=st.text_input('検索したいキーワードを入力して')
    b.append(keywoard)
    if st.button('追加'):
        keywoard1=st.text_input('検索したいキーワードを入力')
        b.append(keywoard1)
    st.write(b)
    b.append(keywoard)
    
    if orand=='and検索':
        A=key_list_from_search_tolist(path,b)
    if orand=='or検索':
        A=any_from_search_tolist(path,b)
        
        
if genre=='分野検索':
    bi=st.selectbox('分野を選んでください',fourgenre)
    keywoard=bi
    A=any_from_search_tolist(path,iden[bi])

z1,z2,z3=st.columns([2,2,3])
with z1:
    answer_binary=st.checkbox('解答を表示しない')
with z2:
    answer_random=st.checkbox('randomにしない')

container=st.container()

c={}
for pref in only_dir(path):
    c1=os.path.join(path,pref)
    for year in only_dir(c1):
        c2=os.path.join(c1,year)
        k2=[os.path.join(c2,i) for i in natsorted(os.listdir(c2)) if i.startswith('t')if i.endswith('.jpg')]
        k1=[os.path.join(c2,i) for i in natsorted(os.listdir(c2)) if i.endswith('.txt')]
        for i,k in zip(k1,k2):
            c[i]=k


A=[c[a] for a in A]



def dict_path_list(A):
##pathをuniqueに抜き出してくる
    p1=r'intan/(.*)/(\d)'
    p2=r'/(\d{4})'
    path_list=[]
    for i in A:
        pref_name=re_search(p1,i)
        year=re_search(p2,i)
        path_=os.path.join(path,pref_name,year)
        path_list.append(path_)
    return path_list

def zisyo_unique_num(path_list):
    zisyo={}
    for i in list(set(path_list)):
        k=[]
        for a in A:
            if i in a:
                k.append(a)
        zisyo[i]=natsorted(k)
    return zisyo

def new_random(num):
    A_b=[]
    p1=r'intan/(.*)/(\d)'
    p2=r'/(\d{4})'
    A_random=random.sample(A,num)
    for i in A_random:
        pref_name=re_search(p1,i)
        year=re_search(p2,i)
        path_=os.path.join(path,pref_name,year)
        if not i in A_b: 
            for z in zisyo_unique_num(dict_path_list(A))[path_]:
                A_b.append(z)
    return A_b

if not answer_random:
    if len(A)<=d_num:
        A=new_random(len(A)-1)
    else:
        A=new_random(d_num)
 
       


Af=[]
# A=random.sample(A,len(A))
for i in range(len(A)-1):  
    k=A[i]
    k1=A[i+1]
    #### 表現
    p = r'intan/(.*)/(\d)'
    pref_name=re_search(p,k)
    pref_1=re_search(p,k1)
    p1=r'(\d{4})'
    year_name=re_search(p1,k)
    year_1=re_search(p1,k1)
    col1,col2,col3=st.columns([1,1,3])
    with col1:
        st.subheader(pre_dict[pref_name])
    with col2:
        st.subheader(f'{year_name}年')
    image=Image.open(k)
    st.image(image)
    Af.append(k)

    _path=os.path.join(path,pref_name,year_name)
    _path1=os.path.join(path,pref_1,year_1)
    if not _path==_path1:
        if len([i for i in os.listdir(_path)if i.startswith('z')])==2:
            image_answer1=Image.open(os.path.join(_path,[i for i in os.listdir(_path)if i.startswith('z')][0]))
            image_answer2=Image.open(os.path.join(_path,[i for i in os.listdir(_path)if i.startswith('z')][1]))
            if not answer_binary:
                st.write('解答')
                st.image(image_answer1)
                st.image(image_answer2)
                Af.append(os.path.join(_path,[i for i in os.listdir(_path)if i.startswith('z')][0]))
                Af.append(os.path.join(_path,[i for i in os.listdir(_path)if i.startswith('z')][1]))
#             p2=r'/test(.*).txt'
#             d = re_search(p2,get_key(c,k))
#             if int(d)<=0.5*len([i for i in os.listdir(_path) if i.endswith('.txt')]):
#                 st.write(d)
#                 image_answer=Image.open(os.path.join(_path,[i for i in os.listdir(_path)if i.startswith('z')][0]))
#             else:
#                 image_answer=Image.open(os.path.join(_path,[i for i in os.listdir(_path)if i.startswith('z')][1]))
        else:##同じだったら解答を入れ込まない
            image_answer=Image.open(os.path.join(_path,[i for i in os.listdir(_path)if i.startswith('z')][0]))
            if not answer_binary:
                st.write('解答')
                st.image(image_answer)
                Af.append(os.path.join(_path,[i for i in os.listdir(_path)if i.startswith('z')][0]))
    else:##末尾に途中のやつが来てしまった場合
        if i==len(A)-2:
            Af.append(k1)
            image_answer=Image.open(os.path.join(_path,[i for i in os.listdir(_path)if i.startswith('z')][0]))
            Af.append(os.path.join(_path,[i for i in natsorted(os.listdir(_path))if i.startswith('z')][0]))
 

st.write(Af)
def all_path():  
    c2_list=[]
    for pref in only_dir(path):
        c1=os.path.join(path,pref)
        for year in only_dir(c1):
            c2=os.path.join(c1,year)
            c2_list.append(c2)
    return c2_list

def path_par_num(c2_list):
    prefnum_zisyo={}
    for i in c2_list:
        if not len([t for t in A if i in t])==0:
            prefnum_zisyo[i]=len([t for t in A if i in t])+len([s for s in  os.listdir(i) if s.startswith('z')])
    return prefnum_zisyo

pdf='test.jpg'

##奇数の値を取り出す→リストに格納
def insert_kisuu(prefnum_zisyo,all_list):
    for k,v in prefnum_zisyo.items():
        if v%2==1:
            zjpeg_=[i for i in os.listdir(k)if i.startswith('z')][-1]
            all_list.insert(all_list.index(os.path.join(k,zjpeg_))+1,pdf)
    return all_list

Af=insert_kisuu(path_par_num(all_path()),Af)

with open('text.pdf',"wb") as f:
    f.write(img2pdf.convert([Image.open(i).filename for i in Af]))
with open("text.pdf", "rb") as file:
    btn=container.download_button(
    label="download pdf",
    data=file,
    file_name=f"{keywoard}.pdf",
    mime="application/octet-stream")
