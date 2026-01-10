# No 'use strict' was common in legacy code, but let's keep it for safety
# Legacy code usually uses BAREWORD filehandles (all caps)

$filename = $ARGV[0];

# Check if filename was provided
die "Usage: perl test.pl <filename>\n" unless $filename;

# The Legacy Two-Argument Open
# Perl looks at the contents of $filename to decide what to do.
open(FILE, $filename) or die "Can't open $filename: $!";

while (<FILE>) {
    print $_;  # $_ is the default variable holding the current line
}

close(FILE);
