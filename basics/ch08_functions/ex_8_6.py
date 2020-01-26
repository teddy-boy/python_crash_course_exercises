def city_country(city, country):
	city_name = city.title() + ', ' + country.title()
	return city_name


print(city_country('hanoi', 'vietnam'))
print(city_country('santiago', 'chile'))
print(city_country('shanghai', 'china'))
