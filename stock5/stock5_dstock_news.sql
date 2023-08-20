-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: stock5
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `dstock_news`
--

DROP TABLE IF EXISTS `dstock_news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dstock_news` (
  `id` int NOT NULL AUTO_INCREMENT,
  `news` text,
  `dstock_id` int DEFAULT NULL,
  `news_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dstock_id` (`dstock_id`),
  CONSTRAINT `dstock_news_ibfk_1` FOREIGN KEY (`dstock_id`) REFERENCES `d_stock` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dstock_news`
--

LOCK TABLES `dstock_news` WRITE;
/*!40000 ALTER TABLE `dstock_news` DISABLE KEYS */;
INSERT INTO `dstock_news` VALUES (1,'this is data of abbotindia',93068,'2023-08-01'),(2,'ABB India share price was up by 1.92% based on previous share price of Rs 4,372.95. ',92841,'2023-08-07'),(4,'Adani Enterprises subsidiary Adani Digital Labs acquires 70.19% stake in Stark Enterprises',93620,'2023-08-07'),(5,'What is the target of ABB?\nStock price target for ABB India Limited ABB are 4374.53 on downside and 4512.53 on upside.',92841,'2023-08-08'),(8,'ABB India share price was up by 1.92% based on previous share price of Rs 4,372.95. ',92841,'2023-07-08');
/*!40000 ALTER TABLE `dstock_news` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-20 12:19:15
