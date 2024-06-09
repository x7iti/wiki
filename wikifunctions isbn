def is_valid_isbn(isbn):
    # Remove spaces and hyphens
    isbn = isbn.replace(' ', '').replace('-', '')
    
    # Check if ISBN is ISBN-10
    if len(isbn) == 10:
        if not isbn[:9].isdigit() or (isbn[-1] not in '0123456789Xx'):
            return False
        checksum = sum((i + 1) * (10 if x in 'Xx' else int(x)) for i, x in enumerate(isbn))
        return checksum % 11 == 0
    
    # Check if ISBN is ISBN-13
    elif len(isbn) == 13:
        if not isbn.isdigit():
            return False
        checksum = sum((1 if i % 2 == 0 else 3) * int(x) for i, x in enumerate(isbn))
        return checksum % 10 == 0
    
    # Invalid ISBN length
    return False

# Test cases
print(is_valid_isbn('978-0-545-01022-1'))  
print(is_valid_isbn('0-306-40615-2'))      
print(is_valid_isbn('978 0 545 01022 1'))  
print(is_valid_isbn('0 306 40615 2'))      
print(is_valid_isbn('978-0-545-01022-0')) 
print(is_valid_isbn('0-306-40615-X'))     
