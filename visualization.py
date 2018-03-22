'''
References cited: https://stackoverflow.com/questions/39444665/add-data-labels-to-seaborn-factor-plot, https://seaborn.pydata.org/generated/seaborn.factorplot.html, https://stackoverflow.com/questions/2247140/how-can-i-filter-a-pcap-file-by-specific-protocol-using-python
Utilized tcpdump on a 1-minute Youtube video (pcap file provided),
Creates a categorical bar graph depicting the count of different protocols from the packets captured.

usage: python visualization.py <insertyourfile.pcap>
Author: Benny Fung
'''

import random
import pandas as p
import seaborn as sns
import pyshark as ps
import argparse
import matplotlib.pyplot as plt
import sys

def run(args):
	df = p.DataFrame()
	df['Protocols'] = packets
	g = sns.factorplot('Protocols', data=df, kind= "count", aspect=2, order=df['Protocols'].value_counts().index)
	sns.despine(offset=1, trim=True)
	plt.tight_layout()
	plt.gcf().subplots_adjust(bottom=.15)
	plt.subplots_adjust(top=.90)
	ax = plt.gca()
	for pa in ax.patches:
		ax.text(pa.get_x() + pa.get_width()/2., pa.get_height(), '%d' % int(pa.get_height()), fontsize=8, color='red', ha='center', va='bottom')
	plt.xlabel('Protocols')
	plt.ylabel('Count')
	plt.title("Protocol Count from Capture")
	plt.show()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("file", help="Input pcap file", default = None)
	args = parser.parse_args()
	packets = list()
	try:
		src = ps.FileCapture(args.file, only_summaries = True)
		for pk in src:
			packets.append(str(pk).split(' ')[4])
	except:
		print("Please input pcap file")
		sys.exit(0)
	run(args)
