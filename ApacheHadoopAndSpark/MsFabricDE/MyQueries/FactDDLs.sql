-- SQL to Create Fact Table
 
CREATE TABLE dbo.FactSales (
    SalesKey INT NOT NULL,
    DateKey INT,
    CustomerKey INT,
    ProductKey INT,
    ChannelKey INT,
    StoreKey INT,
    OrderQuantity INT,
    UnitPrice DECIMAL(10, 2),
    TotalAmount DECIMAL(10, 2),
    DiscountAmount DECIMAL(10, 2)
);