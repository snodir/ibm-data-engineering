-- Create a dimension table for products
CREATE TABLE dbo.Distr_DimProduct (
    ProductID INT,
    ProductName VARCHAR(100),
    Category VARCHAR(50)
);

-- Create a large fact table for sales
CREATE TABLE dbo.Distr_FactSales (
    SalesID BIGINT ,
    ProductID INT,
    CustomerID INT,
    SaleAmount DECIMAL(10, 2),
    OrderDate DATE
);

-- Insert sample data into the product table
INSERT INTO dbo.Distr_DimProduct (ProductID, ProductName, Category) VALUES
(101, 'Laptop Pro', 'Electronics'),
(102, 'Gaming Mouse', 'Electronics'),
(201, 'Office Chair', 'Furniture');

WITH NumberSeries AS (
  SELECT TOP 1000 ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
  FROM (VALUES (0),(1),(2),(3),(4),(5),(6),(7),(8),(9)) AS a(n)
       CROSS JOIN (VALUES (0),(1),(2),(3),(4),(5),(6),(7),(8),(9)) AS b(n)
       CROSS JOIN (VALUES (0),(1),(2),(3),(4),(5),(6),(7),(8),(9)) AS c(n)
)
INSERT INTO dbo.Distr_FactSales (ProductID, CustomerID, SaleAmount, OrderDate)
SELECT
    p.ProductID,
    ABS(CHECKSUM(NEWID())) % 1000 + 1 AS CustomerID,
    (ABS(CHECKSUM(NEWID())) % 5000 + 50) AS SaleAmount,
    DATEADD(day, - (ABS(CHECKSUM(NEWID())) % 365), GETDATE()) AS OrderDate
FROM dbo.Distr_DimProduct p
JOIN NumberSeries ns ON 1 = 1;