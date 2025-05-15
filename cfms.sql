-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 15, 2025 at 08:01 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cfms`
--

-- --------------------------------------------------------

--
-- Table structure for table `announcements`
--

CREATE TABLE `announcements` (
  `id` varchar(36) NOT NULL,
  `title` varchar(200) NOT NULL,
  `content` text NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `announcements`
--

INSERT INTO `announcements` (`id`, `title`, `content`, `created_at`) VALUES
('1', 'Campus Closure', 'Campus will be closed on May 20, 2025, for maintenance.', '2025-05-12 07:41:27'),
('51406afe-c296-4b02-b715-217240fc14ec', 'Summer vacation closure ', 'Campus will be closed from May 20, 2025 to May 28, 2025 for summer.', '2025-05-12 09:28:06');

-- --------------------------------------------------------

--
-- Table structure for table `assets`
--

CREATE TABLE `assets` (
  `id` varchar(36) NOT NULL,
  `name` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `assets`
--

INSERT INTO `assets` (`id`, `name`, `type`) VALUES
('1', 'Projector X1', 'projector'),
('2', 'Laptop Dell', 'laptop');

-- --------------------------------------------------------

--
-- Table structure for table `bookings`
--

CREATE TABLE `bookings` (
  `id` varchar(36) NOT NULL,
  `user_id` varchar(36) NOT NULL,
  `facility_id` varchar(36) NOT NULL,
  `booking_date` date NOT NULL,
  `status` enum('pending','approved','rejected') DEFAULT 'pending'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bookings`
--

INSERT INTO `bookings` (`id`, `user_id`, `facility_id`, `booking_date`, `status`) VALUES
('05bf8929-b8bd-43cc-b3ee-390366b14f3f', '029b0379-da78-4665-86af-20387b6593e4', '2', '2025-05-12', 'pending'),
('1', '2', '1', '2025-05-15', 'pending'),
('128ed64c-1ccd-4cd6-8803-ee944bd4674b', '029b0379-da78-4665-86af-20387b6593e4', '3', '2025-05-12', 'pending'),
('2d27a7af-95f0-494f-9365-574735fe9509', '029b0379-da78-4665-86af-20387b6593e4', '0352d641-c544-419e-88d2-8f6322150abf', '2025-05-12', 'pending'),
('82114739-63fa-4d9f-902c-3f0dd40f2ee1', '029b0379-da78-4665-86af-20387b6593e4', '1', '2025-05-12', 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `facilities`
--

CREATE TABLE `facilities` (
  `id` varchar(36) NOT NULL,
  `name` varchar(100) NOT NULL,
  `type` enum('classroom','lab','conference_hall') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `facilities`
--

INSERT INTO `facilities` (`id`, `name`, `type`) VALUES
('0352d641-c544-419e-88d2-8f6322150abf', 'EEE LAB', 'lab'),
('1', 'Room 101', 'classroom'),
('2', 'Computer Lab 1', 'lab'),
('3', 'Conference Hall A', 'conference_hall');

-- --------------------------------------------------------

--
-- Table structure for table `maintenance_requests`
--

CREATE TABLE `maintenance_requests` (
  `id` varchar(36) NOT NULL,
  `user_id` varchar(36) NOT NULL,
  `facility_id` varchar(36) NOT NULL,
  `description` text NOT NULL,
  `status` enum('pending','in_progress','resolved') DEFAULT 'pending',
  `assigned_to` varchar(36) DEFAULT NULL,
  `comment` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `maintenance_requests`
--

INSERT INTO `maintenance_requests` (`id`, `user_id`, `facility_id`, `description`, `status`, `assigned_to`, `comment`) VALUES
('1', '2', '2', 'Broken projector', 'resolved', '3', 'Fixed Now');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` varchar(36) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `role` enum('admin','student','maintenance') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`, `role`) VALUES
('029b0379-da78-4665-86af-20387b6593e4', 'Shadid', 'shadid@gmail.com', 'shadid', 'student'),
('1', 'Admin User', 'admin@cfms.com', 'admin123', 'admin'),
('2', 'John Doe', 'john@cfms.com', 'student123', 'student'),
('3', 'Jane Smith', 'jane@cfms.com', 'maintenance123', 'maintenance'),
('48befe68-cc09-4382-810b-86bbd8b8e582', 'nanak', 'nakin@gmail.com', 'nakin1', 'maintenance'),
('4d1db44f-e702-4fbd-b14f-32e37f695fc1', 'Nakib', 'n@gmail.com', 'nokib1', 'maintenance'),
('9e815a8e-2821-4cdd-b6fe-56bb422a8784', 'kaka', 'kaka@gmail.com', 'kakaka', 'student');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `announcements`
--
ALTER TABLE `announcements`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `assets`
--
ALTER TABLE `assets`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bookings`
--
ALTER TABLE `bookings`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `facility_id` (`facility_id`);

--
-- Indexes for table `facilities`
--
ALTER TABLE `facilities`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `maintenance_requests`
--
ALTER TABLE `maintenance_requests`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `facility_id` (`facility_id`),
  ADD KEY `assigned_to` (`assigned_to`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bookings`
--
ALTER TABLE `bookings`
  ADD CONSTRAINT `bookings_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `bookings_ibfk_2` FOREIGN KEY (`facility_id`) REFERENCES `facilities` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `maintenance_requests`
--
ALTER TABLE `maintenance_requests`
  ADD CONSTRAINT `maintenance_requests_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `maintenance_requests_ibfk_2` FOREIGN KEY (`facility_id`) REFERENCES `facilities` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `maintenance_requests_ibfk_3` FOREIGN KEY (`assigned_to`) REFERENCES `users` (`id`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
