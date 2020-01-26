def make_album(artist, title, tracks=''):
	album = {'artist': artist.title(), 'title': title.title()}
	if tracks:
		album['tracks'] = tracks

	return album

print(make_album('dzung', 'how to trade in stock'))
print(make_album('lan', 'how to sell more', 13))
print(make_album('trang', 'be a better assistant', 5))
