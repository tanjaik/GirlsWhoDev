#import the csv library
#open the "girls_who_learning_python" file
#Convert it to a csv_data structure
import csv

attendees_file = open ('girls_learning_python.csv')
attendees_data = csv.DictReader(attendees_file)
for attendee in attendees_data:
    if attendee['Who'] == "Geek girl" :
        print ( "Thank you" +  attendee['Name'] + attendee ['Who'])


#Loop through each of the rows

#Compare the 'Who'
#Print "Thank you"
