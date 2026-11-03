-- Populate Dimension Tables
INSERT INTO DimDate (DateKey, FullDate, Month, Quarter, Year) VALUES
(20231115, '2023-11-15', 11, 4, 2023),
(20231116, '2023-11-16', 11, 4, 2023);

INSERT INTO DimCustomer (CustomerKey, CustomerID, CustomerName, City, State) VALUES
(1,'CUST-001', 'John Smith', 'Seattle', 'WA'),
(2,'CUST-002', 'Jane Doe', 'Portland', 'OR');

INSERT INTO DimProduct (ProductKey,ProductID, ProductName, Category) VALUES
(1,'PROD-A1', 'Laptop Pro', 'Electronics'),
(2,'PROD-B2', 'Wireless Mouse', 'Accessories');

INSERT INTO DimChannel (ChannelKey,ChannelName) VALUES
(1,'Online'),
(2,'In-Store');

INSERT INTO DimStore (StoreKey,StoreID, StoreName, Region) VALUES
(1,'STORE-SEA', 'Seattle Downtown', 'West'),
(2,'STORE-POR', 'Portland Central', 'West');

-- Populate Fact Table
-- Note: The keys (1, 2) correspond to the rows created above
INSERT INTO FactSales (SalesKey,DateKey, CustomerKey, ProductKey, ChannelKey, StoreKey, OrderQuantity, UnitPrice, TotalAmount, DiscountAmount) VALUES
(1,20231115, 1, 1, 1, 1, 1, 1200.00, 1200.00, 0.00),     -- John buys a Laptop online from Seattle store
(2,20231115, 1, 2, 1, 1, 1, 25.00, 25.00, 5.00),      -- John also buys a Mouse online from Seattle store
(3,20231116, 2, 1, 2, 2, 1, 1150.00, 1150.00, 50.00);   -- Jane buys a Laptop in-store in Portland