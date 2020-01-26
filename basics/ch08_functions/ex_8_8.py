def make_album(artist, title, tracks=''):
	album = {'artist': artist.title(), 'title': title.title()}
	if tracks:
		album['tracks'] = tracks

	return album

while True:
	print('Please enter your favorite album:')
	print('(Enter "q" to quit at anytime)')
	
	artist_name = input("Artist's name: ")
	if artist_name == 'q':
		break

	album_name = input("Album's title: ")
	if album_name == 'q':
		break

	print(make_album(artist_name, album_name))
