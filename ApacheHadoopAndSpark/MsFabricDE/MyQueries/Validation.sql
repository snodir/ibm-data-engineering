SELECT
    p.ProductName,
    c.CustomerName,
    s.StoreName,
    d.FullDate,
    fs.TotalAmount
FROM FactSales fs
JOIN DimProduct p ON fs.ProductKey = p.ProductKey
JOIN DimCustomer c ON fs.CustomerKey = c.CustomerKey
JOIN DimStore s ON fs.StoreKey = s.StoreKey
JOIN DimDate d ON fs.DateKey = d.DateKey;