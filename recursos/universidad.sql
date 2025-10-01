CREATE DATABASE  IF NOT EXISTS `universidad` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `universidad`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: universidad
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `carrera`
--

DROP TABLE IF EXISTS `carrera`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carrera` (
  `idcarrera` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `duracion` decimal(2,1) DEFAULT NULL,
  PRIMARY KEY (`idcarrera`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrera`
--

LOCK TABLES `carrera` WRITE;
/*!40000 ALTER TABLE `carrera` DISABLE KEYS */;
INSERT INTO `carrera` VALUES (1,'Ingeniería Informática',4.0),(2,'Medicina',6.0),(3,'Derecho',5.0),(4,'Arquitectura',5.0),(5,'Psicología',4.0),(6,'Administración y Dirección de Empresas',4.0),(7,'Biología',4.0),(8,'Historia del Arte',4.0),(9,'Filosofía',4.0),(10,'Ingeniería Civil',5.0),(11,'Enfermería',3.5),(12,'Trabajo Social',3.5),(13,'Ingeniería Mecánica',5.0),(14,'Ingeniería Electrónica',5.0),(15,'Ingeniería Química',5.0),(16,'Matemáticas',4.0),(17,'Química',4.5),(18,'Física',4.5),(19,'Ciencias Políticas',4.0),(20,'Relaciones Internacionales',4.0),(21,'Periodismo',4.0),(22,'Comunicación Audiovisual',4.0),(23,'Diseño Gráfico',3.5),(24,'Arte Dramático',3.5),(25,'Música',4.0),(26,'Educación Primaria',4.0),(27,'Educación Infantil',4.0),(28,'Ingeniería en Telecomunicaciones',5.0),(29,'Ingeniería Aeroespacial',5.0),(30,'Ingeniería en Energías Renovables',4.5),(31,'Nutrición y Dietética',4.0),(32,'Odontología',5.0),(33,'Veterinaria',5.0),(34,'Farmacia',5.0),(35,'Turismo',4.0),(36,'Geografía e Historia',4.0),(37,'Ciencias Ambientales',4.5),(38,'Criminología',4.0);
/*!40000 ALTER TABLE `carrera` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-01 19:36:19
