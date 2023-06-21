# Episteme: A Knowledge Management System
Episteme is a Knowledge Management System created in partial fulfillment of the requirements of the Asia Pacific College Senior High School SoCIT Bootcamp for the Academic Year 2022 - 2023. It designed for the Asia Pacific College Library for storing and managing theses written by Asia Pacific College students and educators.

## Concept of Episteme
Currently, the Asia Pacific College Library manually sorts and encodes the information from the theses papers of students by using a web application called koha. As per the library administrators, it consumes time from the uploading process of a thesis paper to encoding basic information such as the title of the thesis paper, author, and control number. This manual process is inefficient considering that many papers in Asia Pacific College are being created annually. Moreover, this can lead to data inaccuracy based on factors such as human error and time constraints. As the APC Library envisions a faster process of data entry and an efficient knowledge management system, the developers intend to contribute to the vision by creating a web application, called Episteme, that allow students to encode their theses information instead. 

## How to Run Episteme
To run Episteme, you first need Flask and a MySQL database.

To install a Flask:
1. Install Python 3.x from the official website: https://www.python.org/downloads/
2. Afterwards you can install Flask using pip. Open your terminal and run the following command: pip install flask

To install a MySQL database:   
1. Install MySQL database from the official website: https://dev.mysql.com/downloads/mysql/
2. Once MySQL is installed and opened, create a root account with the password "BigBrews-23"
3. Once that is done, input the following commands:

CREATE TABLE `submissions` (
  `submission_id` int NOT NULL AUTO_INCREMENT,
  `thesis_title` varchar(256) NOT NULL,
  `submission_type` set('Individual','Group') NOT NULL,
  `full_name` varchar(64) DEFAULT NULL,
  `group_name` varchar(64) DEFAULT NULL,
  `member_name1` varchar(64) DEFAULT NULL,
  `member_name2` varchar(64) DEFAULT NULL,
  `member_name3` varchar(64) DEFAULT NULL,
  `professor_name` varchar(64) NOT NULL,
  `submission_date` date NOT NULL,
  `abstract` varchar(8192) NOT NULL,
  `soft_copy` longblob,
  `github_repository` varchar(512) DEFAULT NULL,
  `keywords` varchar(512) DEFAULT NULL,
  `school` varchar(128) NOT NULL,
  `status` set('Submitted','Verified','Published') NOT NULL DEFAULT 'Submitted',
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`submission_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `submissions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

and

CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(64) NOT NULL,
  `last_name` varchar(64) NOT NULL,
  `email_address` varchar(64) NOT NULL,
  `password` varchar(64) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

4. Once completed, you can now run Episteme!

---

## Conclusion of the Project
Knowledge management is a process for existing information in an organization to be managed, structured, and accessed by members of the organization. Currently, the Asia Pacific College Library sorts and encodes the thesis paper in a manual process. While it is available to all library users, indexing and encoding all thesis papers manually are inefficient. Thus, the developers created a web application called Episteme that allow members of the institution to upload their thesis papers and get verified by the library administrators in a swift process. Episteme will allow the improvement of the sorting and encoding process of thesis papers, avoid data inaccuracy, and allow all users to access available thesis papers with convenience. With the aim of improving the current system of the Asia Pacific College’s library system, the project requires the developers to possess soft and technical skills such as communication, problem-solving, web development, and other skills necessary to the development process.  

## Project Team
This project was created by the **Big Brews** consisting of three members with different roles in the team. 
|Member Name|Role|
|---|---|
|Christian Luis Esguerra|Developer/Documentation|
|Angelo John Benedict Laus|Development Lead|
|Joaquin Paolo Pacete|Team Leader/Lead Documentation|

---
