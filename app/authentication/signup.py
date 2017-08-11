DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
    IN p_first_name VARCHAR(20),  
    IN p_last_name VARCHAR(20),
    IN p_email VARCHAR(20),
    IN p_username VARCHAR(20),
    IN p_password VARCHAR(20)
)
BEGIN
    if ( select exists (select 1 from user where username = p_username) ) THEN
     
        select 'Username Exists !!';
     
    ELSE
     
        insert into tbl_user
        (
           first_name,
           last_name,
           email,
           username
           password
        )
        values
        (   
            p_first_name,
            p_last_name,
            p_email,
            p_username
            p_password
        );
     
    END IF;
END$$
DELIMITER ;
