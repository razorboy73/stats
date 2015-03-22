__author__ = 'workhorse'

#read in loan data
#clean data
#load it into panda dataFrame

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')


loansData.dropna(inplace=True)

a =  loansData['Amount.Requested']
b =  loansData['Amount.Funded.By.Investors']


#Generate some descriptive statistics about the data set
#format dollar amounts properly
amountRequested ={}
amountFunded = {}

amountRequested["mean"]= loansData['Amount.Requested'].mean()
amountRequested["median"] = loansData['Amount.Requested'].median()
amountRequested["mode"] = stats.mode(loansData['Amount.Requested'])[0][0]
amountRequested["max"] = max(loansData['Amount.Requested'])
amountRequested["min"] = min(loansData['Amount.Requested'])
amountRequested["range"] = max(loansData['Amount.Requested'])- min(loansData['Amount.Requested'])
amountRequested["standard deviation"] = loansData['Amount.Requested'].std()
amountRequested["variance"] = loansData['Amount.Requested'].var()

print "***Amount Requested****"
for k,v in amountRequested.iteritems():
    print "The {} of the amount requested is: {:,.2f}.".format(k, round(v, 2))



amountFunded["mean"]= loansData['Amount.Funded.By.Investors'].mean()
amountFunded["median"] = loansData['Amount.Funded.By.Investors'].median()
amountFunded["mode"] = stats.mode(loansData['Amount.Funded.By.Investors'])[0][0]
amountFunded["max"] = max(loansData['Amount.Funded.By.Investors'])
amountFunded["min"] = min(loansData['Amount.Funded.By.Investors'])
amountFunded["range"] = max(loansData['Amount.Funded.By.Investors'])- min(loansData['Amount.Funded.By.Investors'])
amountFunded["standard deviation"] = loansData['Amount.Funded.By.Investors'].std()
amountFunded["variance"] = loansData['Amount.Funded.By.Investors'].var()

print "****Amount Funded*****"
for k,v in amountFunded.iteritems():
    print "The {} of the amount funded is: {:,.2f}.".format(k, round(v, 2))

loansData.boxplot(column=['Amount.Funded.By.Investors', 'Amount.Requested'])
plt.show()


plt.title('Amount.Requested vs Amount.Funded.By.Investors')
plt.hist((a, b), color=['crimson', 'burlywood'],
                            label=['Amount.Requested', 'Amount.Funded.By.Investors'])
plt.legend()
plt.show()


plt.figure()
graph = stats.probplot(a, dist="norm", plot=plt)
plt.show()
