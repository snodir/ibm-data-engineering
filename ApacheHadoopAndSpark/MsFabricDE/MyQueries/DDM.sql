-- Mask the email address
ALTER TABLE Customers
ALTER COLUMN Email ADD MASKED WITH (FUNCTION = 'email()');

-- Show only the last four digits of the phone number
ALTER TABLE Customers
ALTER COLUMN PhoneNumber ADD MASKED WITH (FUNCTION = 'partial(0,"XXX-XXX-",4)');

-- Show only the last four digits of the credit card number
ALTER TABLE Customers
ALTER COLUMN CreditCardNumber ADD MASKED WITH (FUNCTION = 'partial(0,"XXXX-XXXX-XXXX-",4)');


-- Allow a data engineer to manage masking rules without granting admin rights
GRANT ALTER ANY MASK TO [engineer@contoso.com];


-- Grant a specific user the ability to see unmasked data
GRANT UNMASK ON dbo.Customers TO [user@contoso.com];


REVOKE UNMASK ON dbo.Customers FROM [user@contoso.com];
