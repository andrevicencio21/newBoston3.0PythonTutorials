#!/usr/bin/perl
use 5.010;
use warnings;
use strict;
use File::Copy qw(move);



# move '11Continue.py', 'test.py';


my $directory = '.';
opendir( DIR, $directory ) or die $!;
while ( my $file = readdir(DIR) ) {
	print "$file\n";
	if($file eq "490.png"){
		print "found match";
	}
}

