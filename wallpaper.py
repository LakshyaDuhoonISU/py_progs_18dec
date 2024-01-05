#wallpaper engine

print("Wallpaper Engine")
# Import API class from pexels_api package
from pexels_api import API
# Type your Pexels API
PEXELS_API_KEY = 'dYuJpIIDSdR89samZGSBu6eDYsTUi8JJYqnGUNNq9rqgwvVN3P3Do5ah'
# Create API object
api = API(PEXELS_API_KEY)
while True:
    c=int(input("1.Search for specific images\n2.Curated Images\n3.Popular Images\n4.Exit\n"))
    if c==1:
        a=input("Enter image subject: ")
        api.search(a,page=1,results_per_page=5)
        # Get photo entries
        photos = api.get_entries()
        # Loop the five photos
        for photo in photos:
            # Print photographer
            print('Photographer: ', photo.photographer)
            # Print url
            print('Photo url: ', photo.url)
            # Print original size url
            print('Photo original size: ', photo.original)

    elif c==2:
        api.curated(page=1,results_per_page=5)
        # Get photo entries
        photos = api.get_entries()
        # Loop the five photos
        for photo in photos:
            # Print photographer
            print('Photographer: ', photo.photographer)
            # Print url
            print('Photo url: ', photo.url)
            # Print original size url
            print('Photo original size: ', photo.original)

    elif c==3:
        api.popular(page=1,results_per_page=5)
        # Get photo entries
        photos = api.get_entries()
        # Loop the five photos
        for photo in photos:
            # Print photographer
            print('Photographer: ', photo.photographer)
            # Print url
            print('Photo url: ', photo.url)
            # Print original size url
            print('Photo original size: ', photo.original)
    elif c==4:
        print("Exiting...")
        break
    else:
        print("Invalid choice")