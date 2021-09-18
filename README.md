# Employee-Management-System

The features that make up this project are mentioned below.
1. Add record
2. List record
3. Modify record
4. Delete record
5. Search record

# SQL Database(Xampp)
create database employee_prj;
CREATE TABLE `employee_prj`.`employee` ( `emp_no` VARCHAR(10) NOT NULL , `name` VARCHAR(100) NOT NULL , `email` VARCHAR(100) NOT NULL , `contact` VARCHAR(50) NOT NULL , `dob` VARCHAR(50) NOT NULL , `gender` VARCHAR(10) NOT NULL , `address` VARCHAR(50) NOT NULL ) ENGINE = InnoDB;
