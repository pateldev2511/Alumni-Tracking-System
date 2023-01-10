-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 29, 2020 at 06:34 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ats`
--

-- --------------------------------------------------------

--
-- Table structure for table `association`
--

CREATE TABLE `association` (
  `association_id` int(11) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `country_code` int(5) NOT NULL,
  `mobile_number` bigint(13) NOT NULL,
  `password` varchar(300) NOT NULL,
  `consent_letter` varchar(500) NOT NULL,
  `isEmailVerified` varchar(3) NOT NULL,
  `isMobileVerified` varchar(3) NOT NULL,
  `isAssociationVerified` varchar(3) NOT NULL,
  `verification_code` varchar(300) NOT NULL,
  `otp` int(8) NOT NULL,
  `account_status` varchar(50) NOT NULL,
  `time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_basic_profile_details`
--

CREATE TABLE `association_basic_profile_details` (
  `id` int(11) NOT NULL,
  `association_id` int(11) NOT NULL,
  `address` varchar(5000) NOT NULL,
  `country` varchar(200) NOT NULL,
  `state` varchar(200) NOT NULL,
  `city` varchar(200) NOT NULL,
  `zip_code` int(11) NOT NULL,
  `hometown` varchar(1000) NOT NULL,
  `current_location` varchar(1000) NOT NULL,
  `profile_image` varchar(5000) NOT NULL,
  `date_of_birth` date NOT NULL,
  `gender` varchar(20) NOT NULL,
  `summary` varchar(2000) NOT NULL,
  `isEmailUpdateRequested` varchar(10) NOT NULL,
  `isMobileUpdateRequested` varchar(10) NOT NULL,
  `expertise` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_cron_details`
--

CREATE TABLE `association_cron_details` (
  `job_id` int(11) NOT NULL,
  `association_id` int(11) NOT NULL,
  `table_name` varchar(500) NOT NULL,
  `type` varchar(10) NOT NULL,
  `title` varchar(500) NOT NULL,
  `message` mediumtext NOT NULL,
  `send_not_alumni` varchar(10) NOT NULL,
  `send_not_colleges` varchar(10) NOT NULL,
  `send_not_association` varchar(10) NOT NULL,
  `status_send_not_alumni` varchar(50) NOT NULL,
  `status_send_not_colleges` varchar(50) NOT NULL,
  `status_send_not_association` varchar(50) NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_discussion`
--

CREATE TABLE `association_discussion` (
  `id` int(11) NOT NULL,
  `association_id` int(11) NOT NULL,
  `discussion_title` mediumtext NOT NULL,
  `tags` varchar(500) NOT NULL,
  `total_views` int(11) NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_discussion_comments`
--

CREATE TABLE `association_discussion_comments` (
  `id` int(11) NOT NULL,
  `discussion_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `membership_type` varchar(50) NOT NULL,
  `comment` mediumtext NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_education_details`
--

CREATE TABLE `association_education_details` (
  `id` int(11) NOT NULL,
  `association_id` int(11) NOT NULL,
  `name_of_institute` varchar(2000) NOT NULL,
  `start_year` int(11) NOT NULL,
  `graduation_year` int(11) NOT NULL,
  `degree` varchar(1000) NOT NULL,
  `department` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_email_cron_02aa6604c42611eab405f8cab83da125`
--

CREATE TABLE `association_email_cron_02aa6604c42611eab405f8cab83da125` (
  `id` int(20) UNSIGNED NOT NULL,
  `membership_type` varchar(30) NOT NULL,
  `email` varchar(200) NOT NULL,
  `isEmailSent` varchar(10) NOT NULL,
  `date_time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_events`
--

CREATE TABLE `association_events` (
  `event_id` int(11) NOT NULL,
  `association_id` int(11) NOT NULL,
  `event_name` varchar(5000) NOT NULL,
  `event_logo` varchar(5000) NOT NULL,
  `event_description` mediumtext NOT NULL,
  `event_venue` varchar(1000) NOT NULL,
  `start_date_time` datetime NOT NULL,
  `end_date_time` datetime NOT NULL,
  `event_fee` int(20) NOT NULL,
  `event_tickets_to_sell` int(10) NOT NULL,
  `isBookingAllowed` varchar(3) NOT NULL,
  `isActive` varchar(20) NOT NULL,
  `last_modified_by` int(11) NOT NULL,
  `last_modified_time` datetime NOT NULL,
  `send_notification_to_other_association_members` varchar(3) NOT NULL,
  `send_notification_to_colleges` varchar(3) NOT NULL,
  `send_notification_to_alumni` varchar(3) NOT NULL,
  `time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_inquiry`
--

CREATE TABLE `association_inquiry` (
  `id` int(11) NOT NULL,
  `first_name` varchar(200) NOT NULL,
  `last_name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `mobile_no` bigint(20) NOT NULL,
  `subject` varchar(2000) NOT NULL,
  `message` varchar(5000) NOT NULL,
  `isResponsed` varchar(5) NOT NULL,
  `responsed_by_association_id` int(11) NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_magazines`
--

CREATE TABLE `association_magazines` (
  `id` int(11) NOT NULL,
  `association_id` int(11) NOT NULL,
  `magazine_title` varchar(1000) NOT NULL,
  `magazine_description` varchar(5000) NOT NULL,
  `magazine_poster` varchar(5000) NOT NULL,
  `magazine_file` varchar(5000) NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_news`
--

CREATE TABLE `association_news` (
  `id` int(11) NOT NULL,
  `association_id` int(11) NOT NULL,
  `news_title` varchar(1000) NOT NULL,
  `news_image` varchar(1000) NOT NULL,
  `news_description` mediumtext NOT NULL,
  `news_categories` varchar(1000) NOT NULL,
  `total_views` int(11) NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_poll_details`
--

CREATE TABLE `association_poll_details` (
  `id` int(11) NOT NULL,
  `association_id` int(11) NOT NULL,
  `poll_table_name` varchar(500) NOT NULL,
  `poll_question` varchar(1000) NOT NULL,
  `option_1` varchar(1000) NOT NULL,
  `option_2` varchar(1000) NOT NULL,
  `option_3` varchar(1000) NOT NULL,
  `option_4` varchar(1000) NOT NULL,
  `total_votes_for_option_1` int(11) NOT NULL,
  `total_votes_for_option_2` int(11) NOT NULL,
  `total_votes_for_option_3` int(11) NOT NULL,
  `total_votes_for_option_4` int(11) NOT NULL,
  `total_options` int(11) NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_poll_response_4e68b4cdc57211eaaf3180000bda9a1b`
--

CREATE TABLE `association_poll_response_4e68b4cdc57211eaaf3180000bda9a1b` (
  `id` int(20) UNSIGNED NOT NULL,
  `membership_type` varchar(30) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `voted_option` int(11) NOT NULL,
  `date_time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_poll_response_35f59210c57211ea9fba80000bda9a1b`
--

CREATE TABLE `association_poll_response_35f59210c57211ea9fba80000bda9a1b` (
  `id` int(20) UNSIGNED NOT NULL,
  `membership_type` varchar(30) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `voted_option` int(11) NOT NULL,
  `date_time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_poll_response_439acf36c57211ea9da180000bda9a1b`
--

CREATE TABLE `association_poll_response_439acf36c57211ea9da180000bda9a1b` (
  `id` int(20) UNSIGNED NOT NULL,
  `membership_type` varchar(30) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `voted_option` int(11) NOT NULL,
  `date_time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_poll_response_606c778dcc8a11ea81c980000bda9a1b`
--

CREATE TABLE `association_poll_response_606c778dcc8a11ea81c980000bda9a1b` (
  `id` int(20) UNSIGNED NOT NULL,
  `membership_type` varchar(30) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `voted_option` int(11) NOT NULL,
  `date_time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_poll_response_d37a1a31c63a11ea867f80000bda9a1b`
--

CREATE TABLE `association_poll_response_d37a1a31c63a11ea867f80000bda9a1b` (
  `id` int(20) UNSIGNED NOT NULL,
  `membership_type` varchar(30) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `voted_option` int(11) NOT NULL,
  `date_time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_poll_response_e83a3cefcc8711eaa8dc80000bda9a1b`
--

CREATE TABLE `association_poll_response_e83a3cefcc8711eaa8dc80000bda9a1b` (
  `id` int(20) UNSIGNED NOT NULL,
  `membership_type` varchar(30) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `voted_option` int(11) NOT NULL,
  `date_time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_sms_cron_7475a948c43c11eabb8a80000bda9a1b`
--

CREATE TABLE `association_sms_cron_7475a948c43c11eabb8a80000bda9a1b` (
  `id` int(20) UNSIGNED NOT NULL,
  `membership_type` varchar(30) NOT NULL,
  `mobile_number` bigint(20) NOT NULL,
  `isSMSSent` varchar(10) NOT NULL,
  `date_time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_special_interest_groups`
--

CREATE TABLE `association_special_interest_groups` (
  `id` int(11) NOT NULL,
  `association_id` int(11) NOT NULL,
  `group_title` varchar(1000) NOT NULL,
  `group_description` varchar(5000) NOT NULL,
  `poster_image` varchar(1000) NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_special_interest_groups_comments`
--

CREATE TABLE `association_special_interest_groups_comments` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `membership_type` varchar(50) NOT NULL,
  `comment` mediumtext NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_special_interest_groups_members`
--

CREATE TABLE `association_special_interest_groups_members` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `alumni_id` int(11) NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `association_work_details`
--

CREATE TABLE `association_work_details` (
  `id` int(11) NOT NULL,
  `association_id` int(11) NOT NULL,
  `work_title` varchar(1000) NOT NULL,
  `company_name` varchar(1000) NOT NULL,
  `work_industry` varchar(500) NOT NULL,
  `from_month` varchar(100) NOT NULL,
  `from_year` int(11) NOT NULL,
  `isWorkingNow` varchar(10) NOT NULL,
  `to_year` int(11) NOT NULL,
  `to_month` varchar(200) NOT NULL,
  `achievement` varchar(2000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `blog_post_alumni`
--

CREATE TABLE `blog_post_alumni` (
  `post_id` int(11) NOT NULL,
  `alumni_id` int(11) NOT NULL,
  `post_title` varchar(1000) NOT NULL,
  `post_description` varchar(5000) NOT NULL,
  `total_views` int(11) NOT NULL,
  `time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `blog_post_association`
--

CREATE TABLE `blog_post_association` (
  `post_id` int(11) NOT NULL,
  `association_id` int(11) NOT NULL,
  `post_image` varchar(1000) NOT NULL,
  `post_title` varchar(1000) NOT NULL,
  `post_description` mediumtext NOT NULL,
  `tags` varchar(500) NOT NULL,
  `category` varchar(500) NOT NULL,
  `total_views` int(11) NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `blog_post_college`
--

CREATE TABLE `blog_post_college` (
  `post_id` int(11) NOT NULL,
  `college_id` int(11) NOT NULL,
  `post_title` varchar(1000) NOT NULL,
  `post_description` mediumtext NOT NULL,
  `total_views` int(11) NOT NULL,
  `time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `chat`
--

CREATE TABLE `chat` (
  `id` int(11) NOT NULL,
  `from_type` varchar(100) NOT NULL,
  `from_id` int(11) NOT NULL,
  `to_type` varchar(100) NOT NULL,
  `to_id` int(11) NOT NULL,
  `message` varchar(5000) NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `cities`
--

CREATE TABLE `cities` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `state_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `colleges`
--

CREATE TABLE `colleges` (
  `college_id` int(11) NOT NULL,
  `college_name` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `college_basic_profile_details`
--

CREATE TABLE `college_basic_profile_details` (
  `id` int(11) NOT NULL,
  `spoc_id` int(11) NOT NULL,
  `address` varchar(2000) NOT NULL,
  `country` varchar(200) NOT NULL,
  `state` varchar(200) NOT NULL,
  `city` varchar(200) NOT NULL,
  `zip_code` int(11) NOT NULL,
  `hometown` varchar(2000) NOT NULL,
  `current_location` varchar(2000) NOT NULL,
  `profile_image` varchar(2000) NOT NULL,
  `date_of_birth` date NOT NULL,
  `gender` varchar(20) NOT NULL,
  `summary` varchar(2000) NOT NULL,
  `isEmailUpdateRequested` varchar(10) NOT NULL,
  `isMobileUpdateRequested` varchar(10) NOT NULL,
  `expertise` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `college_degrees`
--

CREATE TABLE `college_degrees` (
  `degree_id` int(11) NOT NULL,
  `college_id` int(10) NOT NULL,
  `degree_name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `college_education_details`
--

CREATE TABLE `college_education_details` (
  `id` int(11) NOT NULL,
  `spoc_id` int(11) NOT NULL,
  `name_of_institute` varchar(2000) NOT NULL,
  `start_year` int(11) NOT NULL,
  `graduation_year` int(11) NOT NULL,
  `degree` varchar(1000) NOT NULL,
  `department` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `college_spoc`
--

CREATE TABLE `college_spoc` (
  `spoc_id` int(11) NOT NULL,
  `college_id` int(10) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(150) NOT NULL,
  `country_code` int(5) NOT NULL,
  `mobile_number` bigint(15) NOT NULL,
  `password` varchar(500) NOT NULL,
  `college` varchar(600) NOT NULL,
  `consent_letter` varchar(5000) NOT NULL,
  `isEmailVerified` varchar(3) NOT NULL,
  `isMobileVerified` varchar(3) NOT NULL,
  `isSpocVerified` varchar(3) NOT NULL,
  `verification_code` varchar(500) NOT NULL,
  `otp` int(8) NOT NULL,
  `account_status` varchar(50) NOT NULL,
  `time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `college_work_details`
--

CREATE TABLE `college_work_details` (
  `id` int(11) NOT NULL,
  `spoc_id` int(11) NOT NULL,
  `work_title` varchar(1000) NOT NULL,
  `company_name` varchar(1000) NOT NULL,
  `work_industry` varchar(500) NOT NULL,
  `from_month` varchar(100) NOT NULL,
  `from_year` int(11) NOT NULL,
  `isWorkingNow` varchar(10) NOT NULL,
  `to_year` int(11) NOT NULL,
  `to_month` varchar(200) NOT NULL,
  `achievement` varchar(2000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `countries`
--

CREATE TABLE `countries` (
  `id` int(11) NOT NULL,
  `sortname` varchar(3) NOT NULL,
  `name` varchar(150) NOT NULL,
  `phonecode` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `cron_event_1`
--

CREATE TABLE `cron_event_1` (
  `id` int(11) NOT NULL,
  `event_id` int(10) DEFAULT NULL,
  `a_c_a_id` int(10) NOT NULL,
  `membership_type` varchar(50) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `mobile_no` bigint(13) DEFAULT NULL,
  `isEmailSent` varchar(3) DEFAULT NULL,
  `isSMSSent` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `fund_raising_projects`
--

CREATE TABLE `fund_raising_projects` (
  `id` int(11) NOT NULL,
  `membership_type` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  `college` varchar(2000) NOT NULL,
  `project_title` varchar(500) NOT NULL,
  `project_description` mediumtext NOT NULL,
  `project_poster` varchar(2000) NOT NULL,
  `project_documents` varchar(10000) NOT NULL,
  `project_goal_amount` bigint(20) NOT NULL,
  `project_collected_amount` bigint(20) NOT NULL,
  `isVerifiedByCollege` varchar(10) NOT NULL,
  `verifiedBySpocId` int(11) NOT NULL,
  `isVerifiedByAssociation` varchar(10) NOT NULL,
  `verifiedByAssociationId` int(11) NOT NULL,
  `status` varchar(100) NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `fund_raising_projects_payments`
--

CREATE TABLE `fund_raising_projects_payments` (
  `id` int(11) NOT NULL,
  `project_id` int(11) NOT NULL,
  `membership_type` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  `payment_id` varchar(5000) NOT NULL,
  `order_id` varchar(5000) NOT NULL,
  `payment_amount` float NOT NULL,
  `payment_fee` float NOT NULL,
  `payment_method` varchar(500) NOT NULL,
  `payment_email` varchar(200) NOT NULL,
  `payment_contact` bigint(20) NOT NULL,
  `payment_status` varchar(200) NOT NULL,
  `payment_done` varchar(200) NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `groups`
--

CREATE TABLE `groups` (
  `id` int(11) NOT NULL,
  `membership_type` varchar(50) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `group_name` varchar(60) NOT NULL,
  `group_description` varchar(100) NOT NULL,
  `group_image` varchar(5000) NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `group_members`
--

CREATE TABLE `group_members` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `membership_type` varchar(100) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `type` varchar(200) NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `group_messages`
--

CREATE TABLE `group_messages` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `membership_type` varchar(100) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `message` varchar(5000) NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `jobs`
--

CREATE TABLE `jobs` (
  `job_id` int(11) NOT NULL,
  `alumni_id` int(10) NOT NULL,
  `job_name` varchar(100) NOT NULL,
  `job_desc` varchar(1000) NOT NULL,
  `job_salary` bigint(12) NOT NULL,
  `due_date` date NOT NULL,
  `total_applicants` int(10) NOT NULL,
  `total_views` int(10) NOT NULL,
  `total_interested` int(10) NOT NULL,
  `total_not_interested` int(10) NOT NULL,
  `time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `job_applicants`
--

CREATE TABLE `job_applicants` (
  `applicant_id` int(11) NOT NULL,
  `job_id` int(10) NOT NULL,
  `alumni_id` int(10) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(250) NOT NULL,
  `mobile_no` bigint(20) NOT NULL,
  `isApproved` varchar(5) NOT NULL,
  `time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `network`
--

CREATE TABLE `network` (
  `id` int(11) NOT NULL,
  `from_type` varchar(100) NOT NULL,
  `from_id` int(11) NOT NULL,
  `to_type` varchar(100) NOT NULL,
  `to_id` int(11) NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `news`
--

CREATE TABLE `news` (
  `news_id` int(11) NOT NULL,
  `news_title` varchar(1000) NOT NULL,
  `news_description` mediumtext NOT NULL,
  `total_views` int(11) NOT NULL,
  `time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `states`
--

CREATE TABLE `states` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `country_id` int(11) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(250) NOT NULL,
  `country_code` int(5) NOT NULL,
  `mobile_number` bigint(20) NOT NULL,
  `password` varchar(100) NOT NULL,
  `college` varchar(200) NOT NULL,
  `degree` varchar(150) NOT NULL,
  `enrollment_number` bigint(20) NOT NULL,
  `entry_year` int(5) NOT NULL,
  `passout_year` int(5) NOT NULL,
  `isEmailVerified` varchar(10) NOT NULL,
  `isMobileVerified` varchar(10) NOT NULL,
  `isStudentVerified` varchar(10) NOT NULL,
  `verification_code` varchar(100) NOT NULL,
  `otp` int(6) NOT NULL,
  `account_status` varchar(20) NOT NULL,
  `time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `students_added_by_college`
--

CREATE TABLE `students_added_by_college` (
  `id` int(11) NOT NULL,
  `spoc_id` int(11) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(250) NOT NULL,
  `country_code` int(5) NOT NULL,
  `mobile_number` bigint(20) NOT NULL,
  `college` varchar(500) NOT NULL,
  `degree` varchar(200) NOT NULL,
  `enrollment_number` bigint(20) NOT NULL,
  `entry_year` int(11) NOT NULL,
  `passout_year` int(11) NOT NULL,
  `isEmailVerified` varchar(10) NOT NULL,
  `isMobileVerified` varchar(10) NOT NULL,
  `isStudentVerified` varchar(10) NOT NULL,
  `isEmailSent` varchar(10) NOT NULL,
  `verification_code` varchar(2000) NOT NULL,
  `otp` int(11) NOT NULL,
  `account_status` varchar(200) NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `association`
--
ALTER TABLE `association`
  ADD PRIMARY KEY (`association_id`);

--
-- Indexes for table `association_basic_profile_details`
--
ALTER TABLE `association_basic_profile_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `association_cron_details`
--
ALTER TABLE `association_cron_details`
  ADD PRIMARY KEY (`job_id`);

--
-- Indexes for table `association_discussion`
--
ALTER TABLE `association_discussion`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `association_discussion_comments`
--
ALTER TABLE `association_discussion_comments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `association_education_details`
--
ALTER TABLE `association_education_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `association_email_cron_02aa6604c42611eab405f8cab83da125`
--
ALTER TABLE `association_email_cron_02aa6604c42611eab405f8cab83da125`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `association_events`
--
ALTER TABLE `association_events`
  ADD PRIMARY KEY (`event_id`);

--
-- Indexes for table `association_inquiry`
--
ALTER TABLE `association_inquiry`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `association_magazines`
--
ALTER TABLE `association_magazines`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `association_news`
--
ALTER TABLE `association_news`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `association_poll_details`
--
ALTER TABLE `association_poll_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `association_poll_response_4e68b4cdc57211eaaf3180000bda9a1b`
--
ALTER TABLE `association_poll_response_4e68b4cdc57211eaaf3180000bda9a1b`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `association_poll_response_35f59210c57211ea9fba80000bda9a1b`
--
ALTER TABLE `association_poll_response_35f59210c57211ea9fba80000bda9a1b`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `association_poll_response_439acf36c57211ea9da180000bda9a1b`
--
ALTER TABLE `association_poll_response_439acf36c57211ea9da180000bda9a1b`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `association_poll_response_606c778dcc8a11ea81c980000bda9a1b`
--
ALTER TABLE `association_poll_response_606c778dcc8a11ea81c980000bda9a1b`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `association_poll_response_d37a1a31c63a11ea867f80000bda9a1b`
--
ALTER TABLE `association_poll_response_d37a1a31c63a11ea867f80000bda9a1b`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `association_poll_response_e83a3cefcc8711eaa8dc80000bda9a1b`
--
ALTER TABLE `association_poll_response_e83a3cefcc8711eaa8dc80000bda9a1b`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `association_sms_cron_7475a948c43c11eabb8a80000bda9a1b`
--
ALTER TABLE `association_sms_cron_7475a948c43c11eabb8a80000bda9a1b`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `association_special_interest_groups`
--
ALTER TABLE `association_special_interest_groups`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `association_special_interest_groups_comments`
--
ALTER TABLE `association_special_interest_groups_comments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `association_special_interest_groups_members`
--
ALTER TABLE `association_special_interest_groups_members`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `association_work_details`
--
ALTER TABLE `association_work_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `blog_post_association`
--
ALTER TABLE `blog_post_association`
  ADD PRIMARY KEY (`post_id`);

--
-- Indexes for table `chat`
--
ALTER TABLE `chat`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cities`
--
ALTER TABLE `cities`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `colleges`
--
ALTER TABLE `colleges`
  ADD PRIMARY KEY (`college_id`);

--
-- Indexes for table `college_basic_profile_details`
--
ALTER TABLE `college_basic_profile_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `college_degrees`
--
ALTER TABLE `college_degrees`
  ADD PRIMARY KEY (`degree_id`);

--
-- Indexes for table `college_education_details`
--
ALTER TABLE `college_education_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `college_spoc`
--
ALTER TABLE `college_spoc`
  ADD PRIMARY KEY (`spoc_id`);

--
-- Indexes for table `college_work_details`
--
ALTER TABLE `college_work_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `countries`
--
ALTER TABLE `countries`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cron_event_1`
--
ALTER TABLE `cron_event_1`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `fund_raising_projects`
--
ALTER TABLE `fund_raising_projects`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `fund_raising_projects_payments`
--
ALTER TABLE `fund_raising_projects_payments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `groups`
--
ALTER TABLE `groups`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `group_members`
--
ALTER TABLE `group_members`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `group_messages`
--
ALTER TABLE `group_messages`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `jobs`
--
ALTER TABLE `jobs`
  ADD PRIMARY KEY (`job_id`);

--
-- Indexes for table `job_applicants`
--
ALTER TABLE `job_applicants`
  ADD PRIMARY KEY (`applicant_id`);

--
-- Indexes for table `network`
--
ALTER TABLE `network`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `states`
--
ALTER TABLE `states`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `students_added_by_college`
--
ALTER TABLE `students_added_by_college`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `association`
--
ALTER TABLE `association`
  MODIFY `association_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_basic_profile_details`
--
ALTER TABLE `association_basic_profile_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_cron_details`
--
ALTER TABLE `association_cron_details`
  MODIFY `job_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_discussion`
--
ALTER TABLE `association_discussion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_discussion_comments`
--
ALTER TABLE `association_discussion_comments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_education_details`
--
ALTER TABLE `association_education_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_email_cron_02aa6604c42611eab405f8cab83da125`
--
ALTER TABLE `association_email_cron_02aa6604c42611eab405f8cab83da125`
  MODIFY `id` int(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_events`
--
ALTER TABLE `association_events`
  MODIFY `event_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_inquiry`
--
ALTER TABLE `association_inquiry`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_magazines`
--
ALTER TABLE `association_magazines`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_news`
--
ALTER TABLE `association_news`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_poll_details`
--
ALTER TABLE `association_poll_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_poll_response_4e68b4cdc57211eaaf3180000bda9a1b`
--
ALTER TABLE `association_poll_response_4e68b4cdc57211eaaf3180000bda9a1b`
  MODIFY `id` int(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_poll_response_35f59210c57211ea9fba80000bda9a1b`
--
ALTER TABLE `association_poll_response_35f59210c57211ea9fba80000bda9a1b`
  MODIFY `id` int(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_poll_response_439acf36c57211ea9da180000bda9a1b`
--
ALTER TABLE `association_poll_response_439acf36c57211ea9da180000bda9a1b`
  MODIFY `id` int(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_poll_response_606c778dcc8a11ea81c980000bda9a1b`
--
ALTER TABLE `association_poll_response_606c778dcc8a11ea81c980000bda9a1b`
  MODIFY `id` int(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_poll_response_d37a1a31c63a11ea867f80000bda9a1b`
--
ALTER TABLE `association_poll_response_d37a1a31c63a11ea867f80000bda9a1b`
  MODIFY `id` int(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_poll_response_e83a3cefcc8711eaa8dc80000bda9a1b`
--
ALTER TABLE `association_poll_response_e83a3cefcc8711eaa8dc80000bda9a1b`
  MODIFY `id` int(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_sms_cron_7475a948c43c11eabb8a80000bda9a1b`
--
ALTER TABLE `association_sms_cron_7475a948c43c11eabb8a80000bda9a1b`
  MODIFY `id` int(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_special_interest_groups`
--
ALTER TABLE `association_special_interest_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_special_interest_groups_comments`
--
ALTER TABLE `association_special_interest_groups_comments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_special_interest_groups_members`
--
ALTER TABLE `association_special_interest_groups_members`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `association_work_details`
--
ALTER TABLE `association_work_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `blog_post_association`
--
ALTER TABLE `blog_post_association`
  MODIFY `post_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `chat`
--
ALTER TABLE `chat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cities`
--
ALTER TABLE `cities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `colleges`
--
ALTER TABLE `colleges`
  MODIFY `college_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `college_basic_profile_details`
--
ALTER TABLE `college_basic_profile_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `college_degrees`
--
ALTER TABLE `college_degrees`
  MODIFY `degree_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `college_education_details`
--
ALTER TABLE `college_education_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `college_spoc`
--
ALTER TABLE `college_spoc`
  MODIFY `spoc_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `college_work_details`
--
ALTER TABLE `college_work_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `countries`
--
ALTER TABLE `countries`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cron_event_1`
--
ALTER TABLE `cron_event_1`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `fund_raising_projects`
--
ALTER TABLE `fund_raising_projects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `fund_raising_projects_payments`
--
ALTER TABLE `fund_raising_projects_payments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `groups`
--
ALTER TABLE `groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `group_members`
--
ALTER TABLE `group_members`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `group_messages`
--
ALTER TABLE `group_messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `jobs`
--
ALTER TABLE `jobs`
  MODIFY `job_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `job_applicants`
--
ALTER TABLE `job_applicants`
  MODIFY `applicant_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `network`
--
ALTER TABLE `network`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `states`
--
ALTER TABLE `states`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `students_added_by_college`
--
ALTER TABLE `students_added_by_college`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
