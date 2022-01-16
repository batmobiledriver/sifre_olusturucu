import random
tür=int(input("""Şifre Oluşturucu by zke
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nHangi türden şifre oluşturulsun? (şifreler rasgele oluşturulur):
1- Sadece Rakam

2- Sadece Küçük Harf

3- Sadece Büyük Harf
 
4- Küçük Harf + Büyük Harf

5- Rakam + Küçük Harf + Büyük Harf

6- Rakam + Küçük Harf + Büyük Harf + Semboller:"""))
if(tür==1):
    list1 = [" 1","2","3","4","5","6","7","8","9",]
elif(tür==2):
    list1= ["q","w","e","r","t","y","u","ı","o","p","ğ","ü","a","s","d","f","g","h","j","k","l","ş","i","z","x","c","v","b","n","m","ö","ç",]
elif(tür==3):
    list1 = ["Q","W","E","R","T","Y","U","I","O","P","Ğ","Ü","A","S","D","F","G","H","J","K","L","Ş","İ","Z","X","C","V","B","N","M","Ö","Ç",]
elif(tür==4):
    list1 = ["q","w","e","r","t","y","u","ı","o","p","ğ","ü","a","s","d","f","g","h","j","k","l","ş","i","z","x","c","v","b","n","m","ö","ç","Q","W","E","R","T","Y","U","I","O","P","Ğ","Ü","A","S","D","F","G","H","J","K","L","Ş","İ","Z","X","C","V","B","N","M","Ö","Ç",]
elif(tür==5):
    list1 = ["1","2","3","4","5","6","7","8","9","0","q","w","e","r","t","y","u","ı","o","p","ğ","ü","a","s","d","f","g","h","j","k","l","ş","i","z","x","c","v","b","n","m","ö","ç","Q","W","E","R","T","Y","U","I","O","P","Ğ","Ü","A","S","D","F","G","H","J","K","L","Ş","İ","Z","X","C","V","B","N","M","Ö","Ç",]
elif(tür==6):
    list1 = ["1","2","3","4","5","6","7","8","9","0","q","w","e","r","t","y","u","ı","o","p","ğ","ü","a","s","d","f","g","h","j","k","l","ş","i","z","x","c","v","b","n","m","ö","ç","Q","W","E","R","T","Y","U","I","O","P","Ğ","Ü","A","S","D","F","G","H","J","K","L","Ş","İ","Z","X","C","V","B","N","M","Ö","Ç","!","+","/","*","-","_",".",",",]
sifre=""

basamak=int(input("-------------------------------------------------\nKaç basamaklı şifre olsun?:"))
sayi=int(input("-------------------------------------------------\nKaç adet şifre oluşturulsun?"))
for i in range (sayi):
    for i in range(basamak):
        sifre=sifre+str(random.choice(list1))
    sifre=sifre+"\n"
print("-------------------------------------------------\nŞifreleriniz oluşturuldu: \n",sifre,sep="")

input("-------------------------------------------------\nÇıkış yapmak için ENTER tuşuna basın")
