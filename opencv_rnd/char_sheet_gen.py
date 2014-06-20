__author__ = 'ganesh'


import exifread


import exifread
# Open image file for reading (binary mode)

# char, char color,shape, shape color, gps data, orientation
print "Loading Images"

f = open("/home/ganesh/edhitha/blobs/", 'rb')


tags = exifread.process_file(f)
for tag in tags.keys():
    if tag in ('GPS GPSLatitude', 'GPS GPSLongitude','GPS GPSAltitude','Image Orientation'):
        print "Key: %s, value %s" % (tag, tags[tag])

