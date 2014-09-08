import csv

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, 'data_viewer/index.html')

def csv_data(request):

	columns, data = get_csv_data()

	context = {
		'columns': columns,
		'data': data,
	}

	return render(request, 'data_viewer/table_view.html', context)

def prn_data(request):
	return HttpResponse("PRN")


def get_csv_data():

	data = []

	with open('data_viewer/data/Workbook2.csv') as f:
		reader = csv.reader(f)

		col_names = next(reader)

		for line in reader:
			data.append(entry.decode('cp1252').encode('utf-8') for entry in line)

	return col_names, data
