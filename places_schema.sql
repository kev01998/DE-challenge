drop table if exists places;

CREATE TABLE `places`
(
    `city` varchar(90)  not null,
    `county` varchar(80) default null,
    `country` varchar(80) default null,
	primary key (`city`)
);
