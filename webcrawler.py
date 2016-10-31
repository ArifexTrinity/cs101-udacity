# coding: utf-8

test_page1 = ('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

test_page2 = '<a href="http://udacity.com">Hello world</a>'

test_page3 = '<a href=">Hello world</a>'

test_page4 = '<a hrf=">Hello world</a>'


def retrieve_1st_url(page):
	'''
	String -> String
	Return the first url from the given string, 
	if no url is contained, return ""
	'''
	start, end = find_1st_link(page)
	if start == 0 or end == -1:
		return ""
	else:
		return page[start: end]


def find_1st_link(page):
	'''
	String -> (Number, Number)
	Find the first link appear in the given page, 
	beginning with '<a href=' and quoted by double quotes
	'''
	start_link = page.find("<a href=")
	start = page.find('"', start_link) + 1
	end = page.find('"', start)
	return start, end



assert find_1st_link(test_page1) == (98, 116)
assert retrieve_1st_url(test_page1) == "http://udacity.com"
assert find_1st_link(test_page2) == (9, 27)
assert retrieve_1st_url(test_page2) == "http://udacity.com"
assert find_1st_link(test_page3) == (9, -1)
assert retrieve_1st_url(test_page3) == ""
assert find_1st_link(test_page4) == (0, 7)
assert retrieve_1st_url(test_page4) == ""