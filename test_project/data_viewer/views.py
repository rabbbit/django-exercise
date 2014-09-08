import csv
import os

from django.shortcuts import render

def index(request):
	return render(request, 'data_viewer/index.html')

def csv_data(request):
	col_names, data = get_csv_data()
	return render_response(request, col_names, data)

def prn_data(request):
	col_names, data = get_prn_data()
	return render_response(request, col_names, data)


def render_response(request, col_names, data):
	context = {
		'col_names': col_names,
		'data': data,
	}

	return render(request, 'data_viewer/table_view.html', context)


def get_csv_data():

	data = []

	with open(_make_path('data/Workbook2.csv')) as f:
		reader = csv.reader(f)

		col_names = next(reader)

		for line in reader:
			data.append(_make_encoding(entry) for entry in line)

	return col_names, data


def get_prn_data():

	with open(_make_path('data/Workbook2.prn')) as f:
		lines = f.readlines()

	col_begins = _find_col_begins(lines)
	data = _split_data(lines, col_begins)


	return data[0], data[1:]

def _make_path(path):
	basepath = os.path.dirname(__file__)
	return os.path.abspath(os.path.join(basepath, path))


def _make_encoding(entry):
	"""
		Hardcoded, but seems to work for given files
	"""
	return entry.strip().decode('cp1252').encode('utf-8')


def _split_data(lines, col_begins):
	"""
		Given a list of strings, and list of integers.
		splits each string into substrings, and return list of lists of those
		substrings.
		Example:
		(['abc abc abc'], (4,8)) will return [['abc', 'abc', 'abc']]
	"""
	data = []
	for line in lines:
		prev_col_begin = 0
		row = []

		for col_begin in col_begins:
			entry = line[prev_col_begin: col_begin]
			entry = _make_encoding(entry)
			row.append(entry)
			prev_col_begin = col_begin

		row.append(_make_encoding(line[col_begin:]))
		data.append(row)

	return data


def _find_col_begins(lines):
	"""
		Finds col begins by looking at first row, finding potential
		col begins, then validating them by iteratin over data set
			col begin - index of col begin within a string,
			potential col begin - location of every word in first row
			a col begin is in-valid if any rows in the data set has character on 
			that location, and one location on the left
		Example:
		123 123 123
		12  1234 34
		Col-begins = (0, 4, 8)

		WARNING: 
			- very in-efficient, keeps whole data in memory
				and iterates over it.
				For big data sets, find a better way.
			- assumes that column names are unique
	"""

	first_line = lines[0]
	col_names = lines[0].split()

	col_begins = set()
	for col_name in col_names:
		col_begins.add(first_line.find(col_name))

	col_begins.remove(0)

	for line in lines:
		false_begins = set()
		for col_begin in col_begins:
			if line[col_begin-1] != ' ' and line[col_begin] != ' ':
				false_begins.add(col_begin)
		col_begins -= false_begins

	return sorted(col_begins)


