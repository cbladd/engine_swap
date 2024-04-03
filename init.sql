CREATE TABLE parts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    compatible_with VARCHAR(255) NOT NULL
);

INSERT INTO parts (name, category, compatible_with) VALUES
('Subaru EJ22 Engine', 'engine', 'VW Vanagon'),
('Engine Conversion Kit', 'conversion kit', 'VW Vanagon'),
('High Performance Exhaust', 'exhaust', 'Subaru EJ22'),
('Transmission Adapter Plate', 'transmission', 'VW Vanagon'),
('Upgraded Cooling System', 'cooling', 'Subaru EJ22');
