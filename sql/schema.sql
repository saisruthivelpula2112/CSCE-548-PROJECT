CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    role VARCHAR(20) NOT NULL
);

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    owner_id INT NOT NULL,
    title VARCHAR(200),
    FOREIGN KEY (owner_id) REFERENCES users(user_id)
);

CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    project_id INT NOT NULL,
    name VARCHAR(200),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

CREATE TABLE tags (
    tag_id SERIAL PRIMARY KEY,
    tag_name VARCHAR(50)
);

CREATE TABLE item_tags (
    item_id INT,
    tag_id INT,
    PRIMARY KEY (item_id, tag_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id),
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id)
);
