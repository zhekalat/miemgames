-- MySQL dump 10.13  Distrib 5.6.28, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: miemgame
-- ------------------------------------------------------
-- Server version	5.6.28-0ubuntu0.15.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `events` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `game` int(11) NOT NULL DEFAULT '0',
  `time` datetime NOT NULL,
  `place` tinytext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE (`game`, `time`, `place`(10)),
  CONSTRAINT `events_ibfk_1` FOREIGN KEY (`game`) REFERENCES `games` (`id`)
) ENGINE=InnoDB DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
/*!40000 ALTER TABLE `events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `games`
--

DROP TABLE IF EXISTS `games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `games` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` text,
  `name` tinytext NOT NULL,
  `min_players` int(11) NOT NULL,
  `max_players` int(11) NOT NULL,
  `picture` text NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE (`description`(10), `name`(10), `min_players`, `max_players`, `picture`)
) ENGINE=InnoDB DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games`
--

LOCK TABLES `games` WRITE;
/*!40000 ALTER TABLE `games` DISABLE KEYS */;
insert into games (name, description, min_players, max_players) values
('Мафия','Психологическая игра для 4-20 участников. Задача игроков — тщательно анализировать слова и поведение других игроков и добиться выполнения своей игровой задачи. Цель мирных жителей — искоренение преступной группировки, цель мафии — захват власти в городе.', 4, 20, 'http://scottystarnes.files.wordpress.com/2013/01/mafia-game-salieri-mobsters-1920x1440.jpg'),
('Манчкин','Вот она — колода для реальных бойцов, суровых чистильщиков подземелий. Пафосные речи? Отыгрыш персонажа? Внутренняя логика мира? Кому ты паришь мозги! Мы-то с тобой знаем, зачем нормальные люди приходят в РПГ — мы приходим прокачивать уровень, мочить монстров и доказывать, что мы здесь круче. Мы — манчкины, и это наша колода.', 3, 10, 'http://hobbygames.ru/image/data/HobbyWorld/Munchkin/igra_manchkin.jpg'),
('Имаджинариум','Настольная игра, в которой надо самому придумывать ассоциации к картинкам и пытаться разгадать чужие ассоциации. Суть игры в том, чтобы как точнее предположить ход мысли других игроков.', 4, 7, 'http://s5.cdnproductmain.mosigra.ru/511/664/imadjinarium_1500x1500.jpg'),
('Игросказ','Исследователь по имени Пропп перебрал сотни и тысячи сюжетов сказок разных народов мира, изучил эпос и мифологию — и пришел к выводу, что каждая выдуманная история строится на нескольких одинаковых ключевых событиях, к примеру, нарушении какого-либо запрета, появлении таинственного дарителя или же соперничестве с противником главного героя. Он выпустил набор из почти четырёх десятков так называемых карт Проппа, каждая из которых показывала одну из подобных «узловых точек». Можно было открывать их одну за одной и придумывать свою историю, а можно было просто искать их в любой прочитанной или услышанной.', 2, 12, 'http://igrology.ru/uploads/game/picture/3/image.jpg'),
('Элиас','Динамичная игра для компании от 4 до 16 человек. Задача игрока — объяснить слово-задание товарищам по команде, не называя его или однокоренных слов, а цель товарищей — как можно быстрее отгадать задание.', 4, 16, 'http://www.igroparty.ru/assets/products/119/large/_.jpg?1274953981'),
('Активити','Командная игра для компаний от 4 до 16 человек. За минуту игроку надо объяснить своему товарищу по команде до 3х слов, и каждое из них можно объяснять только одним способом: жестами, рисунком или словами (без однокоренных форм).', 4, 16, 'http://irecommend.ru/sites/default/files/product-images/92563/nastolnaya_igra_aktiviti-2___activity-2.jpg'),
('Magic: The Gathering','Magic: The Gathering — это стратегическая игра для двух или более игроков, каждый из которых обладает колодой карт Magic, собранной по собственному усмотрению. В ходе партии игроки по очереди разыгрывают различные карты: земли (позволяющие разыгрывать остальные карты), существа, волшебства и другие заклинания. В начале игры у каждого игрока есть 20 жизней. Тот, кто сократит количество жизней оппонента до нуля, атакуя его с помощью существ и разыгрывая заклинания, одерживает победу!', 2, 64, 'http://game-online.shop.by/pics/items/4158.jpg'),
('Гномы-вредители','На первый взгляд, все гномы похожи: маленькие, бородатые, золото любят, упорно стучат своими кирками в подземных туннелях в поисках золотой жилы. Но не случайно же обрушился туннель, кто-то явно намеренно разбил лампу, подстроил ловушку, сломал инструменты. В шахте появились гномы-вредители!  Игроки будут добывать золото в нелегкой борьбе в течение трех раундов, и всякий раз роли гномов будут распределяться заново, так что вредителем сможет побывать каждый золотоискатель. ', 2, 12, 'http://jengames.ru/upload/iblock/76b/76b8eddafe5e1af8483883d0a9135065.jpg'),
('Дженга','Игра на точность движений и хладнокровие игрока. Суть в том, что надо сделать выше башню из деревянных брусочков. Достроить её нужно теми «кирпичиками», которые вытащишь из любого этажа, кроме самого верхнего.', 1, 4, 'http://www.korablik.ru/upload/catalog/13801/13801_1000.jpg'),
('Экивоки','Игра для больших и маленьких компаний, в которую можно играть командами или поодиночке. Суть игры в объяснении слов разными способами: синонимами, задом-наперед, песней, пантомимой, рисунком и при помощи вопросов на «да» и «нет». Отгадать задание надо за 1 минуту.', 4, 16, 'http://www.smartytoys.ru/images/store/3480_2.jpg'),
('Каркассон',' В этой игре вам предстоит составлять карту средневекового княжества из квадратов с нарисованными на них дорогами, полями и монастырями. Именно туда вы будете отправлять своих подданных, чтобы впоследствии получить за них победные очки. Вашему неустанному труду мешают лишь ваши соперники, столь же знатные и могучие, как и вы. Но трон правителя Лангедока в Каркассоне не делится на пятерых, лишь один победитель в этой борьбе!', 2, 5, 'http://nastolki-spb.ru/sites/default/files/styles/large/public/uploads/1953/karkasson-front.png'),
('Монополия','Экономическая игра, основанная на рыночной модели крупных финансовых структур. Игрокам необходимо правильно распределить ресурсы, предусмотреть возможные действия противников и форс-мажорные обстоятельства.', 2, 8, 'http://wonderlavka.ru/files/items/item_image_27.jpg'),
('Уно','Классическая игра с карточками на внимание, реакцию и тактическое мышление. Подходит для компаний от 2 до 10 человек.', 2, 10, 'http://bratsk-game.ru/wp-content/uploads/2013/08/uno.jpg');
/*!40000 ALTER TABLE `games` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `participants`
--

DROP TABLE IF EXISTS `participants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `participants` (
  `event` int(11) NOT NULL DEFAULT '0',
  `player` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`player`,`event`),
  KEY `event` (`event`),
  CONSTRAINT `participants_ibfk_1` FOREIGN KEY (`event`) REFERENCES `events` (`id`),
  CONSTRAINT `participants_ibfk_2` FOREIGN KEY (`player`) REFERENCES `players` (`id`)
) ENGINE=InnoDB DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `participants`
--

LOCK TABLES `participants` WRITE;
/*!40000 ALTER TABLE `participants` DISABLE KEYS */;
/*!40000 ALTER TABLE `participants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `players` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` tinytext NOT NULL,
  `num_group` char(6) DEFAULT NULL,
  `rating` int(11) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY (`name`(10), `num_group`)
) ENGINE=InnoDB DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `players`
--

LOCK TABLES `players` WRITE;
/*!40000 ALTER TABLE `players` DISABLE KEYS */;
/*!40000 ALTER TABLE `players` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-02-23 10:21:01
