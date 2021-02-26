# DiskWipe
Overview:
The purpose of this program is to partially wipe a disk drive. This program is 
meant for hard disk drives only; It may or may not work on SSDs.

Data deleted via the OS will still remain on a hard disk until it's overwritten
with something else, making forensic recovery possible. This program creates that
something else, in the form of a file filled with zeros and ones, in an attempt
to thwart forensic recovery. This is by no means a guarunteed safe method of
data removal. The only surefire way to destroy data is physical destruction of
the medium it is stored on.

This program is to be used as is with no warranty or liability accepted for 
anything bad that happens.

Current issues:
Program doesn't verify available disk space. Hoping implement a check for this in
future versions.
