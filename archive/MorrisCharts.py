
# class ChartSeriesLengthException(object):
# 	"""docstring for ChartSeriesLengthException"""
# 	def __init__(self, value):
# 		super(ChartSeriesLengthException, self).__init__()
# 		self.value = value
# 	def __str__(self):
# 		return repr(self.value);
import json
from django.shortcuts import get_object_or_404, render

		
class MorrisChart(object):
	"""
	This class is used by FRMS to easily constructed saved charts saved in FRMS.
	We use Morris ecause it is both easy and pretty.
	"""
	def __init__(self, title):
		super(MorrisChart, self).__init__()
		self.HtmlIDName= "MorrisChart_"+title;
		self.Options = {}									#Options is the dictionary for the javascript options variable generated.	
		self.ChartType = "None"							
		self.series = self.labels =[]
		self.xkey = None;
		self.ykeys = None;
		 
				
	def addOptions(self, **kwargs):							#Append dictionary with new configurations
		for key, value in kwargs.items():
			self.Options.update( {key: value} )
			

	def AddData(self,series):						#Add (set of or single) series and labels to the chart. The code will tell us if the series is the same size as the label. This will be used by Pie Charts
		self.series = series;

	def ConfigureXKey(self,string):
		self.xkey = string;


	def ConfigureYKey(self,array):
		self.ykeys = array;

	def addLabels(self,labels):
		self.labels = labels;



	def toHtml(self):										#Generate all the html we need in order to create a successful Chartist Table
		if self.series == [] or self.series == None:
			return "Error: No Data populating chart"
		if self.labels == [] or self.labels == None:
			return "Error: No Labels in charts"
		if self.xkey == None:
			self.xkey = self.labels[1]
		if self.ykeys == None:
			self.ykeys = list(self.labels[:1] )

		return """

	<div id='"""+str(self.HtmlIDName)+"""'></div>
	
	<script>
	new Morris."""+self.ChartType+"""({
  	// ID of the element in which to draw the chart.
  	element: '"""+self.HtmlIDName+"""',
  	// Chart data records -- each entry in this array corresponds to a point on
  	// the chart.
  	data: """+json.dumps(self.series)+""",
	  // The name of the data record attribute that contains x-values.
	  xkey: '"""+str(self.xkey)+"""',
	  // A list of names of data record attributes that contain y-values.
	  ykeys:""" + json.dumps(self.ykeys) + """,
	  // Labels for the ykeys -- will be displayed when you hover over the
	  // chart.
	  labels: """ + json.dumps(self.labels) + """
});
	</script>
	"""

		




class MorrisLineChart(MorrisChart):
	"""docstring for MorrisLineChart"""
	def __init__(self, title):
		super(self.__class__, self).__init__(title)
		self.ChartType="Line"

class MorrisPieChart(MorrisChart):
	"""docstring for MorrisPieChart"""
	def __init__(self, title):
		super(self.__class__, self).__init__(title)
		self.ChartType="Pie"
		
		
f = MorrisLineChart("ben");
f.addLabels(['value','year'])
f.addOptions(chartPadding=30)
f.AddData([{'value':2, 'year':'2014'},{'value':2, 'year':'2015'},{'value':2, 'year':'2016'},{'value':28, 'year':'2018'},])

print f.toHtml()


# unittest.main();	

