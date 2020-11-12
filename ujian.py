# print('soal nomor 1')
# nomor=input("Input your phone number: ")

# def create_phone_number(nomor):
#     if len(str(nomor))<10 or len(str(nomor))>10:
#             output='Digits must be in length of 10, not more or less'
#     elif len(str(nomor))==10:
#             output=f"({nomor[0:3]}) {nomor[3:6]}-{nomor[6:10]}"
#     for i in nomor:
#         if str(i).isalpha()==True:
#             output='Invalid Input. No Alphabet'
#         if str(i).isalnum()==False:
#             output='Invalid input. No symbols.' 
#         if str(i)=='-':
#             output='Input only positive number'       
        
#     return print(output)

# create_phone_number(nomor)


print('soal nomor 2')
def moveZeros(nomor):
    nonzero=[]
    zero=[]
    for i in nomor:
        if str(i)!='0':
            nonzero.append(i)
        else:
            zero.append(i)
    print(nonzero+zero)

moveZeros([False, 1, 0, 1, 2, 0,1, 3, 'a'])
moveZeros([0, 0, 0, 'Test',0,3,'a',True,False])
moveZeros([0, True, True, False, 'a','b',1,1,1])
print()


# print('soal nomor 3')

class Statistic:
    def mean(self,a):
        if all(isinstance(item, int) for item in a)==False:
            out='Invalid Input! All value must be integer.'
        else:
            sum=0
            for i in a:
                sum+=i
            med=sum/len(a)
            out="{:1.3f}".format(med)
        return print(out)
    def median(self,a):
        if all(isinstance(item, int) for item in a)==False:
            med='Invalid Input! All value must be integer.'
        else:
            a.sort()
            if len(a)%2==1:
                b=(len(a)/2)+0.5
                med=a[int(b)]
            if len(a)%2==0:
                b=(len(a)/2)
                c=int(b)-1
                med=(a[int(b)]+a[c])/2
        return print(med)
    def mode(self,a):
        if all(isinstance(item, int) for item in a)==False:
            med='Invalid Input! All value must be integer.'
            print(med)
        else:
            hitung={}
            tertinggi=0
            for i in a:
                if i in hitung.keys(): 
                    hitung[i] += 1
                else: 
                    hitung[i] = 1
            for i in hitung.keys():
                if hitung[i] > tertinggi:
                    tertinggi=hitung[i]
                    mode=i
            if tertinggi != 1: print(mode)
            elif tertinggi == 1: print("Tidak ada modus")

    def std(self,a):
        if all(isinstance(item, int) for item in a)==False:
            out='Invalid Input! All value must be integer.'
        else:
            sum=0
            for i in a:
                sum+=i
            med=sum/len(a)
            atas=0
            for i in a:
                atas1=(i-med)**(2)
                atas+=atas1
            stdd=atas/len(a)
            stdd1=stdd**(0.5)
            out="{:1.3f}".format(stdd1)
        return print(out)

st=Statistic()
print('Case 1')
st.mean([1,2,3,4,5,'a'])
st.median([1,2,3,4,5,'a'])
st.mode([1,2,3,4,5,'a'])
st.std([1,2,3,4,5,'a'])
print()
print('Case 2')
st.mean([12,10,10,10,10])
st.median([12,10,10,10,10])
st.mode([12,10,10,10,10])
st.std([12,10,10,10,10])
print()
print('Case 3')
st.mean([4,5,2,1,6,7])
st.median([4,5,2,1,6,7])
st.mode([4,5,2,1,6,7])
st.std([4,5,2,1,6,7])