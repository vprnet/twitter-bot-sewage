import csv

def new_tweet():
    with open('./sewage.csv', 'r') as f:
        reader = csv.reader(f)
        all_incidents = []

        for row in reader:
            all_incidents.append(row)

        if "gallons" not in all_incidents[-1][7]:
            tweet = all_incidents[-1][4] + " - " + all_incidents[-1][6] + " - " + " (" + all_incidents[-1][7] + " gallons estimated) "
        else:
            tweet = all_incidents[-1][4] + " - " + all_incidents[-1][6] + " - " + " (" + all_incidents[-1][7] + " estimated)"
        return tweet
