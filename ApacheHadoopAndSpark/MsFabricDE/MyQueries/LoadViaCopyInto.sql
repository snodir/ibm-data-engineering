CREATE TABLE dbo.DimProductLH (
    ProductKey INT NOT NULL , -- Surrogate Key
    ProductSourceID INT, -- Business Key from the source system
    ProductName VARCHAR(100),
    Category VARCHAR(50)
);

-- dbo.Dimension: dbo.DimCustomer
CREATE TABLE dbo.DimCustomerLH (
    CustomerKey INT NOT NULL,
    CustomerSourceID VARCHAR(10),
    CustomerName VARCHAR(100),
    Country VARCHAR(50)
);

CREATE TABLE dbo.FactSalesLH (
    SalesKey INT NOT NULL ,
    ProductKey INT,
    CustomerKey INT , 
    OrderDate DATE,
    UnitsSold INT,
    Revenue DECIMAL(10, 2)
);

COPY INTO dbo.DimProductLH (ProductKey, ProductSourceID, ProductName, Category)
FROM 'abfss://e081e939-4eec-4c69-b527-cecd7f097f8f@onelake.dfs.fabric.microsoft.com/3398cff3-da5b-429c-989e-cb8a0166e496/Files/demo/product_data.csv'
WITH (
    FILE_TYPE = 'CSV',
    FIRSTROW = 2 -- Skips the header row in the CSV file
);

COPY INTO dbo.DimCustomerLH (CustomerKey, CustomerSourceID, CustomerName, Country)
FROM 'https://onelake.dfs.fabric.microsoft.com/e081e939-4eec-4c69-b527-cecd7f097f8f/3398cff3-da5b-429c-989e-cb8a0166e496/Files/demo/customer_data.csv'
WITH (
    FILE_TYPE = 'CSV',
    FIRSTROW = 2 -- Skips the header row in the CSV file
);

COPY INTO dbo.FactSalesLH (SalesKey,
    ProductKey,
    CustomerKey, 
    OrderDate,
    UnitsSold,
    Revenue)
FROM 'abfss://e081e939-4eec-4c69-b527-cecd7f097f8f@onelake.dfs.fabric.microsoft.com/3398cff3-da5b-429c-989e-cb8a0166e496/Files/demo/sales_data.csv'
WITH (
    FILE_TYPE = 'CSV',
    FIRSTROW = 2 -- Skips the header row in the CSV file
);