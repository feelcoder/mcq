-- MySQL dump 10.16  Distrib 10.1.22-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: mcq-database
-- ------------------------------------------------------
-- Server version	10.1.22-MariaDB-

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `mcq-database`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `mcq-database` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `mcq-database`;

--
-- Table structure for table `answer`
--

DROP TABLE IF EXISTS `answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `answer` (
  `Id` int(8) NOT NULL AUTO_INCREMENT,
  `qnt_id` int(8) DEFAULT NULL,
  `quid` varchar(45) DEFAULT NULL,
  `option_ids` text,
  `quiz_id` int(8) NOT NULL,
  `question_qtn_Id` int(8) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `fk_answer_quiz_idx` (`quiz_id`),
  KEY `fk_answer_question1_idx` (`question_qtn_Id`),
  CONSTRAINT `fk_answer_question1` FOREIGN KEY (`question_qtn_Id`) REFERENCES `question` (`qtn_Id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_answer_quiz` FOREIGN KEY (`quiz_id`) REFERENCES `quiz` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer`
--

LOCK TABLES `answer` WRITE;
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `answer_has_answer`
--

DROP TABLE IF EXISTS `answer_has_answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `answer_has_answer` (
  `answer_Id` int(8) NOT NULL,
  `answer_Id1` int(8) NOT NULL,
  PRIMARY KEY (`answer_Id`),
  KEY `fk_answer_has_answer_answer2_idx` (`answer_Id1`),
  KEY `fk_answer_has_answer_answer1_idx` (`answer_Id`),
  CONSTRAINT `fk_answer_has_answer_answer1` FOREIGN KEY (`answer_Id`) REFERENCES `answer` (`Id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_answer_has_answer_answer2` FOREIGN KEY (`answer_Id1`) REFERENCES `answer` (`Id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer_has_answer`
--

LOCK TABLES `answer_has_answer` WRITE;
/*!40000 ALTER TABLE `answer_has_answer` DISABLE KEYS */;
/*!40000 ALTER TABLE `answer_has_answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question` (
  `qtn_Id` int(8) NOT NULL,
  `quid` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT 'radio',
  `text` text,
  `created` datetime DEFAULT CURRENT_TIMESTAMP,
  `qtn_mark` int(3) DEFAULT NULL,
  `quiz_id` int(8) NOT NULL,
  `quiz_user_id` int(11) NOT NULL,
  `quiz_question_qtn_Id` int(8) NOT NULL,
  PRIMARY KEY (`qtn_Id`),
  KEY `fk_question_quiz1_idx` (`quiz_id`,`quiz_user_id`,`quiz_question_qtn_Id`),
  CONSTRAINT `fk_question_quiz1` FOREIGN KEY (`quiz_id`) REFERENCES `quiz` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question_options`
--

DROP TABLE IF EXISTS `question_options`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question_options` (
  `id` int(8) NOT NULL,
  `qtn_id:` int(8) DEFAULT NULL,
  `text` text,
  `created` datetime DEFAULT CURRENT_TIMESTAMP,
  `answer` tinyint(1) DEFAULT '0',
  `question_qtn_Id` int(8) NOT NULL,
  `question_quiz_id` int(8) NOT NULL,
  `question_quiz_user_id` int(11) NOT NULL,
  `question_quiz_question_qtn_Id` int(8) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_question_options_question1_idx` (`question_qtn_Id`,`question_quiz_id`,`question_quiz_user_id`,`question_quiz_question_qtn_Id`),
  CONSTRAINT `fk_question_options_question1` FOREIGN KEY (`question_qtn_Id`) REFERENCES `question` (`qtn_Id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_options`
--

LOCK TABLES `question_options` WRITE;
/*!40000 ALTER TABLE `question_options` DISABLE KEYS */;
/*!40000 ALTER TABLE `question_options` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quiz`
--

DROP TABLE IF EXISTS `quiz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `quiz` (
  `id` int(8) NOT NULL AUTO_INCREMENT,
  `uid` varchar(45) DEFAULT NULL,
  `quid` varchar(45) DEFAULT NULL,
  `title` varchar(200) DEFAULT NULL,
  `created` datetime DEFAULT CURRENT_TIMESTAMP,
  `time` int(3) DEFAULT NULL,
  `start_date` varchar(45) DEFAULT NULL,
  `instructions` text,
  `closed` tinyint(1) DEFAULT '0',
  `result` char(4) DEFAULT 'mail',
  `student_count` int(8) DEFAULT '0',
  `show_qtn_marks` tinyint(1) DEFAULT '0',
  `total_marks` int(4) DEFAULT '0',
  `question_qtn_Id` int(8) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `quid_UNIQUE` (`quid`),
  KEY `fk_quiz_user_idx` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quiz`
--

LOCK TABLES `quiz` WRITE;
/*!40000 ALTER TABLE `quiz` DISABLE KEYS */;
INSERT INTO `quiz` VALUES (1,'first1234','5CUHIPQ3W71QVS74XE25BLGH73','chris roger','2017-08-08 21:24:30',54,'2017-08-08 21:14:40','salamG',1,'mail',0,0,80,0),(2,'first1234','SAEUPT662BMCLTJS5KOG4R6TLK','chris roger','2017-08-08 21:24:39',54,'2017-08-08 21:14:40','salamGV',1,'mail',0,0,80,0),(3,'first1234','CDWRRBH46EYAKNF2F4IZWBQOQB','chris rogerfg','2017-08-08 21:25:48',54,'2017-08-08 21:14:40','salamGV',1,'mail',0,0,80,0),(4,'first1234','UUQUXWXXOZLDRNCYXWR7GTGMUS','chris rogerfg','2017-08-08 21:27:30',54,'2017-08-08 21:14:40','salamGV778',1,'mail',0,0,80,0),(5,'first1234','JKHY1V03ESU785YGQL4MOD9U7K','Locko','2017-08-08 23:14:52',50,'2017-08-08 23:13:53','take me out tonight',1,'mail',0,0,30,0),(6,'first1234','2CAJTQPV9BVCAACCXNBP3115U5','Locko','2017-08-08 23:15:41',50,'2017-08-08 23:13:53','take me out tonight',1,'mail',0,0,30,0),(7,'first1234','O7773LGN2LUII9VXYT46ZNF9XV','testla','2017-08-11 18:19:23',56,'2017-08-11 18:17:59','dfsdfsdfs',1,'mail',0,0,20,0),(8,'first1234','RLBSF7BDDYB5G5A50KP490DBW4','takos','2017-08-11 20:53:25',25,'2017-08-11 20:52:26','lefa',1,'mail',0,0,45,0),(9,'first1234','6PW8OIH77GNNF3LP4DU9DZ5O03','killer bean','2017-08-11 21:00:21',25,'2017-08-11 20:59:20','nastra automatic',1,'mail',0,0,42,0),(10,'first1234','8RXOOG951PNHDQQTFLETAMAP0K','sdfsdfsdf','2017-08-11 21:06:15',20,'2017-08-11 21:05:42','sdfsdfsdfsdf',1,'mail',0,0,25,0);
/*!40000 ALTER TABLE `quiz` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` varchar(45) DEFAULT NULL,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `status` char(10) DEFAULT 'student',
  `created` datetime DEFAULT CURRENT_TIMESTAMP,
  `lastsigned_in` varchar(45) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `session` varchar(32) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL,
  `permission` int(11) DEFAULT '0',
  `banned` tinyint(1) DEFAULT '0',
  `deleted` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'first1234','tanero','chris','tanejuth@gmail.com','student','2017-08-08 21:24:24',NULL,NULL,NULL,NULL,0,0,0);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-08-12  1:13:20
