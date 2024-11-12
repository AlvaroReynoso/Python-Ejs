INSERT INTO paciente (nombre, telefono, email, fecha_nac) VALUES
('Victoria Oconnor', '(934)946-8567x442', 'tammy51@example.net', '1956-01-03'),
('James Bond', '960-566-9728x34539', 'mlawrence@example.com', '1981-12-31'),
('Emily Fox', '001-377-681-0167x297', 'sgomez@example.org', '1940-06-14'),
('Tyler Joyce', '(502)461-2635', 'jacobsingleton@example.net', '1983-12-19'),
('Janet Garza', '+1-498-874-6282', 'jonespeter@example.net', '1976-08-31'),
('Sarah Nguyen', '968.629.2294', 'joshua64@example.net', '1974-11-15'),
('John Robinson', '3785322246', 'richard86@example.net', '1936-11-09'),
('Douglas Gray', '(208)956-4385x53736', 'laura97@example.org', '1955-07-13'),
('Bryan Gonzalez', '(994)877-9222x49418', 'harrisrichard@example.com', '1981-06-05'),
('David Decker', '7382131072', 'haileywatson@example.com', '1992-01-08');
INSERT INTO doctor (nombre, telefono, email, fecha_nac, especialidad) VALUES
('Christopher Becker', '(713)278-8021', 'zknight@example.com', '1964-06-10', 'Dermatolog�a'),
('Erik Moss', '+1-361-203-8195x66155', 'yvelasquez@example.net', '1973-04-04', 'Gastroenterolog�a'),
('Jerry Roman', '8053301993', 'nthomas@example.com', '1980-01-07', 'Pediatr�a'),
('Christopher Walton', '001-293-829-1919x7919', 'qflores@example.org', '1995-12-24', 'Pediatr�a'),
('Tyler Hall', '001-539-233-8339x256', 'erin80@example.org', '1990-07-26', 'Neurolog�a');
INSERT INTO cita (fecha_cita, id_doctor, id_paciente) VALUES
('2024-04-08 08:58:47', 5, 8),
('2024-06-13 09:21:02', 1, 3),
('2024-01-18 23:18:04', 2, 3),
('2024-06-04 00:42:45', 4, 8),
('2024-03-26 08:48:34', 3, 1),
('2024-08-16 14:50:32', 5, 4),
('2024-07-07 15:01:44', 5, 10),
('2024-07-31 00:54:48', 5, 3),
('2024-09-07 19:52:19', 1, 2),
('2024-02-25 13:32:42', 2, 8),
('2024-04-04 23:47:01', 3, 9),
('2024-06-19 13:51:34', 5, 10),
('2024-02-17 21:38:53', 3, 9),
('2024-07-13 21:24:11', 5, 6),
('2024-07-28 06:09:14', 4, 8),
('2024-04-14 00:28:28', 5, 1),
('2024-08-02 16:01:29', 2, 3),
('2024-08-18 13:33:07', 5, 3),
('2024-03-23 05:27:52', 4, 1),
('2024-02-07 01:01:52', 5, 1);
INSERT INTO diagnostico (nombre, id_doctor, id_paciente, id_cita) VALUES
('Fractura', 4, 4, 7),
('Migra�a', 5, 1, 11),
('Migra�a', 5, 2, 2),
('Infecci�n Respiratoria', 5, 5, 15),
('Migra�a', 2, 8, 1),
('Infecci�n Respiratoria', 4, 4, 2),
('Fractura', 4, 1, 9),
('Infecci�n Respiratoria', 3, 9, 9),
('Infecci�n Respiratoria', 1, 2, 4),
('Migra�a', 2, 4, 10),
('Gastritis', 4, 7, 12),
('Fractura', 3, 7, 14),
('Fractura', 4, 8, 9),
('Infecci�n Respiratoria', 5, 6, 3),
('Infecci�n Respiratoria', 5, 1, 2);
INSERT INTO tratamiento (descripcion, id_diagnostico) VALUES
('Antibi�ticos', 3),
('Fisioterapia', 10),
('Reposo', 14),
('Dieta Especial', 1),
('Cirug�a', 2),
('Dieta Especial', 7),
('Fisioterapia', 10),
('Dieta Especial', 14),
('Fisioterapia', 9),
('Reposo', 5);