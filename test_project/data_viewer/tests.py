from django.test import TestCase
from data_viewer.views import _find_col_begins, _split_data

class DataViewerTestCase(TestCase):

	def test_col_begins_detection(self):
		
		to_test = (
			(['123 234'], [4]),
			(['123 234 345'], [4,8]),
			(['123 234 345', '          '], [4,8]),
			(
				['123 234 345',
				 '123 234 4353453534535'],
				[4,8]
			),
			(
				['123 234 345',
				 '1232344 4353453534535'],
				[8]
			),
			(
				['123 234 345',
				 '123 344 435',
				 '123 3444 35'],
				[4,8]
			),
		)

		for columns, exp_output in to_test:
			self.assertEquals(
				_find_col_begins(columns),
				exp_output,
			)

	def test_split_data(self):

		to_test = (
			(['123 123 123'], [4,8], [['123', '123', '123']]),
			(['123123123'],   [3,6], [['123', '123', '123']]),
			(
				#input strings
				['123123123',
				 '123123123'],
				#col begins
				[3,6],
				#output list-of-list split by col_begins
				[
					['123', '123', '123'],
					['123', '123', '123']
				]
			),
		)

		for lines, col_begins, exp_output in to_test:
			self.assertEquals(
				_split_data(lines, col_begins),
				exp_output,
			)



