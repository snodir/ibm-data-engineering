-- Create a schema for security objects
CREATE SCHEMA [Sec];
GO

-- Define the filter predicate
CREATE FUNCTION sec.tvf_SecurityPredicateBySalesPerson(@SalesPerson AS NVARCHAR(50))
    RETURNS TABLE
WITH SCHEMABINDING
AS
    RETURN SELECT 1 AS result
           WHERE @SalesPerson = USER_NAME()
              OR USER_NAME() = 'salesadmin@contoso.com';
GO

-- Apply the policy to the Sales table
CREATE SECURITY POLICY sec.SalesPolicy
ADD FILTER PREDICATE sec.tvf_SecurityPredicateBySalesPerson(SalesPerson) ON [dbo].[Sales]
WITH (STATE = ON);
GO
