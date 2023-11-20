from difflib import SequenceMatcher
import utils

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio() * 100

def word_include(search_word):
    data = utils.load_json()
    matches = []
    for anime in data['anime']:
        if search_word in anime['title']:
            matches.append(anime)

    if matches:
        print("Exist")
        for anime in matches:
            print("제목: " + anime['title'])
            print("장르: " + ', '.join(anime['genre']))
    else:
        print("Not exist")

def object_similarity(search_word):
    data = utils.load_json()
    matches = []
    for anime in data['anime']:
        if similar(anime['title'], search_word) > 50:
            matches.append(anime)

    if matches:
        print("Exist")
        for anime in matches:
            print("제목: " + anime['title'])
            print("장르: " + ', '.join(anime['genre']))
            #print("일치율: " + str(similar(anime['title'], search_word)))
            print(f"일치율: {similar(anime['title'], search_word):.2f}%")

    else:
        print("Not exist")

search_word = input("Enter search name: ")

def combined_search(search_word):
    data = utils.load_json()
    matches = []
    for anime in data['anime']:
        if search_word in anime['title'] or similar(anime['title'], search_word) > 50:
            matches.append(anime)

    if matches:
        print("Exist")
        for anime in matches:
            print("제목: " + anime['title'])
            print("장르: " + ', '.join(anime['genre']))
            print(f"일치율: {similar(anime['title'], search_word):.2f}%")
    else:
        print("Not exist")


def search_genre(search_genre):
    search_genre = input("Enter search genre: ")
    data = utils.load_json()
    matches = []
    for anime in data['anime']:
        if search_genre in anime['title'] or any(search_genre in genre for genre in anime['genre']):
            matches.append(anime)

    if matches:
        print("Exist")
        print(f"{len(matches)}"+"개의 애니메이션이 검색되었습니다.")
        for anime in matches:
            print("제목: " + anime['title'])
            print("장르: " + ', '.join(anime['genre']))
    else:
        print("Not exist")

def print_anime_number():
    data = utils.load_json()
    print(f"{len(data['anime'])}"+"개의 애니메이션이 등록되어있습니다.")

def print_anime_title():
    data = utils.load_json()
    for anime in data['anime']:
        #print(next(iter(anime.values())))
        index = data['anime'].index(anime)
        print(f"{index+1}." + anime['title'])

combined_search(search_word)
# object_similarity(search_word)
# word_include(search_word)
search_genre(search_genre)
#print_anime_title()