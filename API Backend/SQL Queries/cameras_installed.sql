CREATE TABLE `cameras_installed` (
  `CAM_ID` int NOT NULL AUTO_INCREMENT,
  `CAM_LOCATION` longtext,
  `CAM_ADDRESS` longtext,
  `CAM_IP` varchar(100) NOT NULL,
  PRIMARY KEY (`CAM_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;