__author__ = 'workhorse'
import collections
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)



loansData.index.name = "ID"
print loansData

freq = collections.Counter(loansData["Open.CREDIT.Lines"])

print "freq",freq
print "freq.keys()", freq.keys()
print "freq.values()",freq.values()
print "sum(freq.keys())", sum(freq.keys())
print 'loansData["Open.CREDIT.Lines"].mode()', loansData["Open.CREDIT.Lines"].mode()
print sum(freq.values())

chi, p = stats.chisquare(freq.values())
print chi, p



