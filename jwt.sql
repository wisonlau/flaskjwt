/*
Navicat MySQL Data Transfer

Source Server         : 192.168.173.132_3306
Source Server Version : 50722
Source Host           : 192.168.173.132:3306
Source Database       : jwt

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2019-03-21 09:38:12
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for admin_users
-- ----------------------------
DROP TABLE IF EXISTS `admin_users`;
CREATE TABLE `admin_users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(190) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `avatar` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `remember_token` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `login_time` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_users_username_unique` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of admin_users
-- ----------------------------
INSERT INTO `admin_users` VALUES ('3', 'wison', 'pbkdf2:sha256:50000$4mrb5Asb$7a57e78582b2c8c2e0bb1c44aaf7eff9872c8d8b6b81395844415124061116c9', 'wison', null, null, '2019-03-14 14:32:48', '2019-03-20 12:34:21', '1553056461');
INSERT INTO `admin_users` VALUES ('4', 'wison1', 'pbkdf2:sha256:50000$flB8hKwl$6d6268f7a4babc39441d30217ad43ab05ae8f61f5f566a59b681db4884db2a65', 'wison', '', '', '2019-03-14 14:32:48', '2019-03-15 16:39:10', '1552628866');
INSERT INTO `admin_users` VALUES ('5', 'wison2', 'pbkdf2:sha256:50000$4mrb5Asb$7a57e78582b2c8c2e0bb1c44aaf7eff9872c8d8b6b81395844415124061116c9', 'wison', '', '', '2019-03-14 14:32:48', '2019-03-15 13:47:46', '1552628866');
INSERT INTO `admin_users` VALUES ('6', 'wison3', 'pbkdf2:sha256:50000$4mrb5Asb$7a57e78582b2c8c2e0bb1c44aaf7eff9872c8d8b6b81395844415124061116c9', 'wison', '', '', '2019-03-14 14:32:48', '2019-03-15 13:47:46', '1552628866');
INSERT INTO `admin_users` VALUES ('7', 'wison4', 'pbkdf2:sha256:50000$4mrb5Asb$7a57e78582b2c8c2e0bb1c44aaf7eff9872c8d8b6b81395844415124061116c9', 'wison', '', '', '2019-03-14 14:32:48', '2019-03-15 13:47:46', '1552628866');
INSERT INTO `admin_users` VALUES ('8', 'wison5', 'pbkdf2:sha256:50000$4mrb5Asb$7a57e78582b2c8c2e0bb1c44aaf7eff9872c8d8b6b81395844415124061116c9', 'wison', '', '', '2019-03-14 14:32:48', '2019-03-15 13:47:46', '1552628866');
INSERT INTO `admin_users` VALUES ('9', 'wison6', 'pbkdf2:sha256:50000$4mrb5Asb$7a57e78582b2c8c2e0bb1c44aaf7eff9872c8d8b6b81395844415124061116c9', 'wison', '', '', '2019-03-14 14:32:48', '2019-03-15 13:47:46', '1552628866');
INSERT INTO `admin_users` VALUES ('10', 'wison7', 'pbkdf2:sha256:50000$4mrb5Asb$7a57e78582b2c8c2e0bb1c44aaf7eff9872c8d8b6b81395844415124061116c9', 'wison', '', '', '2019-03-14 14:32:48', '2019-03-15 13:47:46', '1552628866');
INSERT INTO `admin_users` VALUES ('11', 'wison8', 'pbkdf2:sha256:50000$4mrb5Asb$7a57e78582b2c8c2e0bb1c44aaf7eff9872c8d8b6b81395844415124061116c9', 'wison', '', '', '2019-03-14 14:32:48', '2019-03-15 13:47:46', '1552628866');
INSERT INTO `admin_users` VALUES ('12', 'wison9', 'pbkdf2:sha256:50000$4mrb5Asb$7a57e78582b2c8c2e0bb1c44aaf7eff9872c8d8b6b81395844415124061116c9', 'wison', '', '', '2019-03-14 14:32:48', '2019-03-15 13:47:46', '1552628866');
INSERT INTO `admin_users` VALUES ('13', 'wison10', 'pbkdf2:sha256:50000$4mrb5Asb$7a57e78582b2c8c2e0bb1c44aaf7eff9872c8d8b6b81395844415124061116c9', 'wison', '', '', '2019-03-14 14:32:48', '2019-03-15 13:47:46', '1552628866');
INSERT INTO `admin_users` VALUES ('14', 'wison11', 'pbkdf2:sha256:50000$4mrb5Asb$7a57e78582b2c8c2e0bb1c44aaf7eff9872c8d8b6b81395844415124061116c9', 'wison', '', '', '2019-03-14 14:32:48', '2019-03-15 13:47:46', '1552628866');
INSERT INTO `admin_users` VALUES ('15', 'wison12', 'pbkdf2:sha256:50000$4mrb5Asb$7a57e78582b2c8c2e0bb1c44aaf7eff9872c8d8b6b81395844415124061116c9', 'wison', '', '', '2019-03-14 14:32:48', '2019-03-15 13:47:46', '1552628866');
INSERT INTO `admin_users` VALUES ('16', 'wison13', 'pbkdf2:sha256:50000$4mrb5Asb$7a57e78582b2c8c2e0bb1c44aaf7eff9872c8d8b6b81395844415124061116c9', 'wison', '', '', '2019-03-14 14:32:48', '2019-03-15 13:47:46', '1552628866');
INSERT INTO `admin_users` VALUES ('17', 'wison14', 'pbkdf2:sha256:50000$4mrb5Asb$7a57e78582b2c8c2e0bb1c44aaf7eff9872c8d8b6b81395844415124061116c9', 'wison', '', '', '2019-03-14 14:32:48', '2019-03-15 13:47:46', '1552628866');
INSERT INTO `admin_users` VALUES ('18', 'wison15', 'pbkdf2:sha256:50000$4mrb5Asb$7a57e78582b2c8c2e0bb1c44aaf7eff9872c8d8b6b81395844415124061116c9', 'wison', '', '', '2019-03-14 14:32:48', '2019-03-15 13:47:46', '1552628866');
INSERT INTO `admin_users` VALUES ('19', 'wison16', 'pbkdf2:sha256:50000$4mrb5Asb$7a57e78582b2c8c2e0bb1c44aaf7eff9872c8d8b6b81395844415124061116c9', 'wison', '', '', '2019-03-14 14:32:48', '2019-03-15 13:47:46', '1552628866');
INSERT INTO `admin_users` VALUES ('20', 'wison17', 'pbkdf2:sha256:50000$4mrb5Asb$7a57e78582b2c8c2e0bb1c44aaf7eff9872c8d8b6b81395844415124061116c9', 'wison', '', '', '2019-03-14 14:32:48', '2019-03-15 13:47:46', '1552628866');
INSERT INTO `admin_users` VALUES ('21', 'wison18', 'pbkdf2:sha256:50000$4mrb5Asb$7a57e78582b2c8c2e0bb1c44aaf7eff9872c8d8b6b81395844415124061116c9', 'wison', '', '', '2019-03-14 14:32:48', '2019-03-15 13:47:46', '1552628866');
INSERT INTO `admin_users` VALUES ('22', 'wison19', 'pbkdf2:sha256:50000$4mrb5Asb$7a57e78582b2c8c2e0bb1c44aaf7eff9872c8d8b6b81395844415124061116c9', 'wison', '', '', '2019-03-14 14:32:48', '2019-03-15 13:47:46', '1552628866');
INSERT INTO `admin_users` VALUES ('23', 'wison20', 'pbkdf2:sha256:50000$4mrb5Asb$7a57e78582b2c8c2e0bb1c44aaf7eff9872c8d8b6b81395844415124061116c9', 'wison', '', '', '2019-03-14 14:32:48', '2019-03-15 13:47:46', '1552628866');
INSERT INTO `admin_users` VALUES ('24', 'wison21', 'pbkdf2:sha256:50000$4mrb5Asb$7a57e78582b2c8c2e0bb1c44aaf7eff9872c8d8b6b81395844415124061116c9', 'wison', '', '', '2019-03-15 15:32:48', '2019-03-15 15:04:24', '1552628866');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `tel` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `password` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `status` tinyint(1) NOT NULL,
  `remember_token` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `url_path` varchar(300) COLLATE utf8_unicode_ci DEFAULT NULL,
  `real_path` varchar(300) COLLATE utf8_unicode_ci DEFAULT NULL,
  `login_time` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_email_unique` (`email`),
  UNIQUE KEY `users_tel_unique` (`tel`),
  UNIQUE KEY `users_name_unique` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=34 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of users
-- ----------------------------
