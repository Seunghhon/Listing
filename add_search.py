import json
from pprint import pprint
import utils
from engine import word_include, object_similarity, similar

def write_json(new_data, filename='db.json'):
    with open(filename, 'r+', encoding='utf-8') as file:
        file_data = json.load(file)
        file_data["anime"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4, ensure_ascii=False)
        file.truncate()
        print("Successfully added data to file.")

def delete_json(filename='db.json'):
    with open(filename, 'r+', encoding='utf-8') as file:
        print("Enter the title of the anime you want to delete: ")
        delete_title = input()
        file_data = json.load(file)

        matching_anime = find_matching_anime(delete_title)

        if matching_anime:
            print("Exist")
            for anime in matching_anime:
                print("제목: " + anime['title'])
                print("장르: " + ', '.join(anime['genre']))

            confirm_delete = input("Is this the correct anime title? (y/n): ")
            if confirm_delete.lower() == 'y':
                file.seek(0)
                file.truncate()
                json.dump(file_data, file, indent=4, ensure_ascii=False)
                print("Successfully deleted data from file.")
            elif confirm_delete.lower() == 'n':
                delete_json(filename)
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        else:
            print("The title does not exist in the file. Please try again.")

def find_matching_anime(search_word):
    data = utils.load_json()
    matches = []

    for anime in data['anime']:
        if search_word in anime['title'] or similar(anime['title'], search_word) > 50:
            matches.append(anime)

    return matches


# title = input("Enter title: ")
# genre_input = input("Enter genre (comma-separated if multiple genres): ")
# genres = [genre.strip() for genre in genre_input.split(',')]

# new_json_object = {
#     'title': title,
#     'genre': genres,
# }

if __name__ == '__main__':
    
    title = input("Enter title: ")
    genre_input = input("Enter genre (comma-separated if multiple genres): ")
    genres = [genre.strip() for genre in genre_input.split(',')]
    
    new_json_object = {
        'title': title,
        'genre': genres,
    }

    write_json(new_json_object)
    updated_data = utils.load_json()
    pprint(updated_data)
    delete_json(new_json_object)

# write_json(new_json_object)
# updated_data = load_json()



    

