Feature: Cart Discount
    As a customer 
    I want to get a discount
    So that i can save money

  Scenario: Add a product with a price greater than $100 to apply a discount
    Given a shopping cart with no products
    When I add a product with price 200.0 
    Then the cart the total should be 180.0

  Scenario: Add a product with a price greater than $100 to apply a discount
    Given a shopping cart with no products
    When I add a product with price 150.0 
    Then the cart the total should be 135.0