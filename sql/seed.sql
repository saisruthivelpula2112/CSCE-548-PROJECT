-- USERS (10 rows)
INSERT INTO users (username, email, role) VALUES
('user1','user1@uni.edu','student'),
('user2','user2@uni.edu','student'),
('user3','user3@uni.edu','student'),
('user4','user4@uni.edu','student'),
('user5','user5@uni.edu','student'),
('user6','user6@uni.edu','student'),
('user7','user7@uni.edu','student'),
('user8','user8@uni.edu','student'),
('user9','user9@uni.edu','student'),
('user10','user10@uni.edu','student');

-- PROJECTS (10 rows)
INSERT INTO projects (owner_id, title) VALUES
(1,'Project A'),
(2,'Project B'),
(3,'Project C'),
(4,'Project D'),
(5,'Project E'),
(6,'Project F'),
(7,'Project G'),
(8,'Project H'),
(9,'Project I'),
(10,'Project J');

-- ITEMS (20 rows)
INSERT INTO items (project_id, name) VALUES
(1,'Item 1'),(1,'Item 2'),
(2,'Item 3'),(2,'Item 4'),
(3,'Item 5'),(3,'Item 6'),
(4,'Item 7'),(4,'Item 8'),
(5,'Item 9'),(5,'Item 10'),
(6,'Item 11'),(6,'Item 12'),
(7,'Item 13'),(7,'Item 14'),
(8,'Item 15'),(8,'Item 16'),
(9,'Item 17'),(9,'Item 18'),
(10,'Item 19'),(10,'Item 20');

-- TAGS (5 rows)
INSERT INTO tags (tag_name) VALUES
('database'),
('python'),
('backend'),
('frontend'),
('testing');

-- ITEM_TAGS (10 rows)
INSERT INTO item_tags (item_id, tag_id) VALUES
(1,1),(2,2),(3,3),(4,4),(5,5),
(6,1),(7,2),(8,3),(9,4),(10,5);
