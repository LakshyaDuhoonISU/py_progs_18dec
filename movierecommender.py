#movie recommendation app
api_id="eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNzI0NzA1NGEzMDdkYWZlYjU1ZGMyZTkyOGI0YTZmNiIsInN1YiI6IjY1ODEzZWZjOGRiYzMzMDhiMDk5ZjBjMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.fPM54IfCzbnfFpqw6ZHITkNtItHXAst7mPZLRwCoDOc"

import requests
while True:
    c=int(input("What do you want to search for:\n1.Movie\n2.TV Series\n3.Exit\n"))
    if c==1:
        movie=input("Enter movie name: ")
        url = f"https://api.themoviedb.org/3/search/movie?query={movie}&include_adult=false&language=en-US&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {api_id}"
        }

        response = requests.get(url, headers=headers)
        a=response.json()
        #print(a)
        if 'results' in a:
            b=a['results'][0]
            print("Name: ",b['original_title'])
            print("Description: ",b['overview'])
            print("Release Date: ",b['release_date'],"\n")
        else:
            print("No results found\n")
    elif c==2:
        tv=input("Enter TV series name: ")
        url = f"https://api.themoviedb.org/3/search/tv?query={tv}&include_adult=false&language=en-US&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {api_id}"
        }

        response = requests.get(url, headers=headers)
        a=response.json()
        print(a)
        if 'results' in a:
            b=a['results'][0]
            print("Name: ",b['original_name'])
            print("Description: ",b['overview'])
            print("Airing Date: ",b['first_air_date'],"\n")
        else:
            print("No results found\n")
    elif c==3:
        print("Exiting...")
        break
    else:
        print("Invalid choice\n")