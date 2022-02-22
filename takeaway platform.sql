/*
 Navicat Premium Data Transfer

 Source Server         : tyrant
 Source Server Type    : MySQL
 Source Server Version : 80027
 Source Host           : localhost:3306
 Source Schema         : takeaway platform

 Target Server Type    : MySQL
 Target Server Version : 80027
 File Encoding         : 65001

 Date: 22/02/2022 22:49:12
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for issue
-- ----------------------------
DROP TABLE IF EXISTS `issue`;
CREATE TABLE `issue`  (
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `price` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `describtion` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `img` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `accountname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of issue
-- ----------------------------
INSERT INTO `issue` VALUES ('胡桃', '648', 'tnnd为什么不吃', '\\static\\img\\wallhaven-72x259.jpg', 'shangjia');
INSERT INTO `issue` VALUES ('三玖', '1296', '三玖天下第一', '\\static\\img\\wallhaven-6kwrdx.png', 'shangjia');
INSERT INTO `issue` VALUES ('甘雨', '648', '黑色史莱姆', '\\static\\img\\wallhaven-y8xzod.jpg', 'shangjia');
INSERT INTO `issue` VALUES ('助手', '999', '太香啦', '\\static\\img\\wallhaven-od3r85.png', 'shangjia');
INSERT INTO `issue` VALUES ('剑来', '789654', 'tnnd为什么不吃', '\\static\\img\\QQ20220120145204.jpg', 'test');

-- ----------------------------
-- Table structure for member
-- ----------------------------
DROP TABLE IF EXISTS `member`;
CREATE TABLE `member`  (
  `accountname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of member
-- ----------------------------
INSERT INTO `member` VALUES ('894', '123', '2');
INSERT INTO `member` VALUES ('yonghu', '123', '0');
INSERT INTO `member` VALUES ('yonghu', '123', '0');
INSERT INTO `member` VALUES ('yonghu', '123', '0');
INSERT INTO `member` VALUES ('yonghu', '123', '0');
INSERT INTO `member` VALUES ('yonghu', '123', '0');
INSERT INTO `member` VALUES ('yonghu', '123', '0');
INSERT INTO `member` VALUES ('yonghu', '123', '0');
INSERT INTO `member` VALUES ('shangjia', '123', '1');
INSERT INTO `member` VALUES ('qishou', '123', '2');
INSERT INTO `member` VALUES ('test', '123', '1');

-- ----------------------------
-- Table structure for order_receiving
-- ----------------------------
DROP TABLE IF EXISTS `order_receiving`;
CREATE TABLE `order_receiving`  (
  `下单时间` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `下单人` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `住址` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `订单店铺` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `订单内容` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `订单状态` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `接单时间` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `送达时间` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `骑手` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of order_receiving
-- ----------------------------
INSERT INTO `order_receiving` VALUES ('2022/2/20 21:07', 'yonghu', 'xxxxx', '一家店', 'aa、bb、cc', '1', '2022/2/20 21:10', '2022/2/20 21:40', '213', '12345651');
INSERT INTO `order_receiving` VALUES ('2022/2/20 21：20', 'yonghu2', 'xxxxxx', '一家店', 'xxx', '0', '', '', '', '165165');

-- ----------------------------
-- Table structure for shop
-- ----------------------------
DROP TABLE IF EXISTS `shop`;
CREATE TABLE `shop`  (
  `shop_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `describtion` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `accountname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `img` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of shop
-- ----------------------------
INSERT INTO `shop` VALUES ('一家店', '0', 'tnnd为什么不吃', 'shangjia', '\\static\\img\\QQ20220120145157.jpg');
INSERT INTO `shop` VALUES ('儒家', '1', '我只有一剑，但可斩世间万物', 'test', '\\static\\img\\QQ20220120145207.jpg');

SET FOREIGN_KEY_CHECKS = 1;
