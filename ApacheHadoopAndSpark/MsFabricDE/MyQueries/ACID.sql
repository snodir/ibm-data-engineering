BEGIN TRANSACTION;
-- Step 1: Decrease stock in the Inventory table.
UPDATE Inventory SET StockCount = StockCount - 1 WHERE ProductID = 123;
 
-- Step 2: Create a new record in the Shipments table.
INSERT INTO Shipments (OrderID, ShipDate, Carrier) VALUES (456, GETDATE(), 'Express');
 
-- Step 3: Create a new record in the Invoices table.
INSERT INTO Invoices (OrderID, Amount, DueDate) VALUES (456, 99.99, DATEADD(day, 30, GETDATE()));
 
-- If all steps are successful, commit the transaction.
COMMIT TRANSACTION;


BEGIN TRY
	BEGIN TRANSACTION;
 
	-- Execute multi-table operations.
	UPDATE Inventory SET StockCount = StockCount - 1 WHERE ProductID = 123;
	INSERT INTO Shipments (OrderID, ShipDate, Carrier) VALUES (456, GETDATE(), 'Express');
	INSERT INTO Invoices (OrderID, Amount, DueDate) VALUES (456, 99.99, DATEADD(day, 30, GETDATE()));
 
	COMMIT TRANSACTION;
END TRY
BEGIN CATCH
	-- Roll back if transaction is invalid.
	IF (XACT_STATE()) = -1
	BEGIN
    	ROLLBACK TRANSACTION;
	END;
 
	-- Optionally log the error for review.
	-- SELECT ERROR_NUMBER(), ERROR_MESSAGE();
END CATCH;