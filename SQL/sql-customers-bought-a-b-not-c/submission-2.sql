-- Write your query below
SELECT customer_id, customer_name
FROM customers
WHERE customer_id IN (
        SELECT o.customer_id FROM orders AS o WHERE product_name = 'A'
    ) 
    AND customer_id IN (
        SELECT o.customer_id FROM orders AS o WHERE product_name = 'B'
    ) 
    AND customer_id NOT IN (
        SELECT o.customer_id FROM orders AS o WHERE product_name = 'C'
    )
ORDER BY customer_name;
