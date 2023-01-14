-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 14, 2023 at 10:15 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codingthunder`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `phone_num` text NOT NULL,
  `msg` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `phone_num`, `msg`, `date`, `email`) VALUES
(1, 'Komal', '07665035700', 'sir aapki website bhut hi acchi hai so please isko continue rakhe', '2023-01-10 17:49:14', 'misskomalkumari52@gmail.com'),
(39, 'Manish Kumar Mehta', '07665035700', 'teri sdfjndsndnvdvnvnxnj', '2023-01-10 17:50:56', 'jsddjdvjkdvnxjndj@gmail.com'),
(40, 'Manish Kumar Mehta', '07665035700', 'teri sdfjndsndnvdvnvnxnj', '2023-01-10 17:52:26', 'jsddjdvjkdvnxjndj@gmail.com'),
(41, 'Komal', '07665035700', 'mera naam manis hasiosjsdajsdfjk', '2023-01-10 17:53:54', 'misskomalkumari52@gmail.com'),
(42, 'Komal', '07665035700', 'mera naam koml ai', '2023-01-10 18:01:30', 'misskomalkumari52@gmail.com'),
(43, 'mona losa', '1212121221212', 'mai  hu monalisa dekh lo', '2023-01-10 20:22:29', 'papakipari52@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` varchar(30) NOT NULL,
  `tagline` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` varchar(300) NOT NULL,
  `img_file` varchar(25) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tagline`, `slug`, `content`, `img_file`, `date`) VALUES
(1, 'Power Programer', 'The biggest Power of Programers', 'first-post', 'This is my content and i am very happy so you should also happy for me so give me best of luck that i will able to do anything as i want so give me the congretulation so bye', 'post-bg.jpg', '2023-01-13 13:15:34'),
(2, 'Happy Code', 'Is this true about Coder', 'second-post', 'This is about the happy life of coders which is not true thing because coder always do hard work so you cant say that a coder have a happy life so be unterstand the feeling of a coder.....', 'post-sample-image.jpg', '2023-01-14 09:11:05'),
(10, 'now this is not po okay', 'this is for me', 'this-me', 'this very djfdjfkdjfgkldfnuiofdfjkgd', 'no.png', '2023-01-13 13:20:39'),
(12, 'ab ye papa ban gya hai so be h', 'this is for me', 'this-me', 'this very djfdjfkdjfgkldfnuiofdfjkgd', 'no.png', '2023-01-13 13:21:35'),
(17, 'po', 'this is for me', 'this-me', 'this very djfdjfkdjfgkldfnuiofdfjkgd', 'no.png', '2023-01-13 10:54:47'),
(20, 'po', 'this is for me', 'this-me', 'this very djfdjfkdjfgkldfnuiofdfjkgd', 'no.png', '2023-01-13 10:54:58'),
(22, 'last', 'this is for me', 'this-me', 'this very djfdjfkdjfgkldfnuiofdfjkgd', 'no.png', '2023-01-14 13:52:09');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
