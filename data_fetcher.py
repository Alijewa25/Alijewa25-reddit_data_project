import requests #kitabxanani koduma cagiriram
import json #redditden gelen melumatlari bizim rahat oxuyacagimiz json faylina cevire bilmek ucundu

def fetch_reddit_data():
    url = "https://www.reddit.com/r/technology/hot.json" #saytin ozu sadece https://www.reddit.com/r/technology/ den ibaret idi - sonuna .json yazmaqla saytin gorunusu gedir ve rengli frontun yerirni json formati alir Ele mene de bu lazimdi Bezen ise sonuna .json evezine hot.json yaziriq cunki deyirem ki butun portlari yox en cox daisilani ver mene  hot postlari ver
    headers = {'User-Agent': 'python:vaxsey_project:v0.1 (by /u/Tahmina)'} #narahat olma men sadece windows brauzeriyem xeberleri oxumaq isteyirem (deyirem ki qorxma men python kodu deyilem qapilari baglama
    print("Data is pulled from the Reddit API...")
    response = requests.get(url, headers=headers) # linke gedirik ve headersi gosterib datani aliriq sonra onuda response adi altinda bir yere yigiriq - datalari yeni

    if response.status_code == 200: #bu kod her sey ela gedir demekdi yeni deyir ki urldan datani duzgun cekdik
        data = response.json() #datani uzun metn olan stringden rahat oxuna bilecek json formatina ceviririk
        print("Data successfully extracted!") #bunu da izah etsem yuh artik zjddjxn
        posts = data['data']['children'] #data dictionarysinin icine data keyi ile girib children listini gotururuk ve lazimsiz sistem melumatlarini atib elimizde sirf postlar olan temiz list saxlayiriq
        for i, post in enumerate(posts[:3]): #her seyin duzgun islediyini yoxlamaq ucun hamisi yox ilk 3u ustunde isleyecik yeni butun postlari goturmuruk sadece ilk 3nu gotururuk ENUMERATE ise bize hem dovrun novbesini hem de ozunu verir deyek ki 0 ve 0 daki post 2 ve 3deki post 
            title = post['data']['title'] #post dictionarysinde data keyine giririk ve title-i gotururuk
            author = post['data']['author'] #post dictionarysinde data keyine giririk ve author-u gotururuk
            score = post['data']['score'] #post dictionarysinde data keyine giririk ve score-u gotururuk
            print(f"{i+1}. Title: {title}")
            print(f"Author: {author} | Like: {score}\n") #\n o demekdir ki postlar arasinda bosluq olsun yeni yeni setre kecek
    else:
        print(f"An error occurred! Status code: {response.status_code}")
if __name__ == "__main__": #eger bu esas fayldirsa yeni basqa faylin icinden cagirilmayibsa bunun altindaki kodu icra et
    fetch_reddit_data() #ve eger bu sert odenerse yuxaridaki kod tetbiq edilir