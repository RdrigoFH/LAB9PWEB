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

$cgi->charset("UTF-8");

my $result_index = 0;
my @matching_results;

open(my $csv_file, "<", "./universidades.csv");
my @csv_lines = <$csv_file>;
close($csv_file);