#marvel character details
import requests
a=input("Enter character name: ")
url = "https://marvel-heroic-api-unlock-the-mcu-legendary-characters.p.rapidapi.com/name"

querystring = {"q":a}

headers = {
	"X-RapidAPI-Key": "45e68fa234msh1f0ecdefb82fac7p17d1b5jsn737e9607495a",
	"X-RapidAPI-Host": "marvel-heroic-api-unlock-the-mcu-legendary-characters.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

b=response.json()
# print(b)
if 'message' in b:
    print("Character not found")
else:
    print("Name:",a,"aka",b[0]['aka'])
    print("Description:",b[0]['description'])
    print("Powers:",b[0]['powers'])
    print("Allies:",b[0]['allies'])
    print("Enemies:",b[0]['enemies'])
    print("First appearance:",b[0]['firstAppearance'])