CREATE DATABASE IF NOT EXISTS test;

CREATE TABLE IF NOT EXISTS Student (
Student_id varchar(7),
Address varchar(255),
First_Name varchar(255),
Sur_Name varchar(255),
GPA float(4,3),
PRIMARY KEY(Student_id)
);

CREATE TABLE IF NOT EXISTS  Department (
Dept_id varchar(7),
dept_name varchar(255),
description varchar(255),
PRIMARY KEY (Dept_id)
);

CREATE TABLE IF NOT EXISTS  Other_Names (
Student_id varchar(7),
other_Name varchar (255),
PRIMARY KEY (Student_id,other_Name),
FOREIGN KEY(Student_id) REFERENCES Student(Student_id)
);

CREATE TABLE IF NOT EXISTS  Employe (
id varchar(7),
First_Name varchar(255),
Sur_Name varchar(255),
Salary float(8,2),
Calculated_Salaray float(8,2),
Workfor_deptID varchar(7),
PRIMARY KEY(id),
FOREIGN KEY(Workfor_deptID) REFERENCES Department(Dept_id)
);

CREATE TABLE IF NOT EXISTS  Emp_Names (
id varchar(7),
Name varchar (255),
PRIMARY KEY (id,Name),
FOREIGN KEY(id) REFERENCES Employe(id)
);

CREATE TABLE IF NOT EXISTS  Faculty (
id varchar(7),
PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS  Staff(
id varchar(7),
PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS  Emp_Qualification (
id varchar(7),
Qualification varchar (255),
PRIMARY KEY (id,Qualification),
FOREIGN KEY(id) REFERENCES Faculty(id)
);




CREATE TABLE IF NOT EXISTS  Emp_Management(
Employe_id varchar(7),
Dept_id varchar(7),
PRIMARY KEY (Employe_id, Dept_id),
FOREIGN KEY (Employe_id) REFERENCES Employe(id),
FOREIGN KEY (Dept_id) REFERENCES Department(Dept_id)
);

CREATE TABLE IF NOT EXISTS  Course(
Course_no varchar(6),
title varchar(255),
credits float(2,1),
year2 enum('1','2','3','4'),
Semester_ enum('1','2','3','4','5','6','7','8'),
PRIMARY KEY(Course_no)
);

CREATE TABLE IF NOT EXISTS  Course_Offering (
Section1 varchar(7),
Days enum('Monday','Tuesday','Wednesday','Thursday','Friday'),
Times varchar(255),
location varchar(255),
Course VARCHAR(6),
PRIMARY KEY(Section1),
FOREIGN KEY(Course) REFERENCES Course(Course_no)
);

CREATE TABLE IF NOT EXISTS  Lecture_Section (
Section1 varchar(7),
PRIMARY KEY(Section1)
);

CREATE TABLE IF NOT EXISTS  Lab_Section(
Section1 varchar(7),
PRIMARY KEY(Section1)
);

CREATE TABLE IF NOT EXISTS  Semester(
Semester_no enum('1','2','3','4','5','6','7','8'),
year1 enum('1','2','3','4'),
PRIMARY KEY(Semester_no,year1)
);

CREATE TABLE IF NOT EXISTS  Register (
Stud_id varchar(7),
Course_id varchar(6),
grade Varchar(10),
PRIMARY KEY (Stud_id,Course_id),
FOREIGN KEY(Stud_id) REFERENCES Student(Student_id)
);

CREATE TABLE IF NOT EXISTS  Lectures(
Section_id varchar(7),
Fac_ID varchar (7),
PRIMARY KEY (Section_id,Fac_ID),
FOREIGN KEY(Section_id) REFERENCES Course_Offering(Section1),
FOREIGN KEY(Fac_ID) REFERENCES Faculty(id)
);



 







