# DiskWipe
The purpose of this program is to partially wipe a disk drive. Data deleted
via the OS will still remain on a hard disk until it's overwritten with 
something else, making forensic recovery possible. This program creates that
something else, in the form of a file filled with zeros and ones, in an attempt
to thwart forensic recovery.
Note- this program is meant for hard disk drives only; It may or may not work
on SSDs.
Another note- this is a work in progress no error checking has been implemented.
