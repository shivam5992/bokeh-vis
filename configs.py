def ceo_ticker():
	if tick == "23":
		return "Sundar Pichai (2015 - Present)"
	elif tick == "16":
		return "Larry Page (2011 - 2015)"
	elif tick == "11":
		return "Eric Shmidt (2011 - 2011)"


def year_ticker():
	if tick == "23":
		return "Sundar Pichai (2015 - Present)"
	elif tick == "16":
		return "Larry Page (2011 - 2015)"
	elif tick == "11":
		return "Eric Shmidt (2011 - 2011)"


ceo = {	'chart_title' : "Google Acquisitions by CEOs",
		'category' : 'ceo',
		'ticks' : [23,16,11],
		'ticker_func' : ceo_ticker,
		'data_config' : [{ 'name' : 'Eric Shmidt (2001 - 2011)',
							'starting_year' : 2000,
							'dataset' : [],
							'upper_index' : 24},
						  { 'name' : 'Larry Page (2011 - 2015)',
							'starting_year' : 2011,
							'dataset' : [],
							'upper_index' : 18},
						  { 'name' : 'Sundar Pichai (2015 - Present)',
							'starting_year' : 2015,
							'dataset' : [],
							'upper_index' : 11}]
	}

year = {'chart_title' : "Google Acquisitions by Years",
		'category' : 'year',
		'ticks'  : [22,18,12, 7, 4],
		'data_config' : [{  'name' : '2000 - 2004',
							'starting_year' : 2000,
							'dataset' : [],
							'upper_index' : 4},
						  { 'name' : '2004 - 2008',
							'starting_year' : 2004,
							'dataset' : [],
							'upper_index' : 8},
						  { 'name' : '2008 - 2012' ,
							'starting_year' : 2008,
						 	'dataset' : [],
						 	'upper_index' : 13},
						  { 'name' : '2012 - 2016' ,
							'starting_year' : 2012,
							'dataset' : [],
							'upper_index' : 19},
						  { 'name' : '2016 - Present',
							'starting_year' : 2016,
							'dataset' : [],
							'upper_index' : 22},]
	}