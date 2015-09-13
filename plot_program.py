import csv                          # parsing the csv file
import os                           # changing the directory for save
from datetime import datetime       # plotting datetimes
import matplotlib.pyplot as plt     # plotting on the grpah

plt.xlabel('time')

# open the data file
with open('test.csv', newline='') as data_file:
    csv_reader = csv.reader(data_file)

    # get past the column headers
    next(csv_reader)

    plt.close('all')

    f, axarr = plt.subplots(3, sharex=True)
    axarr[0].set_title('Temperature')
    axarr[1].set_title('g = inlet depth; r = throat depth; c = submergence')
    axarr[2].set_title('m = flow rate; y = acc. flow')

    for row in csv_reader:
        # convert the time in to a datetime object, also removes
        # leading and trailing whitespace
        time_str = row[1].strip()
        time_obj = datetime.strptime(time_str, '%m/%d/%Y %H:%M:%S')

        # plot time and air temp
        axarr[0].plot(time_obj, row[2], 'bo')

        # plot time and inlet depth
        axarr[1].plot(time_obj, row[3], 'go')

        # plot time and throat depth
        axarr[1].plot(time_obj, row[4], 'ro')

        # plot time and submergence
        axarr[1].plot(time_obj, row[5], 'co')

        # plot time and flow rate
        axarr[2].plot(time_obj, row[6], 'mo')

        # plot time and accumulated flow
        axarr[2].plot(time_obj, row[7], 'yo')


#plt.show()

# Save the file
os.chdir('saved_images/')
plt.savefig(datetime.now().strftime('%Y%m%d-%H-%M-%S'))

