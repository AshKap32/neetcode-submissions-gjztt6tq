-- Write your query below

-- can left join on customer id keeping everything on the orders table 
-- keeping everything on the orders table will 
SELECT c.customer_id, c.customer_name
FROM customers AS c
WHERE c.customer_id IN (
    SELECT customer_id FROM orders WHERE product_name = 'A'
    )
    AND c.customer_id IN (
    SELECT customer_id FROM orders WHERE product_name = 'B'
    )
    AND c.customer_id NOT IN (
    SELECT customer_id FROM orders WHERE product_name = 'C'
    )
ORDER BY c.customer_name;