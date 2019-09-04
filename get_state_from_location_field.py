import city_state_dictionary_28dec as LD
def get_state(loc):
	loc=loc.split(" ")
	loc=[q for q in loc if len(q) >2]
	for state in LD.locationD.keys():
		cities=[city.lower() for city in LD.locationD[state]]
		for ci in cities:
			if ci in loc:	
				return state

print get_state("bangal")								
