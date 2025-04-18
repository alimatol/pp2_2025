'''
CREATE OR REPLACE PROCEDURE insert_new(
	new_name VARCHAR,
	new_number VARCHAR
)
AS $$
BEGIN 
    IF EXISTS (SELECT 1 FROM phonebook WHERE user_name = new_name) THEN
        UPDATE phonebook
        SET phone_number = new_number
        WHERE user_name = new_name;
    ELSE
        INSERT INTO phonebook(user_name, phone_number)
        VALUES(new_name, new_number);
    END IF;

END;
$$
LANGUAGE PLPGSQL;
'''

'''
CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(user_id INTEGER, user_name VARCHAR, phone_number VARCHAR) AS
$$
BEGIN
    RETURN QUERY
    SELECT p.user_id, p.user_name, p.phone_number
    FROM phonebook AS p
    WHERE p.user_name ILIKE '%' || pattern || '%'
       OR p.phone_number ILIKE '%' || pattern || '%';
END;
$$
LANGUAGE plpgsql;
'''

#5


"""
CREATE OR REPLACE PROCEDURE delete_user(
	username VARCHAR)
AS $$
BEGIN 
    IF username IS NOT NULL THEN 
        DELETE FROM phonebook
        WHERE user_name = username;
    END IF;

END;
$$
LANGUAGE PLPGSQL;
"""

"""
CREATE OR REPLACE FUNCTION query_phonebook(
    limit_1 INT, 
    offset_1 INT
)
RETURNS TABLE(user_id INT, user_name VARCHAR, phone_number VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT p.user_id, p.user_name, p.phone_number
    FROM phonebook p
    LIMIT limit_1 OFFSET offset_1;
END;
$$ LANGUAGE plpgsql;


"""