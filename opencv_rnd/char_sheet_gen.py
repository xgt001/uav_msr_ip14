__author__ = 'ganesh'

import exifread
# Open image file for reading (binary mode)

# char, char color,shape, shape color, gps lat, gps long, orientation
print "Loading Images"

f = open("/home/ganesh/edhitha/blobs/alpha_D.JPG", 'rb')


tags = exifread.process_file(f)
for tag in tags.keys():
    if tag in ('GPS GPSLatitude', 'GPS GPSLongitude','GPS GPSAltitude','Image Orientation','GPS GPSLongitudeRef','GPS GPSLatitudeRef'):
        print "Key: %s, value %s" % (tag, tags[tag])

