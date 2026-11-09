# EGN 475 – Week 2 Assignment 2.1
## User Stories and Acceptance Criteria
### Project: Café Calle Ocho

## 1. User Stories

### Story 1 – View Menu and Prices
**Priority:** Must have

As a first-time café customer, I want to see the prices of available food and drinks on the café menu, so that I can choose what to order within my budget.

**Acceptance Criteria 1**
- Given the café menu contains available food and drinks,
- When the customer opens the menu,
- Then the menu displays item names and prices.

**Acceptance Criteria 2 – Edge Case**
- Given a food or drink item is sold out,
- When the customer views the menu,
- Then the item is marked sold out and cannot be ordered.

### Story 2 – Place an Order
**Priority:** Must have

As a returning café customer, I want to place a food and drink order, so that I can order my meal before arriving at the café.

Acceptance Criterion 1
- Given: I have added at least one available food or drink item to my cart.
- When: I submit my order with a valid pickup time.
- Then: My order is successfully submitted and I receive an order number.
Acceptance Criterion 2 – Edge Case
- Given: My cart is empty.
- When: I try to submit my order.
- Then: I see a message asking me to add at least one item, and the order is not submitted.

### Story 3 – Select Pickup Time
**Priority:** Must have

As a customer placing an order, I want to select a pickup time for my order, so that I can collect my food when it is convenient for me.
Replace Acceptance Criterion 1 with:
- Given: The café has pickup times available during its operating hours.
- When: The customer views the pickup-time options.
- Then: Only available pickup times are displayed.
Keep Acceptance Criterion 2 as it is:
- Given: The café has no available pickup times.
- When: The customer tries to select a pickup time.
- Then: A message explains that no pickup times are available.
### Story 4 – Add an Item to the Cart
**Priority:** Must have

As a café customer placing an order, I want to add a food or drink item to my cart, so that I can review the items I want before submitting my order.

**Acceptance Criteria 1**
- Given the café menu displays available food and drinks,
- When I select an available item and add it to my cart,
- Then the selected item appears in my cart with its name, quantity, and price.

**Acceptance Criteria 2 – Edge Case**
- Given a food or drink item is sold out,
- When I try to add that item to my cart,
- Then the item is not added, and I see a message that it is sold out.

### Story 5 – View Order Confirmation
**Priority:** Must have

As a café customer who has placed an order, I want to view my order confirmation, so that I can make sure my order was successfully submitted.

*Acceptance Criterion 1
- Given: I have submitted an order with at least one item and a valid pickup time.
- When: The order is saved successfully.
- Then: I see a confirmation message with my order number and selected pickup time.
Acceptance Criterion 2 (Edge Case)
- Given: I submit an order with missing required information or an unavailable pickup time.
- When: I try to submit the order.
- Then: I see an error message identifying what needs to be corrected, and the order is not submitted.

### Story 6 – Check Order Status
**Priority:** Must have

As a café customer waiting for an order, I want to check the status of my order, so that I know when my food will be ready for pickup.

**Acceptance Criteria 1**
- Given I have a valid order number,
- When I check my order status,
- Then I see whether my order is received, preparing, or ready for pickup.

**Acceptance Criteria 2 – Edge Case**
- Given I enter an order number that does not exist,
- When I check the order status,
- Then I see a message saying the order could not be found.

### Story 7 – View New Customer Orders
**Priority:** Must have

As a kitchen staff member preparing café orders, I want to view all new customer orders, so that I can see which orders need to be prepared.

Acceptance Criterion 1
- Given: Customers have submitted orders that have not yet been started by kitchen staff.
- When: I open the kitchen order page.
- Then: I see a list of all unstarted orders with their order numbers and items.
Acceptance Criterion 2 (Edge Case)
- Given: No unstarted customer orders exist.
- When: I open the kitchen order page.
- Then: I see a message saying there are no new orders to prepare.
### Story 8 – Update Order Status
**Priority:** Must have

As a kitchen staff member managing café orders, I want to update an order's status to preparing, so that customers can know that their food is being prepared.

**Acceptance Criteria 1**
- Given a customer order has been received,
- When kitchen staff selects the order and marks it as preparing,
- Then the order status changes to preparing.

**Acceptance Criteria 2 – Edge Case**
- Given an order has already been cancelled,
- When kitchen staff tries to mark it as preparing,
- Then the status does not change, and a message explains that the cancelled order cannot be prepared.

## 2. Reflection Questions

**Question 1: Which story did you split into smaller stories, and why?**

I split the original idea of placing a food and drink order into smaller stories, including viewing the menu, adding items to the cart, selecting a pickup time, and viewing order confirmation. I split it because the original idea included several tasks. Smaller stories are easier to understand, develop, and test.

**Question 2: Which story was hardest to write acceptance criteria for? What made it hard?**

The order status story was the hardest because I needed to describe both the normal situation and an error situation. I had to make sure the system explains what happens when a customer enters an order number that does not exist.

**Copilot feedback:**

Copilot identified possible problems in Stories 1, 2, 3, 5, and 7. It found unclear or incomplete acceptance criteria and suggested that some stories needed more specific details. It found no major issues in Stories 4, 6, and 8.

**Accepted feedback:**

- Story 1: Clarify the sold-out item behavior.
- Story 2: Clarify the normal ordering process and reorder feature.
- Story 3: Make pickup-time availability more specific.
- Story 5: Clarify order confirmation and error conditions.
- Story 7: Define what counts as a new order.

**Rejected feedback:**

No suggestions were rejected because the five identified issues were reasonable. Stories 4, 6, and 8 had no major problems identified.

**Changes made:**

I clarified the sold-out menu message in Story 1, defined the normal order submission and empty-cart behavior in Story 2, specified pickup-time options in Story 3, clarified confirmation and validation errors in Story 5, and defined new/unstarted orders in Story 7.