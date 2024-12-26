-- Keep a log of any SQL queries you execute as you solve the mystery.

--All you know is that the theft took place on July 28, 2021 and that it took place on Humphrey Street.

SELECT * FROM crime_scene_reports WHERE street = "Humphrey Street" AND month = 7 AND day = 28;

--They said the theft occured at 10:15am, interviews were conducted with three witnesses which mentinos the word bakery.

--Find interviews of that day where it contains the word bakery:

SELECT * FROM interviews WHERE month = 7 AND day = 28 AND transcript LIKE '%bakery%';

--Witness testimoinies:
--| 161 | Ruth    | 2021 | 7     | 28  | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
--If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
--| 162 | Eugene  | 2021 | 7     | 28  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery,
--I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
--| 163 | Raymond | 2021 | 7     | 28  | As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
--In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
--The thief then asked the person on the other end of the phone to purchase the flight ticket.

--Find number plate, based on Ruth's testimony.:

SELECT * FROM bakery_security_logs WHERE month = 7 AND day = 28 AND hour =10 AND minute >=15 AND minute <=30;

NUMBER PLATES of people that left during that time
#1
| id  | year | month | day | hour | minute | activity | license_plate |
+-----+------+-------+-----+------+--------+----------+---------------+
| 260 | 2021 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       |
| 261 | 2021 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | ** Bruce
| 262 | 2021 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       |
| 263 | 2021 | 7     | 28  | 10   | 19     | exit     | 4328GD8       | ** LUCA
| 264 | 2021 | 7     | 28  | 10   | 20     | exit     | G412CB7       |
| 265 | 2021 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       |
| 266 | 2021 | 7     | 28  | 10   | 23     | exit     | 322W7JE       |
| 267 | 2021 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       | ** Kelsey
LICENSE PLATE OF THE PEOPLE ON THE FLIGHT:
#2
+--------+--------+---------------+
|   id   |  name  | license_plate |
+--------+--------+---------------+
| 953679 | Doris  | M51FA04       |
| 398010 | Sofia  | G412CB7       |
| 686048 | Bruce  | 94KL13X       | **
| 651714 | Edward | 130LD9Z       |
| 560886 | Kelsey | 0NTHK55       |**
| 449774 | Taylor | 1106N58       |
| 395717 | Kenny  | 30G67EN       |
| 467400 | Luca   | 4328GD8       | **
+--------+--------+---------------+

NAME OF PEOPLE THAT TOOK OUT MONEY DURING EYEWITNESS ACCOUNTS
+---------+-----------+
|  name   | person_id |
+---------+-----------+
| Bruce   | 686048    | **
| Diana   | 514354    |
| Brooke  | 458378    |
| Kenny   | 395717    |
| Iman    | 396669    |
| Luca    | 467400    | **
| Taylor  | 449774    |
| Benista | 438727    |
+---------+-----------+

--HINT HERE: LICENSE PLATES

SELECT name, phone_number, passport_number, license_plate FROM people WHERE name = "Luca";
SUSPECT 1
+------+----------------+-----------------+---------------+
| name |  phone_number  | passport_number | license_plate |
+------+----------------+-----------------+---------------+
| Luca | (389) 555-5198 | 8496433585      | 4328GD8       |
+------+----------------+-----------------+---------------+
SUSPECT 2:
+-------+----------------+-----------------+---------------+
| name  |  phone_number  | passport_number | license_plate |
+-------+----------------+-----------------+---------------+
| Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |
+-------+----------------+-----------------+---------------+

+-------+----------------+-----------------+---------------+
| name  |  phone_number  | passport_number | license_plate |
+-------+----------------+-----------------+---------------+
| Diana | (770) 555-1861 | 3592750733      | 322W7JE       |
+-------+----------------+-----------------+---------------+
Diana was not on the flight. That's the thing.
+-----+----------------+----------------+------+-------+-----+----------+
| id  |     caller     |    receiver    | year | month | day | duration |
+-----+----------------+----------------+------+-------+-----+----------+
| 221 | (130) 555-0289 | (996) 555-8899 | 2021 | 7     | 28  | 51       |
| 224 | (499) 555-9472 | (892) 555-8872 | 2021 | 7     | 28  | 36       |
| 233 | (367) 555-5533 | (375) 555-8161 | 2021 | 7     | 28  | 45       | -> BRUCE
| 234 | (609) 555-5876 | (389) 555-5198 | 2021 | 7     | 28  | 60       |
| 251 | (499) 555-9472 | (717) 555-1342 | 2021 | 7     | 28  | 50       |
| 254 | (286) 555-6063 | (676) 555-6554 | 2021 | 7     | 28  | 43       |
| 255 | (770) 555-1861 | (725) 555-3243 | 2021 | 7     | 28  | 49       | -> DIANA
| 261 | (031) 555-6622 | (910) 555-3251 | 2021 | 7     | 28  | 38       |
| 279 | (826) 555-1652 | (066) 555-9701 | 2021 | 7     | 28  | 55       |
| 281 | (338) 555-6650 | (704) 555-2131 | 2021 | 7     | 28  | 54       |
+-----+----------------+----------------+------+-------+-----+----------+

SELECT name FROM people WHERE phone_number = "(375) 555-8161";

--Lists all accounts withdrawn on that day based on Eugue's testimony. Find atm that is being withdrawn:

SELECT * FROM atm_transactions WHERE atm_location = "Leggett Street" AND month = 7 AND day = 28 AND transaction_type = "withdraw";

+-----+----------------+------+-------+-----+----------------+------------------+--------+
| id  | account_number | year | month | day |  atm_location  | transaction_type | amount |
+-----+----------------+------+-------+-----+----------------+------------------+--------+
| 246 | 28500762       | 2021 | 7     | 28  | Leggett Street | withdraw         | 48     | ** = LUCA
| 264 | 28296815       | 2021 | 7     | 28  | Leggett Street | withdraw         | 20     | xx
| 266 | 76054385       | 2021 | 7     | 28  | Leggett Street | withdraw         | 60     | xx
| 267 | 49610011       | 2021 | 7     | 28  | Leggett Street | withdraw         | 50     | ** = BRUCE
| 269 | 16153065       | 2021 | 7     | 28  | Leggett Street | withdraw         | 80     | xx
| 288 | 25506511       | 2021 | 7     | 28  | Leggett Street | withdraw         | 20     | xx
| 313 | 81061156       | 2021 | 7     | 28  | Leggett Street | withdraw         | 30     | xx
| 336 | 26013199       | 2021 | 7     | 28  | Leggett Street | withdraw         | 35     | ** = DIANA, present in the caller list and also took money out
+-----+----------------+------+-------+-----+----------------+------------------+--------+

SELECT bank_accounts.account_number, bank_accounts.person_id, atm_transactions.atm_location FROM bank_accounts JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number WHERE atm_location = "Leggett Street" AND month = 7 AND day = 28 AND transaction_type = "withdraw";
SELECT bank_accounts.account_number, bank_accounts.person_id, people.name  FROM bank_accounts JOIN people ON bank_accounts.person_id = people.id WHERE bank_accounts.account_number = 26013199;

LIST OF CALLERS NAMES:
+---------+----------------+
| Sofia   | (130) 555-0289 |
| Kelsey  | (499) 555-9472 |
| Bruce   | (367) 555-5533 | &&
| Kathryn | (609) 555-5876 |
| Kelsey  | (499) 555-9472 | **
| Taylor  | (286) 555-6063 |
| Diana   | (770) 555-1861 | -> potential new suspect
| Carina  | (031) 555-6622 |
| Kenny   | (826) 555-1652 |
| Benista | (338) 555-6650 |
+---------+----------------+

#3
+----------------+-----------+----------------+
| account_number | person_id |  atm_location  |
+----------------+-----------+----------------+
| 28500762       | 467400    | Leggett Street |
| 28296815       | 395717    | Leggett Street |
| 76054385       | 449774    | Leggett Street |
| 49610011       | 686048    | Leggett Street |
| 16153065       | 458378    | Leggett Street |
| 25506511       | 396669    | Leggett Street |
| 81061156       | 438727    | Leggett Street |
| 26013199       | 514354    | Leggett Street |
+----------------+-----------+----------------+

NAME OF PEOPLE ON THE CULPRIT'S FLIGHT:
+--------+-----------------+-----------+
|  name  | passport_number | flight_id |
+--------+-----------------+-----------+
| Doris  | 7214083635      | 36        |
| Sofia  | 1695452385      | 36        |
| Bruce  | 5773159633      | 36        |
| Edward | 1540955065      | 36        |
| Kelsey | 8294398571      | 36        |
| Taylor | 1988161715      | 36        |
| Kenny  | 9878712108      | 36        |
| Luca   | 8496433585      | 36        |
+--------+-----------------+-----------+

Names of people that withdrew money DURING the said time period

ALL OF THE ACCOUNT NUMBERS FROM LEGGETT STREET WITHDRAW DURING THAT TIME^^

SELECT name, person_id FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id WHERE bank_accounts.person_id = 467400 OR bank_accounts.person_id = 395717 OR bank_accounts.person_id = 449774 OR bank_accounts.person_id = 686048 OR bank_accounts.person_id = 458378 OR bank_accounts.person_id = 396669 OR bank_accounts.person_id = 438727 OR bank_accounts.person_id = 514354;

HINT HERE: ACCOUNT NUMBER
--Eugine's testimony:

--Displays ATM transactions of that time:

SELECT * FROM atm_transactions WHERE atm_location = "Humphrey Lane" AND year = 2021;

--Raymond's Testimony:

--Finding phone calls that match, less than 1 minute. Displays phone number.

SELECT * FROM phone_calls WHERE month = 7 AND day = 28 AND duration < 61;

SELECT people.name, people.phone_number FROM people JOIN phone_calls ON people.phone_number = phone_calls.caller WHERE phone_calls.month = 7 AND phone_calls.day = 28 AND phone_calls.duration < 61;;

+-----+----------------+----------------+------+-------+-----+----------+
| id  |     caller     |    receiver    | year | month | day | duration |
+-----+----------------+----------------+------+-------+-----+----------+
| 221 | (130) 555-0289 | (996) 555-8899 | 2021 | 7     | 28  | 51       |
| 224 | (499) 555-9472 | (892) 555-8872 | 2021 | 7     | 28  | 36       |
| 233 | (367) 555-5533 | (375) 555-8161 | 2021 | 7     | 28  | 45       |
| 234 | (609) 555-5876 | (389) 555-5198 | 2021 | 7     | 28  | 60       |
| 251 | (499) 555-9472 | (717) 555-1342 | 2021 | 7     | 28  | 50       |
| 254 | (286) 555-6063 | (676) 555-6554 | 2021 | 7     | 28  | 43       |
| 255 | (770) 555-1861 | (725) 555-3243 | 2021 | 7     | 28  | 49       |
| 261 | (031) 555-6622 | (910) 555-3251 | 2021 | 7     | 28  | 38       |
| 279 | (826) 555-1652 | (066) 555-9701 | 2021 | 7     | 28  | 55       |
| 281 | (338) 555-6650 | (704) 555-2131 | 2021 | 7     | 28  | 54       |
+-----+----------------+----------------+------+-------+-----+----------+

LIST OF CALLERS NAMES:
+---------+----------------+
| Sofia   | (130) 555-0289 |
| Kelsey  | (499) 555-9472 |
| Bruce   | (367) 555-5533 | &&
| Kathryn | (609) 555-5876 |
| Kelsey  | (499) 555-9472 |
| Taylor  | (286) 555-6063 |
| Diana   | (770) 555-1861 |
| Carina  | (031) 555-6622 |
| Kenny   | (826) 555-1652 |
| Benista | (338) 555-6650 |
+---------+----------------+

SELECT people.name, people.phone_number FROM people JOIN phone_calls ON people.phone_number = phone_calls.receiver WHERE phone_calls.month = 7 AND phone_calls.day = 28 AND phone_calls.duration < 61;;

RECIEVERS OF THE CALLS:

+------------+----------------+
| Jack       | (996) 555-8899 |
| Larry      | (892) 555-8872 |
| Robin      | (375) 555-8161 |
| Luca       | (389) 555-5198 |
| Melissa    | (717) 555-1342 |
| James      | (676) 555-6554 |
| Philip     | (725) 555-3243 |
| Jacqueline | (910) 555-3251 |
| Doris      | (066) 555-9701 |
| Anna       | (704) 555-2131 |
+------------+----------------+

--Display flights during that time, earliest flight:

SELECT * FROM flights WHERE month = 7 AND day = 29 ORDER BY hour ASC limit 1;

+----+-------------------+------------------------+------+-------+-----+------+--------+
| id | origin_airport_id | destination_airport_id | year | month | day | hour | minute |
+----+-------------------+------------------------+------+-------+-----+------+--------+
| 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     |
| 43 | 8                 | 1                      | 2021 | 7     | 29  | 9    | 30     |
| 23 | 8                 | 11                     | 2021 | 7     | 29  | 12   | 15     |
| 53 | 8                 | 9                      | 2021 | 7     | 29  | 15   | 20     |
| 18 | 8                 | 6                      | 2021 | 7     | 29  | 16   | 0      |
+----+-------------------+------------------------+------+-------+-----+------+--------+

--FLIGHT ID = 36. Find passport numbers

SELECT * FROM passengers JOIN people ON passengers.passport_number = people.passport_number WHERE passengers.flight_id = 36;
+-----------+-----------------+------+
| flight_id | passport_number | seat |
+-----------+-----------------+------+
| 36        | 7214083635      | 2A   |
| 36        | 1695452385      | 3B   |
| 36        | 5773159633      | 4A   |
| 36        | 1540955065      | 5C   |
| 36        | 8294398571      | 6C   |
| 36        | 1988161715      | 6D   |
| 36        | 9878712108      | 7A   |
| 36        | 8496433585      | 7B   |
+-----------+-----------------+------+
Expanded:
+--------+-----------------+-----------+
|  name  | passport_number | flight_id |
+--------+-----------------+-----------+
| Doris  | 7214083635      | 36        |
| Sofia  | 1695452385      | 36        |
| Bruce  | 5773159633      | 36        |
| Edward | 1540955065      | 36        |
| Kelsey | 8294398571      | 36        |
| Taylor | 1988161715      | 36        |
| Kenny  | 9878712108      | 36        |
| Luca   | 8496433585      | 36        |
+--------+-----------------+-----------+

--Find People that was on flight 36 that match with their passport numbers and their license plates.

SELECT id, name, license_plate FROM people JOIN passengers ON people.passport_number = passengers.passport_number WHERE flight_id = 36;

+--------+--------+---------------+
|   id   |  name  | license_plate |
+--------+--------+---------------+
| 953679 | Doris  | M51FA04       |
| 398010 | Sofia  | G412CB7       |
| 686048 | Bruce  | 94KL13X       |
| 651714 | Edward | 130LD9Z       |
| 560886 | Kelsey | 0NTHK55       |
| 449774 | Taylor | 1106N58       |
| 395717 | Kenny  | 30G67EN       |
| 467400 | Luca   | 4328GD8       |
+--------+--------+---------------+
ALL THE PEOPLE ON THE FLIGHT

--Functions to compare
--SELECT * FROM bakery_security_logs WHERE month = 7 AND day = 28 AND hour =10 AND minute >15 AND minute < 25;
--SELECT id, name, license_plate FROM people JOIN passengers ON people.passport_number = passengers.passport_number WHERE flight_id = 36;
--BREAK

+--------+---------+----------------+-----------------+---------------+
|   id   |  name   |  phone_number  | passport_number | license_plate |
+--------+---------+----------------+-----------------+---------------+
| 221103 | Vanessa | (725) 555-4692 | 2963008352      | 5P2BI95       |
| 243696 | Barry   | (301) 555-4174 | 7526138472      | 6P58WS2       |
| 396669 | Iman    | (829) 555-5269 | 7049073643      | L93JTIZ       |
| 398010 | Sofia   | (130) 555-0289 | 1695452385      | G412CB7       |
| 467400 | Luca    | (389) 555-5198 | 8496433585      | 4328GD8       |
| 514354 | Diana   | (770) 555-1861 | 3592750733      | 322W7JE       |
| 560886 | Kelsey  | (499) 555-9472 | 8294398571      | 0NTHK55       |
| 686048 | Bruce   | (367) 555-5533 | 5773159633      | 94KL13X       |
+--------+---------+----------------+-----------------+---------------+

--Code finds ALL names of people where license plate matches with people in the flight. Just comparing it one by one: BRUCE and KELSEY. Matching license plate from bakery and on flight.

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