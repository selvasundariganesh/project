create table winner (
winner_year int,
winner_subject varchar(50),
winner_name varchar(50),
winner_country varchar(50),
winner_category varchar(50)
);
insert into winner (winner_year, winner_subject, winner_name, winner_country, winner_category)
values (1994, 'literature', 'kenzaburo oe', 'japan', 'linguist');
insert into winner(winner_year, winner_subject, winner_name, winner_country, winner_category)
values(1994, 'economics', 'reinhard selten', 'germany', 'economics');
insert into winner (winner_year, winner_subject, winner_name, winner_country, winner_category)
values(1987, 'chemistry', 'donald j.cram', 'usa', 'scientist');
insert into winner (winner_year, winner_subject, winner_name, winner_country, winner_category)
values(1987, 'chemistry', 'jean-marie lehn', 'france', 'scientist');
insert into winner (winner_year, winner_subject, winner_name, winner_country, winner_category)
values(1987, 'literature', 'joseph brodsky', 'russia', 'linguist');
insert into winner (winner_year, winner_subject, winner_name, winner_country, winner_category)
values(1987, 'economics', 'robert solow', 'usa', 'economics');
insert into winner (winner_year, winner_subject, winner_name, winner_country, winner_category)
values(1971, 'chemistry', 'gerhard herzberg', 'germany', 'scientist');
insert into winner (winner_year, winner_subject, winner_name, winner_country, winner_category)
values(1971, 'literature', 'pablo neruda', 'chile', 'linguist');
insert into winner (winner_year, winner_subject, winner_name, winner_country, winner_category)
values(1971, 'economics', 'simom kuznets', 'russia', 'economics');
insert into winner (winner_year, winner_subject, winner_name, winner_country, winner_category)
values(1970, 'literature', 'aleksandr solzhenitsyn', 'russia', 'linguist');
insert into winner (winner_year, winner_subject, winner_name, winner_country, winner_category)
values(1970, 'chemistry', 'luis federico leloir', 'france', 'scientist');
insert into winner (winner_year, winner_subject, winner_name, winner_country, winner_category)
values(1970, 'economics', 'paul samuelson', 'usa', 'economics');
select * from winner
select * from winner where winner_name like 'luis%' ;
select * from winner where winner_year=1970 and winner_subject not in ('physiology', 'economics');
select * from winner where winner_subject not like 'p%' order by winner_year desc, winner_name asc;






