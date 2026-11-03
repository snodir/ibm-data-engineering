-- In Fabric Data Warehouse, a clustered columnstore index is created by default for new tables, which is ideal for fact tables.

ALTER TABLE dbo.DimProduct
ADD CONSTRAINT PK_DimProduct
 PRIMARY KEY NONCLUSTERED (ProductKey) NOT ENFORCED;

ALTER TABLE dbo.DimCustomer
ADD CONSTRAINT PK_DimCustomer
 PRIMARY KEY NONCLUSTERED (CustomerKey) NOT ENFORCED;

ALTER TABLE dbo.DimDate
ADD CONSTRAINT PK_DimDate
 PRIMARY KEY NONCLUSTERED (DateKey) NOT ENFORCED;

ALTER TABLE dbo.DimChannel
ADD CONSTRAINT PK_DimChannel
 PRIMARY KEY NONCLUSTERED (ChannelKey) NOT ENFORCED;

ALTER TABLE dbo.DimStore
ADD CONSTRAINT PK_DimStore
 PRIMARY KEY NONCLUSTERED (StoreKey) NOT ENFORCED;