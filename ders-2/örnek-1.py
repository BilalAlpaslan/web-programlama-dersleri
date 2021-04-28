değişken1=2
değişken2="hello world"

# print(değişken1,değişken2)

# print(değişken1+5)
# print(değişken1*5)

# print(değişken2+5)  #hatalı
# print(değişken2+"5")

# print(değişken2*3)

# print(değişken2+str(değişken1))
# değişken3="4"
# print(int(değişken3)+değişken1)

# print(değişken2[0])
# print(değişken2[-1])

meyveler = [1,2.0,"a","string"]
# print(meyveler)
# print(*meyveler)

# if değişken1==1:
#     print("değişken1 1 e eşittir")
# elif değişken1==2:
#     print("değişken1 2 ye eşittir")
# else:
#     print("değişken1 1ve 2  değil")

# i=0
# while i<5:
#     print(i)
#     i+=1

# for i in range(10):
#     print(i)

# for meyve in meyveler:
#     print(meyve)

# for meyve in meyveler:
#     if meyve!="a":
#         print(meyve)


# for meyve in meyveler:
#     if meyve=="a":
#         continue
#     print(meyve)


# for meyve in meyveler:
#     if meyve=="a":
#         break
#     print(meyve)


# çift sayılar
# print([i for i in range(100) if i%2==0])


# def selamla(a):
#     print("merhaba"+str(a))
#     print("merhaba",a)

# selamla("ahmet")
# selamla(1)

# def asalmı(sayı:int):
#     if sayı>=2:
#         kontrol=[i for i in range(2,sayı) if sayı%i==0]
#         return len(kontrol)==0
#     return 0
    

# print(asalmı(5))
# print(asalmı(2))
# print(asalmı(15))
# print([i for i in range(100) if asalmı(i)])



# ----------------------------------------------------------------------
# değişken4=5
# print(değişken4)

# def arttır():
#     global değişken4
#     değişken4+=1
#     print(değişken4)

# arttır()
# print(değişken4)

# ----------------------------------------------------------------------


# class insan():
#     def __init__(self,boy ,isim):
#         self.boy=boy
#         self.isim=isim

#     def merhaba(self):
#         print("merhaba ben",self.isim)

# ahmet =insan(100,"ahmet")


# print(ahmet.boy)
# ahmet.merhaba()

# ----------------------------------------------------------------------


def fonk1(func):
    def wrapper():
        print("başlama")
        func()
        print("bitiş")
    return wrapper


@fonk1
def fonk2():
    print("2")

fonk2()