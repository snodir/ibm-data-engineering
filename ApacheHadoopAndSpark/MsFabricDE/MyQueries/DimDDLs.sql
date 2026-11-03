-- dbo.Dimension: dbo.DimDate
CREATE TABLE dbo.DimDate (
    DateKey INT NOT NULL,
    FullDate DATE,
    Day INT,
    Month INT,
    Quarter INT,
    Year INT
);
 
-- dbo.Dimension: dbo.DimCustomer
CREATE TABLE dbo.DimCustomer (
    CustomerKey INT NOT NULL,
    CustomerID VARCHAR(50),
    CustomerName VARCHAR(100),
    City VARCHAR(50),
    State VARCHAR(50)
);
 
-- dbo.Dimension: dbo.DimProduct
CREATE TABLE dbo.DimProduct (
    ProductKey INT  NOT NULL,
    ProductID VARCHAR(50),
    ProductName VARCHAR(100),
    Category VARCHAR(50)
);
 
-- dbo.Dimension: dbo.DimChannel
CREATE TABLE dbo.DimChannel (
    ChannelKey INT  NOT NULL,
    ChannelName VARCHAR(50)
);
 
-- dbo.Dimension: dbo.DimStore
CREATE TABLE dbo.DimStore (
    StoreKey INT NOT NULL,
    StoreID VARCHAR(50),
    StoreName VARCHAR(100),
    Region VARCHAR(50)
);