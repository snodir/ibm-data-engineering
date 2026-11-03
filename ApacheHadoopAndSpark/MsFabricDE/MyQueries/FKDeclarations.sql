ALTER TABLE dbo.FactSales
  ADD CONSTRAINT FK_FactSales_Product
  FOREIGN KEY (ProductKey)
  REFERENCES dbo.DimProduct(ProductKey)
  NOT ENFORCED;

ALTER TABLE dbo.FactSales
  ADD CONSTRAINT FK_FactSales_Date
  FOREIGN KEY (DateKey)
  REFERENCES dbo.DimDate(DateKey)
  NOT ENFORCED;

ALTER TABLE dbo.FactSales
  ADD CONSTRAINT FK_FactSales_Customer
  FOREIGN KEY (CustomerKey)
  REFERENCES dbo.DimCustomer(CustomerKey)
  NOT ENFORCED;

ALTER TABLE dbo.FactSales
  ADD CONSTRAINT FK_FactSales_Channel
  FOREIGN KEY (ChannelKey)
  REFERENCES dbo.DimChannel(ChannelKey)
  NOT ENFORCED;

ALTER TABLE dbo.FactSales
  ADD CONSTRAINT FK_FactSales_Store
  FOREIGN KEY (StoreKey)
  REFERENCES dbo.DimStore(StoreKey)
  NOT ENFORCED;

GO