drop table if exists examples;

create table `examples` (
  `id` int not null auto_increment,
  `name` varchar(20) default null,
  primary key (`id`)
);
