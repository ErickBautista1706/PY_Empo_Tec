-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-11-2023 a las 22:35:17
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `empo`
--
CREATE DATABASE IF NOT EXISTS `empo` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `empo`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cursos`
--

DROP TABLE IF EXISTS `cursos`;
CREATE TABLE `cursos` (
  `ID` int(11) NOT NULL,
  `Titulo` varchar(100) DEFAULT NULL,
  `Descripcion` varchar(200) DEFAULT NULL,
  `Duracion` int(11) DEFAULT NULL,
  `Nivel` varchar(20) DEFAULT NULL,
  `Profesor` int(11) DEFAULT NULL,
  `Imagen` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cursos`
--

INSERT INTO `cursos` (`ID`, `Titulo`, `Descripcion`, `Duracion`, `Nivel`, `Profesor`, `Imagen`) VALUES
(1, 'Introduccion a la Programacion', 'Aprende los conceptos basicos de la programacion', 60, 'Basico', NULL, 'curso1.jpeg'),
(2, 'Diseno de Interfaz de Usuario', 'Descubre los principios de diseno para crear interfaces atractivas', 45, 'Intermedio', NULL, 'curso2.jpeg'),
(3, 'Introduccion al Machine Learning', 'Explora los fundamentos del Machine Learning y sus aplicaciones', 90, 'Avanzado', NULL, 'curso3.jpeg'),
(4, 'Marketing Digital 101', 'Aprende estrategias y tecnicas de marketing digital', 60, 'Basico', NULL, 'curso4.jpeg'),
(5, 'Ingles Conversacional', 'Mejora tus habilidades de conversacion en ingles', 30, 'Intermedio', NULL, 'curso5.jpeg'),
(6, 'Fundamentos de Finanzas', 'Conoce los conceptos basicos de finanzas personales y empresariales', 45, 'Basico', NULL, 'curso6.jpeg'),
(7, 'Fotografia Profesional', 'Aprende tecnicas y trucos para tomar fotografias de calidad', 60, 'Intermedio', NULL, 'curso7.jpeg'),
(8, 'Introduccion al Diseno Grafico', 'Descubre los principios de diseno para crear graficos impactantes', 45, 'Basico', NULL, 'curso8.jpeg'),
(9, 'Programacion Web Avanzada', 'Aprende tecnologias avanzadas para el desarrollo web', 90, 'Avanzado', NULL, 'curso9.jpeg'),
(10, 'Liderazgo y Gestion de Equipos', 'Desarrolla habilidades de liderazgo y gestion efectiva de equipos', 60, 'Intermedio', NULL, 'curso10.jpeg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inscripciones`
--

DROP TABLE IF EXISTS `inscripciones`;
CREATE TABLE `inscripciones` (
  `ID` int(11) NOT NULL,
  `Usuario` int(11) DEFAULT NULL,
  `Curso` int(11) DEFAULT NULL,
  `Progreso` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `inscripciones`
--

INSERT INTO `inscripciones` (`ID`, `Usuario`, `Curso`, `Progreso`) VALUES
(9, 1, 1, NULL),
(11, 1, 9, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `lecciones`
--

DROP TABLE IF EXISTS `lecciones`;
CREATE TABLE `lecciones` (
  `ID` int(11) NOT NULL,
  `Titulo` varchar(100) DEFAULT NULL,
  `Descripcion` varchar(200) DEFAULT NULL,
  `Contenido` text DEFAULT NULL,
  `Curso` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `lecciones`
--

INSERT INTO `lecciones` (`ID`, `Titulo`, `Descripcion`, `Contenido`, `Curso`) VALUES
(1, 'Introduccion a la Programacion', 'Leccion introductoria sobre programacion', 'Contenido de la lecci├│n 1', 1),
(2, 'Variables y Operadores', 'Leccion sobre variables y operadores', 'Contenido de la lecci├│n 2', 1),
(3, 'Diseno de Interfaces', 'Leccion sobre diseno de interfaces de usuario', 'Contenido de la lecci├│n 1', 2),
(4, 'Principios de Usabilidad', 'Leccion sobre principios de usabilidad', 'Contenido de la lecci├│n 2', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `maestros`
--

DROP TABLE IF EXISTS `maestros`;
CREATE TABLE `maestros` (
  `ID` int(11) NOT NULL,
  `Usuario` int(11) DEFAULT NULL,
  `Documento` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `progresolecciones`
--

DROP TABLE IF EXISTS `progresolecciones`;
CREATE TABLE `progresolecciones` (
  `ID` int(11) NOT NULL,
  `Usuario` int(11) DEFAULT NULL,
  `Leccion` int(11) DEFAULT NULL,
  `Estado` enum('Sin empezar','En progreso','Casi completado','Completado') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `progresolecciones`
--

INSERT INTO `progresolecciones` (`ID`, `Usuario`, `Leccion`, `Estado`) VALUES
(1, 1, 1, 'Sin empezar'),
(2, 1, 2, 'En progreso');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE `usuarios` (
  `ID` int(11) NOT NULL,
  `Nombre` varchar(50) DEFAULT NULL,
  `Apellido` varchar(50) DEFAULT NULL,
  `CorreoElectronico` varchar(100) DEFAULT NULL,
  `Contrasena` varchar(100) DEFAULT NULL,
  `Rol` varchar(20) DEFAULT NULL,
  `Imagen` varchar(200) DEFAULT NULL,
  `Activo` tinyint(1) DEFAULT 1,
  `FechaNacimiento` date DEFAULT NULL,
  `PaisOrigen` varchar(50) DEFAULT NULL,
  `InstitutoEmpresa` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`ID`, `Nombre`, `Apellido`, `CorreoElectronico`, `Contrasena`, `Rol`, `Imagen`, `Activo`, `FechaNacimiento`, `PaisOrigen`, `InstitutoEmpresa`) VALUES
(1, 'Erick Jonathan ', 'Bautista Perez', 'erick.bautista577@gmail.com', 'BPmBBO+ZLqRAD8H2DI6i6MUaGH75ki48ee5crW0GzIgVz0xHCA==', 'Alumno', NULL, 1, '2002-06-17', 'Mexico', 'Universidad Politécnica de Pachuca');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Profesor` (`Profesor`);

--
-- Indices de la tabla `inscripciones`
--
ALTER TABLE `inscripciones`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Usuario` (`Usuario`),
  ADD KEY `Curso` (`Curso`);

--
-- Indices de la tabla `lecciones`
--
ALTER TABLE `lecciones`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Curso` (`Curso`);

--
-- Indices de la tabla `maestros`
--
ALTER TABLE `maestros`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Usuario` (`Usuario`);

--
-- Indices de la tabla `progresolecciones`
--
ALTER TABLE `progresolecciones`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Usuario` (`Usuario`),
  ADD KEY `Leccion` (`Leccion`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cursos`
--
ALTER TABLE `cursos`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `inscripciones`
--
ALTER TABLE `inscripciones`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `lecciones`
--
ALTER TABLE `lecciones`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `progresolecciones`
--
ALTER TABLE `progresolecciones`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `cursos`
--
ALTER TABLE `cursos`
  ADD CONSTRAINT `cursos_ibfk_1` FOREIGN KEY (`Profesor`) REFERENCES `maestros` (`ID`);

--
-- Filtros para la tabla `inscripciones`
--
ALTER TABLE `inscripciones`
  ADD CONSTRAINT `inscripciones_ibfk_1` FOREIGN KEY (`Usuario`) REFERENCES `usuarios` (`ID`),
  ADD CONSTRAINT `inscripciones_ibfk_2` FOREIGN KEY (`Curso`) REFERENCES `cursos` (`ID`);

--
-- Filtros para la tabla `lecciones`
--
ALTER TABLE `lecciones`
  ADD CONSTRAINT `lecciones_ibfk_1` FOREIGN KEY (`Curso`) REFERENCES `cursos` (`ID`);

--
-- Filtros para la tabla `maestros`
--
ALTER TABLE `maestros`
  ADD CONSTRAINT `maestros_ibfk_1` FOREIGN KEY (`Usuario`) REFERENCES `usuarios` (`ID`);

--
-- Filtros para la tabla `progresolecciones`
--
ALTER TABLE `progresolecciones`
  ADD CONSTRAINT `progresolecciones_ibfk_1` FOREIGN KEY (`Usuario`) REFERENCES `usuarios` (`ID`),
  ADD CONSTRAINT `progresolecciones_ibfk_2` FOREIGN KEY (`Leccion`) REFERENCES `lecciones` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
