nizovi =["jabuka","kruska","brek","banana"]
nizovi_map = map(lambda x: len(x),nizovi)

nizovi_c =[len(x) for x in nizovi]

brojevi =[3,4,5,6,7]
kvadrat_c=[broj**2 if broj%2==0 else broj for broj in brojevi]