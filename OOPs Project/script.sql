DROP TABLE IF EXISTS role;
CREATE TABLE role (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
INSERT INTO role VALUES (1,'Store Manager'),(2,'Product Lead'),(3,'Sales Lead'),(4,'Customer');


DROP TABLE IF EXISTS user;
CREATE TABLE user (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(45) DEFAULT NULL,
  username varchar(45) DEFAULT NULL,
  password varchar(45) DEFAULT NULL,
  mobile_number varchar(45) DEFAULT NULL,
  email varchar(45) DEFAULT NULL,
  address varchar(45) DEFAULT NULL,
  role_id int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`role_id`) REFERENCES role (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
);
INSERT INTO user VALUES (1,'Sridevi Harish','srideviharish','srid','8074564565','sri@gmail.com','Kasaragod, India',1),(2,'Vidya','vidya','vidya','9635263215','vidya@yahoo.in','Mangalore, Karnataka',4),(3,'Sai Teja','saitez','saitez','7456963256','saiteja@gmail.com','Andra Pradesh',2),(4,'Aswin Krishna','akrishna','akrishna','9659653232','akrishna@gmail.com','Trissur, India',3),(5,'Lava Gowda','lava','lava','9654563212','lava@gmail.com','Kalasa',3),(6,'Rani','rani','rani','7458659825','rani@gmail.com','Ckm',4),(7,'Ajay Vivek','ajai','abcd123','4563258963','avivek@yahoo.in','Puttur',4);


DROP TABLE IF EXISTS brand;
CREATE TABLE brand (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ;
INSERT INTO brand VALUES (1,'Apple'),(2,'Samsung'),(3,'SkyBag'),(4,'Adidas'),(5,'Nike'),(6,'American Tourister'),(7,'Lotus'),(8,'Nivea');


DROP TABLE IF EXISTS product_category;
CREATE TABLE product_category (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(45) DEFAULT NULL,
  description varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
INSERT INTO product_category VALUES (1,'Electronics','Electronics'),(2,'Fashion','Fashion'),(3,'Footware','Footwares'),(4,'Home and Furniture','Home and Furniturs');


DROP TABLE IF EXISTS product_type;
CREATE TABLE product_type (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(45) DEFAULT NULL,
  description varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
INSERT INTO product_type VALUES (1,'Smartphone','Mobile'),(2,'Tablet','Tablets and accessories'),(3,'Bagpack','Bagpack'),(4,'Shoe','Shoe'),(5,'Toys','Toys'),(6,'Jewellery','Jewelleries');


DROP TABLE IF EXISTS product;
CREATE TABLE product (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(45) NOT NULL,
  brand_id int(11) NOT NULL,
  color varchar(45) NOT NULL,
  material varchar(45) NOT NULL,
  price decimal(10,0) NOT NULL,
  active int(11) DEFAULT NULL,
  quantity int(11) DEFAULT NULL,
  product_type_id int(11) NOT NULL,
  product_category_id int(11) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`brand_id`) REFERENCES brand (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  FOREIGN KEY (`product_category_id`) REFERENCES product_category (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  FOREIGN KEY (`product_type_id`) REFERENCES product_type (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
);
INSERT INTO product VALUES (1,'iPhone 11 Pro',1,'Midnight green','Aluminium',99900,_binary '1',4,1,1),(2,'iPhone 7 Plus',1,'Gold','Aluminium',35000,_binary '1',4,1,1),(3,'Skybag New Edition',3,'Blue','Waterproof fabrics',2429,_binary '1',12,3,2),(4,'Running shoe',4,'Blue','EVA',2999,_binary '0',4,4,3);


DROP TABLE IF EXISTS supplier;
CREATE TABLE supplier (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(45) DEFAULT NULL,
  mobile_number varchar(45) DEFAULT NULL,
  email varchar(45) DEFAULT NULL,
  address varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
INSERT INTO supplier VALUES (1,'Nivin','80745674565','nivin@gmail.com','India'),(2,'Sristi','9632123652','sristi@gmail.com','Mangalore, India'),(3,'Aswin','7894569856','aswin@gmail.com','Trissur, Kerala'),(4,'Tej','7458547485','tej@gmail.com','Andra Pradesh');


DROP TABLE IF EXISTS purchase_order;
CREATE TABLE purchase_order (
  id int(11) NOT NULL AUTO_INCREMENT,
  supplier_id int(11) DEFAULT NULL,
  quantity int(11) DEFAULT NULL,
  total_price decimal(10,0) DEFAULT NULL,
  tax_amount decimal(10,0) DEFAULT NULL,
  product_lead_id int(11) DEFAULT NULL,
  purchased_date date DEFAULT NULL,
  item_list_id int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY item_list_id_UNIQUE (`item_list_id`),
  FOREIGN KEY (`product_lead_id`) REFERENCES user (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  FOREIGN KEY (`supplier_id`) REFERENCES supplier (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
);
INSERT INTO purchase_order VALUES (2,1,1,117882,17982,3,'2020-02-02',NULL),(3,4,2,165200,25200,3,'2020-02-02',NULL),(4,3,1,51703,7557,3,'2020-12-04',NULL),(5,1,1,117882,17982,3,'2020-10-04',NULL);


DROP TABLE IF EXISTS purchase_order_item;
CREATE TABLE purchase_order_item (
  id int(11) NOT NULL AUTO_INCREMENT,
  product_id int(11) DEFAULT NULL,
  quantity int(11) DEFAULT NULL,
  unit_price decimal(10,0) DEFAULT NULL,
  purchase_order_id int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`purchase_order_id`) REFERENCES purchase_order (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  FOREIGN KEY (`product_id`) REFERENCES product (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
);
INSERT INTO purchase_order_item VALUES (1,1,1,99900,5),(2,2,2,35000,3),(3,3,6,2999,4),(4,4,10,2999,4);


DROP TABLE IF EXISTS sales_order;
CREATE TABLE sales_order (
  id int(11) NOT NULL AUTO_INCREMENT,
  customer_id int(11) NOT NULL,
  quantity int(11) DEFAULT NULL,
  total_price decimal(10,0) DEFAULT NULL,
  tax_amount decimal(10,0) DEFAULT NULL,
  sales_lead_id int(11) DEFAULT NULL,
  sale_date date DEFAULT NULL,
  item_list_id int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY item_list_id_UNIQUE (`item_list_id`),
  FOREIGN KEY (`customer_id`) REFERENCES user (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  FOREIGN KEY (`sales_lead_id`) REFERENCES user (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
);
INSERT INTO sales_order VALUES (1,2,1,235764,35964,4,'2020-02-02',NULL),(2,6,2,320951,48959,4,'2020-09-06',NULL),(3,7,2,261176,35996,5,'2020-05-04',NULL);


DROP TABLE IF EXISTS sales_order_item;
CREATE TABLE sales_order_item (
  id int(11) NOT NULL,
  product_id int(11) NOT NULL,
  quantity int(11) NOT NULL,
  unit_price decimal(10,0) NOT NULL,
  sales_order_id int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`product_id`) REFERENCES product (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  FOREIGN KEY (`sales_order_id`) REFERENCES sales_order (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
);
INSERT INTO sales_order_item VALUES (1,1,2,99900,1),(2,2,4,33999,2),(3,3,2,35000,3),(4,4,10,2999,2);


