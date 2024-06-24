
-- 0)Make a new table employee with specified column id, name, position and salary.
-- 1)insert query adds a new row to the employees table with specific values for id, name, position, and salary.
-- 2)update query updates the salary of the employee with id = 1.
-- 3)delete query deletes the row from employees where id = 1.
-- 4)create a query that creates a table called students.

	The foreign key constraint ensures that the course_id in students must refer to a valid course_id in the courses table.
-- 
-- 


create database amazon;
use amazon;

create table products
(
    product_id int primary key,
    product_name varchar(45) not null,
    price int 
    stock int not null,
    location varchar(45) check(locaiton in ('chennai' , 'madurai'))
);
--0
create table employee
(
    column_id int primary key,
    name varchar(45) not null,
    position varchar(45) not null,
    salary int(10) not null,
);

--1
Insert into employee(column_id,name,position,salary) values('1','ajay','intern','10000');

--2
update employee
set salary = 15000
where id = 1;

--3
delete from employee
where id = 1;

--4
create table students(
  student_id INT PRIMARY KEY,       
  name VARCHAR(100) NOT NULL,        
  email VARCHAR(100) UNIQUE,       
  age INT CHECK (age >= 18),        
  course_id INT,                    
  grade CHAR(1) DEFAULT 'F'          
);

-- 5)create another table courses and set up a foreign key constraint in the students table.

create table courses
(
    course_id int primary key,
    title varchar(100) not null,
);


--6)Alter the students table to add the foreign key constraint.

alter table students
Add constraint fk_course
foreign key (course_id)
on delete cascade;

--7)insert some data into the students table while respecting the constraints.

insert into students (student_id, name, email, age, course_id, grade)
VALUES (1, 'Alice Johnson', 'alice@example.com', 21, 101, 'A');  

-- 8)create a SELECT query that retrieves products based on numeric and date conditions.

select * from products
where price > 1000 and date > '2002-01-01';

-- 10)delete products with stock below a certain threshold.
delete from products
where stock < 10;


eate database amazon;

#using databse
use amazon;

-- Creating table Products - pid, pname, price, stock, location (Mumbai or Delhi)
create table products
(
	pid int(3) primary key,
    pname varchar(50) not null,
    price int(10) not null,
    stock int(5),
    location varchar(30) check(location in ('Mumbai','Delhi'))
);

-- Creating table Customer - cid, cname, age, addr
create table customer
(
	cid int(3) primary key,
    cname varchar(30) not null,
    age int(3),
    addr varchar(50)
);

-- Creating table Orders - oid, cid, pid, amt
create table orders
(
	oid int(3) primary key,
    cid int(3),
    pid int(3),
    amt int(10) not null,
    foreign key(cid) references customer(cid),
    foreign key(pid) references products(pid)
);


-- Creating table Payment - pay_id, oid,amount, mode(upi, cerdit, debit), status
create table payment
(
	pay_id int(3) primary key,
    oid int(3),
    amount int(10) not null,
    mode varchar(30) check(mode in('upi','credit','debit')),
    status varchar(30),
    foreign key(oid) references orders(oid)
);

--Creating table employee - eid, ename, phone_no., department, manager_id
CREATE TABLE employee(
eid INT(4) PRIMARY KEY,
ename VARCHAR(40) NOT NULL,
phone_no INT(10) NOT NULL,
department VARCHAR(40) NOT NULL,
manager_id INT(4)
);


--1 display details of all orders which were delivered from "Mumbai"

Select * from orders
Left Join products on orders.pid = products.pid
where products.location = "Mumbai";

-- Display details of all orders whose payment was made through "UPI"

Select * from orders
Right Join payment on payment.oid = orders.id
where payment.mode = "UPI";

--Dispaly oid, amt, cname, payment mode of orders which were made by people below 30 years

Select orders.oid,amt,mode from payment
Right Join orders on payment.oid = orders.oid
and
Select cname from orders
Left Join customer on customer.cid = orders.cid 
where customer.age<30

--Dispaly oid, amt, cname, paymentmode of orders which were made by people below 30 years and payment was made through "Credit"

Select 
    orders.oid
    orders.amt
    customer.cname
    payment.mode
from
    orders
Inner join customer on customer.cid = orders.cid
Inner join payment on payment.oid = orders.oid
where customer.age < 30 and mode = "Credit";

--Display oid, amount, cname, pname, location of the orders whose payment is still pending or in process

Select oid, amt, cname, pname, location from orders
Inner