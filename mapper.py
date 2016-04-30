#!/usr/bin/env python
import sys, time
import datetime

holydays = ['01/01/2016', '01/18/2016', '02/12/2016', '02/15/2016', '05/30/2016', '07/04/2016', '09/05/2016', '10/10/2016', '11/08/2016', '11/11/2016', '11/24/2016', '12/25/2016', '12/26/2016', '01/01/2015', '01/19/2015', '02/12/2015', '02/16/2015', '05/25/2015', '07/04/2015', '09/07/2015', '10/12/2015', '11/03/2015', '11/11/2015', '11/26/2015', '12/25/2015', '01/01/2014', '01/20/2014', '02/12/2014', '02/17/2014', '05/26/2014', '07/04/2014', '09/01/2014', '10/13/2014', '11/04/2014', '11/11/2014', '11/27/2014', '02/25/2014', '01/01/2013', '01/21/2013', '02/12/2013', '02/18/2013', '05/27/2013', '07/04/2013', '09/02/2013', '10/14/2013', '11/05/2013', '11/11/2013', '11/28/2013', '12/25/2013', '01/01/2012', '01/02/2012', '01/16/2012', '02/12/2012', '02/13/2012', '02/20/2012', '05/28/2012', '07/04/2012', '09/03/2012', '10/08/2012', '11/06/2012', '11/11/2012', '11/12/2012', '11/22/2012', '12/25/2012', '01/01/2011', '01/17/2011', '02/12/2011', '02/21/2011', '05/30/2011', '07/04/2011', '09/05/2011', '10/10/2011', '11/08/2011', '11/11/2011', '11/24/2011', '12/25/2011', '12/26/2011', '01/01/2010', '01/18/2010', '02/15/2010', '05/31/2010', '07/05/2010', '09/06/2010', '10/11/2010', '11/11/2010', '11/25/2010', '12/24/2010']

def parserecords():
	for linenum,line in enumerate(sys.stdin):
		if (linenum):
			line = line.strip('\n')	
			cells = line.split(',')
			if (cells[2] != '') and (cells[8] != ''):
				date = cells[1].split(' ')
				year = date[0].split('/')
				time = date[1].split(':')
				hour = int(time[0])

				holiday = 0
				if date[0] in holydays:
					holiday = 1
				
				month = int(year[0])
				weekday = datetime.date(int(year[2]),int(year[0]),int(year[1])).weekday()
				
				if hour == 12:
					hour = 0
				if date[2] == "PM":
					hour = hour + 12
				create_time = datetime.datetime(int(year[2]), int(year[0]), int(year[1]), hour, int(time[1]), int(time[2]))
			
				date1 = cells[2].split(' ')
				year1 = date1[0].split('/')
				time1 = date1[1].split(':')
				hour1 = int(time1[0])
				if hour1 == 12:
					hour1 = 0
				if date1[2] == "PM":
					hour1 = hour1 + 12

				close_time = datetime.datetime(int(year1[2]), int(year1[0]), int(year1[1]), hour1, int(time1[1]), int(time1[2]))
			
				proc_time_sec = (close_time - create_time).seconds
				proc_time_day = (close_time - create_time).days
				proc_time = int(proc_time_sec/3600)+proc_time_day*24
			
				if proc_time >= 0:
					yield (cells[0], (cells[1], cells[2], cells[3], cells[5], cells[6], cells[8], hour, month, weekday, holiday, proc_time))

def mapper():
	for key,val in parserecords():
		print '%s\t%s' % (key, val)

if __name__=='__main__':
    mapper()
