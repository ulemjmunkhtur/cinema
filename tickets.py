print('Welcome to Prime Cineplex Encanto')
name = input ('What is your name? ')
phone_number = input('What is your phone number? ')

print("These are today's movies")
movies = ['Encanto','Forrest Gump', 'Avatar the Last Airbender']

for count, movie in enumerate(movies):
    print (f"{count + 1}. {movie}")

movie_selection = None

while movie_selection not in range(1,4):
    try: 
        movie_selection = int(input('Please, enter your choice of movie from 1-3: '))
    except:
        print ("Nope")

print('you have chosen', movies[movie_selection-1])


