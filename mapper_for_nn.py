#!/usr/bin/env python
import sys, time
import datetime

def isint(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

holydays = ['01/01/2016', '01/18/2016', '02/12/2016', '02/15/2016', '05/30/2016', '07/04/2016', '09/05/2016', '10/10/2016', '11/08/2016', '11/11/2016', '11/24/2016', '12/25/2016', '12/26/2016', '01/01/2015', '01/19/2015', '02/12/2015', '02/16/2015', '05/25/2015', '07/04/2015', '09/07/2015', '10/12/2015', '11/03/2015', '11/11/2015', '11/26/2015', '12/25/2015', '01/01/2014', '01/20/2014', '02/12/2014', '02/17/2014', '05/26/2014', '07/04/2014', '09/01/2014', '10/13/2014', '11/04/2014', '11/11/2014', '11/27/2014', '02/25/2014', '01/01/2013', '01/21/2013', '02/12/2013', '02/18/2013', '05/27/2013', '07/04/2013', '09/02/2013', '10/14/2013', '11/05/2013', '11/11/2013', '11/28/2013', '12/25/2013', '01/01/2012', '01/02/2012', '01/16/2012', '02/12/2012', '02/13/2012', '02/20/2012', '05/28/2012', '07/04/2012', '09/03/2012', '10/08/2012', '11/06/2012', '11/11/2012', '11/12/2012', '11/22/2012', '12/25/2012', '01/01/2011', '01/17/2011', '02/12/2011', '02/21/2011', '05/30/2011', '07/04/2011', '09/05/2011', '10/10/2011', '11/08/2011', '11/11/2011', '11/24/2011', '12/25/2011', '12/26/2011', '01/01/2010', '01/18/2010', '02/15/2010', '05/31/2010', '07/05/2010', '09/06/2010', '10/11/2010', '11/11/2010', '11/25/2010', '12/24/2010']

agencies = ['3-1-1', 'DCA', 'DEP', 'DFTA', 'DHS', 'DOB', 'DOE', 'DOF', 'DOHMH', 'DOITT', 'DOT', 'DPR', 'DSNY', 'EDC', 'FDNY', 'HPD', 'HRA', 'NYCEM', 'NYPD', 'TLC']

complain = ['Rodent',  'Blocked Driveway', 'Noise - Commercial', 'Taxi Complaint', 'Consumer Complaint', 'Noise - Street/Sidewalk', 'Maintenance or Facility',
 'Noise - House of Worship', 'PLUMBING', 'HEATING', 'Street Light Condition', 'For Hire Vehicle Complaint', 'Street Condition', 'Broken Muni Meter', 'Damaged Tree',
 'Drinking', 'Urinating in Public', 'DOF Property - Payment Issue', 'Noise - Vehicle', 'Vending', 'Indoor Air Quality', 'Unsanitary Animal Pvt Property',
 'Food Establishment', 'Derelict Vehicle', 'Public Payphone Complaint', 'Sidewalk Condition', 'Street Sign - Dangling', 'Illegal Tree Damage', 'Street Sign - Damaged',
 'Homeless Encampment', 'Street Sign - Missing', 'Overgrown Tree/Branches', 'Animal in a Park', 'Posting Advertisement', 'Highway Condition', 'Noise - Park',
 'PAINT - PLASTER', 'GENERAL CONSTRUCTION', 'NONCONST', 'CONSTRUCTION', 'ELECTRIC', 'APPLIANCE', 'Water System', 'Air Quality', 'Sewer', 'Industrial Waste',
 'Traffic Signal Condition', 'Noise', 'Water Conservation', 'Lead', 'Hazardous Materials', 'Dirty Conditions', 'Overflowing Litter Baskets', 'Snow',
 'Derelict Vehicles', 'Sanitation Condition', 'Missed Collection (All Materials)', 'Other Enforcement', 'Graffiti', 'Building/Use', 'Special Projects Inspection Team (SPIT)',
 'General Construction/Plumbing', 'Boilers', 'Elevator', 'Broken Parking Meter', 'Bike/Roller/Skate Chronic', 'Dead Tree', 'Electrical', 'Plumbing', 'Plant',
 'Violation of Park Rules', 'Non-Residential Heat', 'Safety', 'Unsanitary Pigeon Condition', 'Food Poisoning', 'Smoking', ' Queens and Brooklyn"', 'Vacant Lot',
 'School Maintenance', 'Root/Sewer/Sidewalk Condition', 'Teaching/Learning/Instruction', 'City Vehicle Placard Complaint', 'DOE Complaint or Compliment',
 'Health', 'Recycling Enforcement', 'Asbestos', 'BEST/Site Safety', 'Miscellaneous Categories', 'Investigations and Discipline (IAD)', 'Cranes and Derricks',
 'Litter Basket / Request', 'Sweeping/Missed-Inadequate', 'Animal Facility - No Permit', 'Unleashed Dog', 'Discipline and Suspension', 'Portable Toilet',
 'Senior Center Complaint', 'Bus Stop Shelter Placement', 'Emergency Response Team (ERT)', 'Water Quality', 'Illegal Fireworks', 'Legal Services Provider Complaint',
 'Municipal Parking Facility', 'Disorderly Youth', 'Transportation Provider Complaint', 'Bridge Condition', 'Collection Truck Noise', 'Registration and Transfers',
 'Mold', 'Panhandling', 'Illegal Animal Kept as Pet', 'DOF Property - City Rebate', ' Technology', ' Nursing', 'Parent Leadership', 'Drinking Water',
 'Unsanitary Animal Facility', 'Highway Sign - Damaged', 'Poison Ivy', 'Bottled Water', 'Radioactive Material', 'Highway Sign - Missing', 'Highway Sign - Dangling',
 'Beach/Pool/Sauna Complaint', 'DOF Property - RPIE Issue', 'Scaffold Safety', 'Stalled Sites', 'Special Enforcement', 'Lifeguard',
 'Found Property', 'Special Natural Area District (SNAD)', 'Illegal Animal Sold', 'Adopt-A-Basket', 'Public Toilet', 'Trans Fat', 'Squeegee', 'Harboring Bees/Wasps',
 ' Science and Design Technology"', ' Liberal Arts', 'Noise - Helicopter', 'Illegal Parking', 'Traffic', 'Tunnel Condition', 'Calorie Labeling', 'Forensic Engineering',
 'No Child Left Behind', ' Arts and Media"', ' Technology and Math High School"', 'Derelict Bicycle', ' Advocacy and Community Justice"', ' Engineering', ' Business',
 'Bike Rack Condition', 'Tattooing', ' Science', 'OEM Disabled Vehicle', 'X-Ray Machine/Equipment', 'Lost Property', ' Government', 'Summer Camp', ' Science and Technology"',
 ' Finance', 'DOF Parking - Tax Exemption', 'Indoor Sewage', 'Fire Safety Director - F58', 'EAP Inspection - F59', 'Fire Alarm - New System', 'Construction',
 'Fire Alarm - Reinspection', 'Fire Alarm - Addition', 'Noise Survey', 'Fire Alarm - Modification', 'Taxi Compliment', 'Public Assembly', 'Sprinkler - Mechanical',
 'Standpipe - Mechanical', 'Open Flame Permit', 'Fire Alarm - Replacement', 'Building Condition', 'Complaint', 'Agency Issues', 'Compliment', 'Standing Water',
 'Hazmat Storage/Use', 'Public Assembly - Temporary', 'DOF Literature Request', 'Benefit Card Replacement', 'Curb Condition', 'GENERAL', 'Homeless Person Assistance',
 'PAINT/PLASTER', 'SCRIE', 'Animal Abuse', 'DPR Internal', 'STRUCTURAL', 'Sweeping/Missed', 'Sweeping/Inadequate', 'Request Xmas Tree Collection',
 'Overflowing Recycling Baskets', 'UNSANITARY CONDITION', 'WATER LEAK', 'SAFETY', 'DOOR/WINDOW', 'FLOORING/STAIRS', 'HEAT/HOT WATER', 'OUTSIDE BUILDING', 'ELEVATOR',
 ' Science and Engineering at City College"', 'VACANT APARTMENT', 'DOF Property - Reduction Issue', ' Science and Technology Applications"', 'Tanning', 'AGENCY',
 'Taxi Report', 'For Hire Vehicle Report', 'Literature Request', 'SG-98', 'New Tree Request', 'SRDE', 'Vector', 'Foam Ban Enforcement', 'Advocate-SCRIE/DRIE',
 'Advocate-Personal Exemptions', 'Advocate-Prop Class Incorrect', 'Taxpayer Advocate Inquiry', 'Interior Demo', 'Advocate - Other', 'DOF Property - Update Account',
 'Advocate - RPIE', 'Advocate-Prop Refunds/Credits', 'Advocate-Co-opCondo Abatement', 'Dead/Dying Tree', 'DOF Parking - Request Status', 'Trapping Pigeon',
 ' Engineering and Architecture"', 'Home Care Provider Complaint', 'Unlicensed Dog', ' Computer Applications', ' Science Research', ' Imagination and Inquiry"',
 'SG-99', 'Unspecified', 'Advocate-Commercial Exemptions', 'Advocate-Property Value', 'Advocate-UBT']

def parserecords():
	for linenum,line in enumerate(sys.stdin):
		if (linenum):
			line = line.strip('\n')	
			cells = line.split(',')
			if (cells[2] != '') and (isint(cells[8])):
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
					if proc_time < 1:
						proc_cat = 0
					elif proc_time < 2:
						proc_cat = 1
				        elif proc_time < 3:
						proc_cat = 2
				        elif proc_time < 6:
						proc_cat = 3
				        elif proc_time < 12:
						proc_cat = 4
				        elif proc_time < 24:
						proc_cat = 5
				        elif proc_time < 48:
						proc_cat = 6
				        elif proc_time < 72:
						proc_cat = 7
				        elif proc_time < 120:
                                                proc_cat = 8
			                elif proc_time < 240:
                                                proc_cat = 9
			                elif proc_time < 720:
                                                proc_cat = 10
				        else:
                                                proc_cat = 11
	
					yield (cells[0], (cells[1], cells[2], agencies.index(cells[3]), complain.index(cells[5]), cells[6], 
							  int(cells[8]), hour, month, weekday, holiday, proc_cat))

def mapper():
	for key,val in parserecords():
		print '%s\t%s' % (key, val)

if __name__=='__main__':
    mapper()
