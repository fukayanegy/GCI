# titanic kagle competition
## subject
この課題はタイタニック船の乗客がなくなったのかどうかを予想するコンペである。
学習用のデータはtest.csv, 問題用のデータはtrain.csvである。
## column
### PassengerID
乗客の通し番号  
### Pershed  
死亡したのかどうか  
alive = 0, death = 1
### Pclass
チケットのクラス  
first, second, third がある  
1 = 1st, 2 = 2nd, 3 = 3rd  
### Name
乗客の名前  
ほぼ使えないが'Miss', 'Mrs'の違いについては考えても良いかも知れない  
### Sex
性別  
### Age
年齢  
### SibSp
乗船していた兄弟姉妹・配偶者の数  
### Parch
乗船していた親・子供の数  
年齢から親なのか子供なのかで分ける必要がある  
### Ticket
チケット番号  
ただの数字とそうでないものがある  
### Fare
チケット料金  
### Cabin
キャビン番号  
### Embarked
乗船した船  