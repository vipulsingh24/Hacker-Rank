/*
Query the median value from Station table of Lat_N column.
*/

Select round(S.LAT_N,4) from station AS S where (select count(Lat_N) from station where Lat_N < S.LAT_N ) = (select count(Lat_N) from station where Lat_N > S.LAT_N);

