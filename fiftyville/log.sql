-- Keep a log of any SQL queries you execute as you solve the mystery.

--All you know is that the theft took place on July 28, 2021 and that it took place on Humphrey Street.

SELECT * FROM crime_scene_reports WHERE street = "Humphrey Street" AND month = 7 AND day = 28;

--They said the theft occured at 10:15am, interviews were conducted with three witnesses which mentinos the word bakery.

--Find interviews of that day where it contains the word bakery:

SELECT * FROM interviews WHERE month = 7 AND day = 28 AND transcript LIKE '%bakery%';

--Witness testimoinies:
--| 161 | Ruth    | 2021 | 7     | 28  | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
--| 162 | Eugene  | 2021 | 7     | 28  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
--| 163 | Raymond | 2021 | 7     | 28  | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |

--Find number plate, based on Ruth's testimony.:

SELECT * FROM bakery_security_logs WHERE month = 7 AND day = 28 AND hour =10 AND minute >15 AND minute < 25;

--Lists all accounts withdrawn on that day based on Eugue's testimony. Find atm that is being withdrawn:

SELECT * FROM atm_transactions WHERE atm_location = "Leggett Street" AND month = 7 AND day = 28 AND transaction_type = "withdraw";

--Eugine's testimony:

--Displays ATM transactions of that time:

SELECT * FROM atm_transactions WHERE atm_location = "Humphrey Lane" AND year = 2021;

--Raymond's Testimony:

--Finding phone calls that match, less than 1 minute. Displays phone number.

SELECT * FROM phone_calls WHERE month = 7 AND day = 28 AND duration < 61;

--Display flights during that time, earliest flight:

SELECT * FROM flights WHERE month = 7 AND day = 29 ORDER BY hour ASC limit 1;

--FLIGHT ID = 36. Find passport numbers

SELECT * FROM passengers WHERE flight_id = 36;

--Find People that was on flight 36 that match with their passport numbers and their license plates.

SELECT id, name, license_plate FROM people JOIN passengers ON people.passport_number = passengers.passport_number WHERE flight_id = 36;


--Functions to compare
--SELECT * FROM bakery_security_logs WHERE month = 7 AND day = 28 AND hour =10 AND minute >15 AND minute < 25;
--SELECT id, name, license_plate FROM people JOIN passengers ON people.passport_number = passengers.passport_number WHERE flight_id = 36;
--BREAK

--Code finds ALL names of people where license plate matches with people in the flight

SELECT * FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE month = 7 AND day = 28 AND hour =10 AND minute >15 AND minute < 25);

--Next would be to match the phone number. This code finds all the suspicious phone numbers that match with the ones on the flight.

SELECT name FROM people WHERE phone_number IN (SELECT phone_number FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE month = 7 AND day = 28 AND hour =10 AND minute >15 AND minute < 25));

--Next would be to find the match between the account numbers and the people that are in the above. Code finds all suspicious account numbers

--SELECT * FROM atm_transactions WHERE atm_location = "Leggett Street" AND month = 7 AND day = 28 AND transaction_type = "withdraw";
--Find out people's account number

--Practice function tells you the account number and name of the person

--SELECT name, atm_transactions.account_number FROM people INNER JOIN bank_accounts ON people.id = person_id INNER JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number;

--Find names where ID matches up with formula.
--(1)SELECT name FROM people WHERE phone_number IN (SELECT phone_number FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE month = 7 AND day = 28 AND hour =10 AND minute >15 AND minute < 25));
--Compare names of both functions
--(2)SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE month = 7 AND day = 28 AND duration < 61);
--SELECT name FROM people WHERE id IN

SELECT * FROM phone_calls WHERE month = 7 AND day = 28 AND duration < 61;

--Function displays names of all of the people that are potential suspects based on the calls done:

SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE month = 7 AND day = 28 AND duration < 61);

SELECT name FROM people WHERE name IN

--SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE month = 7 AND day = 28 AND duration < 61);

SELECT Match(SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE month = 7 AND day = 28 AND duration < 61), SELECT * FROM crime_scene_reports WHERE street = "Humphrey Street" AND month = 7 AND day = 28)

--Think need to practice with smaller tables. With smaller examples. So the next task, actually would be to practice creating database tables myself and practicing with it. 