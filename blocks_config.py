"""
this script contains utility functions required to create 
blocks

"""

def ceo_ticker():
	if tick == "23":
		return "Sundar Pichai (2015 - Present)"
	elif tick == "16":
		return "Larry Page (2011 - 2015)"
	elif tick == "11":
		return "Eric Shmidt (2011 - 2011)"


def year_ticker():
	if tick == "22":
		return "2016 - Present"
	elif tick == "18":
		return "2012 - 2016"
	elif tick == "12":
		return "2008 - 2012"
	elif tick == "7":
		return "2004 - 2008"
	elif tick == "4":
		return "2000 - 2004"

def compl_ticker():
	return "Companies"

def category_ticker():
	if tick == "48":
		return "AI"
	elif tick == "43":
		return "Search"
	elif tick == "39":
		return "Cloud"
	elif tick == "35":
		return "Offers"
	elif tick == "31":
		return "Security"
	elif tick == "27":
		return "Youtube"
	elif tick == "23":
		return "Mobile"
	elif tick == "19":
		return "Social"
	elif tick == "15":
		return "Misc"
	elif tick == "11":
		return "Maps"
	elif tick == "7":
		return "Publishing"
	elif tick == "4":
		return "Communication"


from bokeh.palettes import Blues, Greens,  Reds, PuRd


ceo = {	'chart_title' : "Google Acquisitions by CEOs",
		'category' : 'ceo',
		'col_ind' : Reds,
		'ticks' : [23,16,11],
		'ticker_func' : ceo_ticker,
		'width' : 800,
		'height' : 500,
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
		'col_ind' : Greens,
		'ticks'  : [22,18,12, 7, 4],
		'ticker_func' : year_ticker,
		'width' : 800,
		'height' : 600,
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

category = { 'chart_title' : "Google Acquisitions by Category",
			 'category' : 'category',
			 'ticks' : [48,43,39,35,31,27,23,19,15,11,7,4],
			 'ticker_func' : category_ticker,
			 'width' : 600,
			 'height' : 1000,
			 'col_ind' : Blues,
			 'data_config' : [{ 'name' : 'AI',
								'dataset' : [],
								'upper_index' : 48},
						  	  { 'name' : 'Search',
								'dataset' : [],
								'upper_index' : 43},
						  	  { 'name' : 'Cloud',
								'dataset' : [],
								'upper_index' : 39},
								 { 'name' : 'Offers',
								'dataset' : [],
								'upper_index' : 35},
								 { 'name' : 'Security',
								'dataset' : [],
								'upper_index' : 31},
								 { 'name' : 'Youtube',
								'dataset' : [],
								'upper_index' : 27},
								 { 'name' : 'Mobile',
								'dataset' : [],
								'upper_index' : 23},
								 { 'name' : 'Social',
								'dataset' : [],
								'upper_index' : 19},
								 { 'name' : 'Misc',
								'dataset' : [],
								'upper_index' : 15},
								 { 'name' : 'Maps',
								'dataset' : [],
								'upper_index' : 11},
								 { 'name' : 'Publishing',
								'dataset' : [],
								'upper_index' : 7},
								 { 'name' : 'Communication',
								'dataset' : [],
								'upper_index' : 4}],

	}

compl = {'chart_title' : "All Google Acquisitions",
		'category' : 'compl',
		'col_ind' : PuRd,
		'ticks'  : [20],
		'ticker_func' : compl_ticker,
		'width' : 600,
		'height' : 400,
		'data_config' : [{  'starting_year' : 2000,
							'dataset' : [],
							'upper_index' : 25}]
	}