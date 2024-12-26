--PAST ATTEMPT: SELECT title, movies.id, stars.movie_id, stars.person_id FROM movies JOIN stars ON movies.id = stars.movie_id JOIN people ON stars.person_id = people.id WHERE people.name LIKE '%Johnny Depp%' OR name LIKE '%Helena Bonham Carter%';

SELECT title FROM movies JOIN stars ON movies.id = stars.movie_id JOIN people ON stars.person_id=people.id WHERE people.name LIKE '%Johnny Depp%' OR name LIKE '%Helena Bonham Carter%' GROUP BY stars.movie_id HAVING COUNT(stars.movie_id) > 1;

--PATTERNS are: the movie has to appear more than once in the movies.id section
--This denotes that the movie has more than one star in it.
--Next is to show all the movies that have more than one star that has the specific star in it johnny depp etc
--Shows two records, first record will have appearance of Johnny Depp and second record will have the appearance of Helana Bonham Carter