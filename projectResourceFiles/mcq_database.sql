-- MySQL Script generated by MySQL Workbench
-- Sun 23 Jul 2017 06:19:46 PM WAT
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema mcq-database
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mcq-database
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mcq-database` ;
USE `mcq-database` ;

-- -----------------------------------------------------
-- Table `mcq-database`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mcq-database`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(60) NULL,
  `status` CHAR(10) NULL DEFAULT 'student',
  `created` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `lastsigned_in` VARCHAR(45) NULL,
  `username` VARCHAR(45) NULL,
  `session` VARCHAR(32) NULL,
  `password` VARCHAR(64) NULL,
  `permission` INT(11) NULL DEFAULT 0 ,
  `banned` TINYINT(1) NULL DEFAULT 0,
  `deleted` TINYINT(1) NULL DEFAULT 0,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mcq-database`.`quiz`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mcq-database`.`quiz` (
  `id` INT(8) NOT NULL AUTO_INCREMENT,
  `uid` INT NOT NULL,
  `title` VARCHAR(200) NULL,
  `created` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `time` INT(3) NULL,
  `start_date` VARCHAR(45) NULL,
  `instructions` TEXT(300) NULL,
  `closed` TINYINT(1) NULL DEFAULT 0,
  `result` CHAR(4) NULL DEFAULT 'mail',
  `student_count` INT(8) NULL DEFAULT 0,
  `show_qtn_marks` TINYINT(1) NULL DEFAULT 0,
  `total_marks` INT(4) NULL DEFAULT 0,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mcq-database`.`question`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mcq-database`.`question` (
  `id` INT(8) NOT NULL AUTO_INCREMENT,
  `quid` INT(8) NOT NULL,
  `type` VARCHAR(45) NULL DEFAULT 'radio',
  `text` TEXT(6000) NULL,
  `created` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `qtn_mark` INT(3) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mcq-database`.`question_options`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mcq-database`.`question_options` (
  `id` INT(8) NOT NULL AUTO_INCREMENT,
  `qtn_id` INT(8) NULL,
  `text` TEXT(6000) NULL,
  `created` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `answer` TINYINT(1) NULL DEFAULT 0,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mcq-database`.`answer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mcq-database`.`answer` (
  `id` INT(8) NOT NULL AUTO_INCREMENT,
  `qnt_id` INT(8) NULL,
  `option_ids` TEXT(6000) NULL,
  `quiz_id` INT(8) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mcq-database`.`answer_has_answer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mcq-database`.`answer_has_answer` (
  `answer_Id` INT(8) NOT NULL,
  `answer_Id1` INT(8) NOT NULL,
  PRIMARY KEY (`answer_Id`))
ENGINE = InnoDB;

USE `mcq-database` ;

-- -----------------------------------------------------
-- Placeholder table for view `mcq-database`.`view1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mcq-database`.`view1` (`id` INT);

-- -----------------------------------------------------
-- View `mcq-database`.`view1`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mcq-database`.`view1`;
USE `mcq-database`;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
