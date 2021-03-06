#!/usr/bin/python2.7

"""
	Parse reviews from all supported formats (JSON, CSV, XML...)
	
"""

import sys, csv, json


"""
	Check for proper python version and running environment
"""


## The review parser class
#
# Parse reviews from all supported formats (JSON, CSV, XML) to a list of dicts
class ReviewParser:

	def __init__(self, handle, format_, delimiter = ','):
		self.reviews = []
		self.format_ = format_
		self.handle = handle 
		self.CSV_DELIM = delimiter

	## Parse method
	#
	# 
	def parse(self):
		if self.handle is None or self.format_ is None:
			raise AttributeError
		
		if self.format_ == 'CSV':
			reviews = csv.reader(self.handle, delimiter = self.CSV_DELIM, quotechar = '"')
			self.reviews = [{'user': review[0], 'rating': review[1], 'raw-text': review[2]} for review in reviews]

		elif self.format_ == 'JSON':
			reviews = json.load(self.handle)
			self.reviews = [{'user': review['comment-by'], 'rating': review['comment-rating'], 'raw-text': review['comment-text']}]

		elif self.format_ == 'XML':
			#parse XML
			None
		else:
			raise AttributeError

		return self.reviews

	def get_raw_text(self):
		if self.reviews:
			return "".join([review['raw-text'] for review in self.reviews])
