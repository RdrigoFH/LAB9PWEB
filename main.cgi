#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use Data::Dumper;

my $cgi = CGI->new;

my $search_name = $cgi->param("name");
my $search_period = $cgi->param("period");
my $search_local = $cgi->param("local");
my $search_program = $cgi->param("program");