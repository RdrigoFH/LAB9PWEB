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

for (my $line_index = 1; $line_index < @csv_lines; $line_index++) {
    if ($csv_lines[$line_index] =~ /(.+?)\|(.+?)\|(?:.+?\|){2}(.+?)\|(?:.+?\|){5}(.+?)\|(?:.+?\|){5}(.+?)\|/) {
        my ($code, $name, $period, $city, $program, $type) = ($1, $2, $3, $4, $5, $6);
        
        if ((!$search_name || $search_name eq $name) &&
            (!$search_period || $search_period eq $period) &&
            (!$search_local || $search_local eq $city) &&
            (!$search_program || $search_program eq $program)) {
            
            $matching_results[$result_index] = [$code, $name, $period . " años", $city, $program, $type];
            
            $result_index++;
        }
    }
}


print $cgi->header("text/html");

print<<HTML_BLOCK;
<!DOCTYPE html>
<html>
<head>
    <title>Consulta de Universidades</title>
    <link rel="stylesheet" href="../estilo.css" />
</head>

<body>
    <div style="padding-block: 5px"></div>
    <div style="padding-block: 5px"></div>
    <div class="content">
        <h1>RESULTADOS DE BUSQUEDA</h1>
        <hr />
        <br />
        <table>
HTML_BLOCK

if (@matching_results == 0) {
    print "<h2>SIN COINCIDENCIAS - REALICE OTRA BUSQUEDA.</h2>\n";
} else {
    print<<HTML_BLOCK;
        <tr>
            <th style="width: 80px">CODIGO</th>
            <th style="width: 350px">NOMBRE</th>
            <th style="width: 80px">PERIODO</th>
            <th style="width: 80px">CIUDAD</th>
            <th style="width: 700px">CARRERA</th>
            <th style="width: 80px">TIPO</th>
        </tr>
HTML_BLOCK